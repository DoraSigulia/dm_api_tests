from pydantic import BaseModel, StrictStr, Field


class ChangeEmail(BaseModel):
    login: StrictStr = Field(min_length=2)
    password: StrictStr = Field(min_length=6)
    email: StrictStr = Field(pattern='[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+')
