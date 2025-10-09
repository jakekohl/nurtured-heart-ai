
from pydantic import BaseModel, EmailStr


class ComplimentRequest(BaseModel):
    recipient_name: str
    relationship: str  # e.g., "student", "child", "colleague"
    qualities: list[str]  # e.g., ["creative", "persistent", "kind"]
    context: str | None = None  # Recent achievement or situation
    tone: str | None = "warm"  # "warm", "encouraging", "celebratory"

class ComplimentResponse(BaseModel):
    compliment: str
    generated_at: str

class EmailRequest(BaseModel):
    recipient_email: EmailStr
    recipient_name: str
    compliment: str
    sender_name: str | None = "A Nurtured Heart Friend"

