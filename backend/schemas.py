from pydantic import BaseModel
from typing import List,Literal

class IdeaReq(BaseModel):
    skill_level: Literal['beginner','intermediate','advanced']
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

class ExecBlueprint(BaseModel):
    project_type:str
    core_components: List[str]
    tools_and_resources: List[str]
    validation_strategy: List[str]
    risks: List[str]
    first_7_day_plan: List[str]

class Milestone(BaseModel):
    title: str
    objectives: str
    deliverables: List[str]
    success_criteria: str

class RoadMap(BaseModel):
    overview: str
    milestones: List[Milestone]
    estimated_duration_weeks:int

class Impact(BaseModel):
    measurable_outcome: str
    differentiation: str
    resume_bullet: List[str]
