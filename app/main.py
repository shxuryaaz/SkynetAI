from fastapi import FastAPI
from app.routes.chat import chat_router

app = FastAPI(title="IntelliChat - AI Conversational Agent")

# Add routes
app.include_router(chat_router, prefix="/chat", tags=["Chat"])
