import json

from pydantic import BaseModel, model_validator


class InputModel(BaseModel):
    src_format: str
    target_format: str

    @model_validator(mode='before')
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class ConversionResponse(BaseModel):
    file_type: str
    file_data: str
