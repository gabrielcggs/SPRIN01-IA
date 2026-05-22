from pydantic import BaseModel


class ResponseModel(BaseModel):

    category: str
    response: str
    confidence: float
