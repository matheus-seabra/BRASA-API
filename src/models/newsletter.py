from beanie import Document
from pydantic import BaseModel
from src.core.constants import NEWSLETTER_COLLECTIONS
from src.models.base import Response


class Newsletter(Document):
    email: str

    class Settings:
        name = NEWSLETTER_COLLECTIONS

    class Config:
        schema_extra = {"example": {"email": "some_email@ucf.edu"}}


class NewsletterRequestModel(BaseModel):
    email: str


class NewsletterResponse(Response):
    data: NewsletterRequestModel | None
