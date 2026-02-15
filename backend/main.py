from fastapi import FastAPI
import uvicorn
from schemas import IdeaReq,ConvIdeaReq
from llm_engine import generate_curated_ideas

app = FastAPI()

@app.post('/generate')
async def generate_ideas(req:IdeaReq):
    return await generate_curated_ideas(req.model_dump())

@app.post('/discuss')
async def discuss(req:ConvIdeaReq):
    pass


def run():
    uvicorn.run(app = app,host='127.0.0.0',port=6969,reload=True)

if __name__ == '__main__':
    uvicorn.run(app=app)

