from pydantic import BaseModel, EmailStr
from typing import Optional, List

class ComplimentRequest(BaseModel):
    recipient_name: str
    relationship: str  # e.g., "student", "child", "colleague"
    qualities: List[str]  # e.g., ["creative", "persistent", "kind"]
    context: Optional[str] = None  # Recent achievement or situation
    tone: Optional[str] = "warm"  # "warm", "encouraging", "celebratory"

class ComplimentResponse(BaseModel):
    compliment: str
    generated_at: str

class EmailRequest(BaseModel):
    recipient_email: EmailStr
    recipient_name: str
    compliment: str
    sender_name: Optional[str] = "A Nurtured Heart Friend"

