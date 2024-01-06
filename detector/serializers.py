from pydantic import BaseModel

class TextSampleSerializer(BaseModel):
    text: str