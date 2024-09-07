from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, StrictStr, StrictBool, AwareDatetime, Field


class Roles(Enum):
    GUEST = 'Guest'
    PLAYER = 'Player'
    ADMINISTRATOR = 'Administrator'
    NANNY_MODERATOR = 'NannyModerator'
    REGULAR_MODERATOR = 'RegularModerator'
    SENIOR_MODERATOR = 'SeniorModerator'


class Rating(BaseModel):
    enabled: StrictBool
    quality: int
    quantity: int


class User(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(alias='mediumPictureUrl', default=None)
    small_picture_url: Optional[StrictStr] = Field(alias='smallPictureUrl', default=None)
    status: Optional[StrictStr] = Field(default=None)
    rating: Rating
    online: Optional[AwareDatetime] = Field(default=None)
    name: Optional[StrictStr] = Field(default=None)
    location: Optional[StrictStr] = Field(default=None)
    registration: Optional[AwareDatetime] = Field(default=None)


class Metadata(BaseModel):
    email: Optional[StrictStr] = Field(default=None)


class UserEnvelope(BaseModel):
    resource: Optional[User] = Field(default=None)
    metadata: Optional[Metadata] = Field(default=None)
