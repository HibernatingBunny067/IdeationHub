from langchain_ollama import ChatOllama
from schemas import Idea,Ideas
from prompts import input_prompt,deduplication_prompt
from langchain_core.runnables import RunnableParallel
from typing import List

idea_llm = ChatOllama(model="gpt-oss:20b-cloud", temperature=0.3)
chat_llm = ChatOllama(model='gpt-oss:20b-cloud',temperature=0.4)
curator_llm = ChatOllama(model="gpt-oss:20b-cloud", temperature=0.1)

structured_llm = idea_llm.with_structured_output(Idea)
curated_llm = curator_llm.with_structured_output(Ideas)

idea_chain = input_prompt | structured_llm
curator_chain = deduplication_prompt | curated_llm


def make_parallel(n:int,chain) -> RunnableParallel:
    return RunnableParallel(
        **{f'idea_{i}':chain for i in range(n)}
    )


parallel_chain = make_parallel(5,idea_chain)


async def generate_curated_ideas(input_dict:dict) -> List[Idea]:
    output = await parallel_chain.ainvoke(input_dict)

    ideas = list(output.values())
    ideas_json = [idea.model_dump() for idea in ideas]

    final_output = await curator_chain.ainvoke({
        'skill_level':input_dict['skill_level'],
        'career_goal':input_dict['career_goal'],
        'ideas':ideas_json
    })
    
    return final_output


if __name__ == "__main__":
    chain = input_prompt | structured_llm
    currator_chain = deduplication_prompt | currator_llm
    parallel_chain = make_parallel(5,chain)

    input_data = {
        'skill_level':'beginner',
        'domain':'web-development',
        'career_goal':'frontend developer'
    }

    output = parallel_chain.ainvoke(input_data) 

    ideas = list(output.values())
    ideas_json = [idea.model_dump() for idea in ideas]
    print(len(ideas))
    final_output = currator_chain.invoke({
        'skill_level':input_data['skill_level'],
        'career_goal':input_data['career_goal'],
        'ideas':ideas_json
    })

    print(final_output)

