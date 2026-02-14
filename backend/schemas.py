from pydantic import BaseModel
from typing import List,Literal

class IdeaReq(BaseModel):
    skill_level:str
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

class ConvIdeaReq(BaseModel):
    idea:Idea
    user_message:str
    last_messages: List[str]
    user_idea_info: IdeaReq