from pydantic import BaseModel, StrictStr, Field


class ResetPassword(BaseModel):
    login: StrictStr = Field(min_length=2)
    email: StrictStr = Field(pattern='[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+[a-zA-Z0-9_-]+')
