from datetime import datetime

from fastapi import APIRouter, HTTPException, status

from core.config import settings
from core.constants import SUCCESS
from models.base import Response
from models.newsletter import NewsletterRequestModel
from src.db.operations import add_newsletter

# from schemas.prediction import TestRequest, TestResponse


settings.app_tags_metadata.append(
    {"name": "Newsletter", "description": "Newsletter endpoint"}
)
router = APIRouter(prefix="/newsletter", tags=["Newsletter"])


@router.post(
    path="/addNewsletterEmail",
    response_model=Response,
    name="Test endpoint",
)
async def mama(body: NewsletterRequestModel):
    try:
        await add_newsletter(body)
        print("hello")
        return Response(
            status_code=status.HTTP_200_OK,
            response_type=SUCCESS,
            description="Successfully got a service",
            data=datetime.now().strftime("%Hh:%Mm:%Ss"),
        )

    except Exception:
        raise HTTPException(status_code=404, detail="Some Exception")
