## we run this from the terminal using uvicorn commmand 
from fastapi import FastAPI,HTTPException
from .schemas import (
    IdeaReq,
    Ideas,
    ConvIdeaReq,
    ExecBlueprint,
    RoadMap,
    Impact)
from .llm_engine import (
    generate_curated_ideas,
    discuss_idea,
    generate_blueprint,
    generate_roadmap,
    generate_impact)

app = FastAPI()

@app.post('/generate',response_model=Ideas)
async def generate_ideas(req:IdeaReq):
    try:
        result =  await generate_curated_ideas(req.model_dump())
        return result
    except HTTPException:
        raise HTTPException(500, "Internal server error")
    except Exception as e:
        print("[GENERATION FAILED]",e)

@app.post('/discuss')
async def discuss(req:ConvIdeaReq):
    try:
        if len(req.user_message) > 1000:
            raise HTTPException(400,"message too long")
        result = await discuss_idea(req.model_dump())
        return {"response":result}
    except HTTPException as e:
        raise HTTPException(500,'Internal server error')
    except Exception as e:
        print("[DISUCSSION FAILED]",e)

@app.post('/blueprint',response_model=ExecBlueprint)
async def blueprint(req:IdeaReq):
    return await generate_blueprint(req)

@app.post('/roadmap',response_model=RoadMap)
async def roadmap(req:IdeaReq):
    return await generate_roadmap(req)

@app.post('/impact',response_model=Impact)
async def impact(req:IdeaReq):
    return await generate_impact(req)