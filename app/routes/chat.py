from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_engine import generate_response

# Define the request schema
class ChatRequest(BaseModel):
    query: str
    domain: str = "general"

chat_router = APIRouter()

@chat_router.post("/")
async def chat(req: ChatRequest):
    response = generate_response(req.query, req.domain)
    return {"response": response}
