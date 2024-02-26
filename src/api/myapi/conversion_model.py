from pydantic import BaseModel, Field
from typing import Optional

class ConversionResponse(BaseModel):
    filename: str
    content_type: str
    content: bytes = Field(..., description="The content of the converted file as a byte string.")
