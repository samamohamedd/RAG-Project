from pydantic import BaseModel, Field
from typing import Optional
from bson.objectid import ObjectId

class data_chunk(BaseModel):
    id: Optional[ObjectId] = Field(default=None, alias="_id")

    chunk_text: str = Field(..., min_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(..., gt=0)
    chunk_project_id: ObjectId

    class Config:
        arbitrary_types_allowed = True
        populate_by_name = True

    @classmethod
    def get_indexes(cls):
        return [
            {}
        ]