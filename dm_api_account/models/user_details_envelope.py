from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, StrictStr, StrictBool, AwareDatetime, Field


class UserRoles(Enum):
    GUEST = 'Guest'
    PLAYER = 'Player'
    ADMINISTRATOR = 'Administrator'
    NANNY_MODERATOR = 'NannyModerator'
    REGULAR_MODERATOR = 'RegularModerator'
    SENIOR_MODERATOR = 'SeniorModerator'


class BbParseMode(Enum):
    COMMON = 'Common'
    INFO = 'Info'
    POST = 'Post'
    CHAT = 'Chat'


class ColorSchema(Enum):
    MODERN = 'Modern'
    PALE = 'Pale'
    CLASSIC = 'Classic'
    CLASSICPALE = 'ClassicPale'
    NIGHT = 'Night'


class PagingSettings(BaseModel):
    posts_per_page: Optional[int] = Field(alias='postsPerPage', default=None)
    comments_per_page: Optional[int] = Field(alias='commentsPerPage', default=None)
    topics_Per_page: Optional[int] = Field(alias='topicsPerPage', default=None)
    messages_per_page: Optional[int] = Field(alias='messagesPerPage', default=None)
    entities_per_page: Optional[int] = Field(alias='entitiesPerPage', default=None)


class UserSettings(BaseModel):
    color_schema: List[ColorSchema]
    nanny_greetings_message: Optional[StrictStr] = Field(alias='nannyGreetingsMessage', default=None)
    paging: PagingSettings


class InfoBbText(BaseModel):
    value: Optional[StrictStr] = Field(default=None)
    parse_mode: List[BbParseMode]


class Rating(BaseModel):
    enabled: StrictBool
    quality: int
    quantity: int


class UserDetails(BaseModel):
    login: StrictStr
    role: List[UserRoles]
    medium_picture_url: Optional[StrictStr] = Field(alias='mediumPictureUrl', default=None)
    small_picture_url: Optional[StrictStr] = Field(alias='smallPictureUrl', default=None)
    status: Optional[StrictStr] = Field(default=None)
    rating: Rating
    online: Optional[AwareDatetime] = Field(default=None)
    name: Optional[StrictStr] = Field(default=None)
    location: Optional[StrictStr] = Field(default=None)
    registration: Optional[AwareDatetime] = Field(default=None)
    icq: Optional[StrictStr] = Field(default=None)
    original_picture_url: Optional[StrictStr] = Field(alias='originalPictureUrl', default=None)
    info: InfoBbText
    settings: UserSettings


class Resource(BaseModel):
    field_ref: StrictStr = Field(..., alias='$ref')


class Metadata(BaseModel):
    description: StrictStr = Field(default=None)
    nullable: bool = Field(default=None)


class Properties12(BaseModel):
    resource: Resource
    metadata: Metadata


class UserDetailsEnvelope(BaseModel):
    type: StrictStr = Field(default=None)
    properties: Properties12 = Field(default=None)
    additional_properties: bool = Field(default=None, alias='additionalProperties')
    description: StrictStr = Field(default=None)



