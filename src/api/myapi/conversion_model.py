from pydantic import BaseModel, Field
from typing import Optional

class ConversionResponse(BaseModel):
    file_type: str
    file_data: str
