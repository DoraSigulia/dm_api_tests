from pydantic import BaseModel, StrictStr, Field


class Registration(BaseModel):
    login: StrictStr = Field()
    email: StrictStr = Field()
    password: StrictStr = Field()
