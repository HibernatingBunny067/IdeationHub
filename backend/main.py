from fastapi import FastAPI,HTTPException
import uvicorn
from schemas import IdeaReq,ConvIdeaReq
from llm_engine import generate_curated_ideas,discuss_idea

app = FastAPI()

@app.post('/generate')
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



if __name__ == '__main__':
    uvicorn.run("main:app",port=6969,reload=True)

