from pydantic import BaseModel, StrictStr, Field


class LoginCredential(BaseModel):
    login: StrictStr = Field(min_length=2)
    password: StrictStr = Field(min_length=6)
    rememberMe: bool = Field(default=True)
