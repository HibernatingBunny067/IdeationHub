from langchain_ollama import ChatOllama
from .schemas import *
from .prompts import *
from langchain_core.runnables import RunnableParallel
from typing import List
import time

idea_llm = ChatOllama(model="gpt-oss:20b-cloud", temperature=0.6,num_predict=1000,reasoning=False,validate_model_on_init=True)
chat_llm = ChatOllama(model='gpt-oss:20b-cloud',temperature=0.4,num_predict=500) ## higher temperature to be more creative
curator_llm = ChatOllama(model="gpt-oss:20b-cloud", temperature=0.1,reasoning=False)


##LLMs with structured output parsing
structured_llm = idea_llm.with_structured_output(Idea)
curated_llm = curator_llm.with_structured_output(Ideas)

##Individual LLM chains
idea_chain = input_prompt | structured_llm
curator_chain = deduplication_prompt | curated_llm
conversation_chain = conversation_prompt | chat_llm

def make_parallel(n:int,chain) -> RunnableParallel:
    diversity_modes = [
    "Focus on artistic or performance-based ideas.",
    "Focus on community-driven or collaborative ideas.",
    "Focus on experimental or unconventional formats.",
    "Focus on research-based or analytical ideas.",
    "Focus on hybrid tech + art concepts."
    ]
    return RunnableParallel(
        **{
            f'idea_{i}':chain.bind(extra_instruction = diversity_modes[i])
            for i in range(n)
        }
    )
parallel_chain = make_parallel(5,idea_chain)


async def generate_curated_ideas(input_dict:dict) -> List[Idea]:
    IN = time.time()
    output = await parallel_chain.ainvoke(input_dict)
    print('[IDEAS GENERATED] in {time:.4f} seconds'.format(time = time.time() - IN))
    ideas = list(output.values())
    ideas_json = [idea.model_dump() for idea in ideas]

    final_output = await curator_chain.ainvoke({
        'skill_level':input_dict['skill_level'],
        'career_goal':input_dict['career_goal'],
        'ideas':ideas_json
    })
    print('[EXIT IN {time:.4f} seconds]'.format(time=time.time()-IN))
    return final_output

async def discuss_idea(data:dict):
    idea_json = data['idea']

    history = [
        (msg['role'],msg['content'])
        for msg in data['last_messages']
    ]

    response = await conversation_chain.ainvoke({
        "idea":idea_json,
        "skill_level": data['user_idea_info']['skill_level'],
        "career_goal": data['user_idea_info']['career_goal'],
        "domain": data['user_idea_info']['domain'],
        "history": history,
        "user_message":data['user_message']
    })

    return response.content

async def generate_blueprint(input:dict):
    pass

async def generate_roadmap(input:dict):
    pass

async def generate_impact(input:dict):
    pass