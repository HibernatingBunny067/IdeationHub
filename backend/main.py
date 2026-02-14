from fastapi import FastAPI
import uvicorn
from .schemas import IdeaReq,ConvIdeaReq

app = FastAPI()

@app.post('/generate')
async def generate_ideas(req:IdeaReq):
    return {
        "ideas": [
            {
                "title": "Dummy Idea",
                "problem_statement": "Test problem",
                "prerequisites": ["Python"],
                "features": ["Feature 1"],
                "tech_stack": "FastAPI",
                "difficulty": "Intermediate"
            }
        ]
    }

@app.post('/discuss')
async def discuss(req:ConvIdeaReq):
    pass


def run():
    uvicorn.run(app = app,host='127.0.0.0',port=6969,reload=True)

if __name__ == '__main__':
    uvicorn.run(app=app)

