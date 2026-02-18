from pydantic import BaseModel
from typing import List,Literal

class IdeaReq(BaseModel):
    skill_level: Literal['begineer','intermediate','advanced']
    domain:str
    career_goal:str

class Idea(BaseModel):
    title:str
    problem_statement:str
    prerequisites:List[str]
    features:List[str]
    tech_stack:List[str]
    difficulty:Literal['easy','intermediate','advanced']

class Ideas(BaseModel):
    ideas:List[Idea]

class ChatMessage(BaseModel):
    role: Literal['user','assistant']
    content:str

class ConvIdeaReq(BaseModel):
    idea:Idea
    user_message:str
    last_messages: List[ChatMessage]
    user_idea_info: IdeaReq
