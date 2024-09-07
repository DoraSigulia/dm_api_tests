from pydantic import BaseModel, StrictStr, Field


class ChangePassword(BaseModel):
    login: StrictStr = Field(min_length=2)
    token: StrictStr
    old_password: StrictStr = Field(alias='oldPassword', min_length=6)
    new_password: StrictStr = Field(alias='newPassword', min_length=6)
