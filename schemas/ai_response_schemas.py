from pydantic import BaseModel
from typing import List

class AIRequest(BaseModel):
    message: str
    images: List[str] = [] # List of base64 strings
    system_prompt: str = "You are a helpful assistant."

class AIResponse(BaseModel):
    response: str