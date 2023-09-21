from db.init_db import brasa_users_collection, brasa_newsletter_collection
from models.services import Service
from models.user import User, UsernameModel
from src.models.newsletter import Newsletter, NewsletterRequestModel

user_collection = User
service_collection = Service
newsletter_collection = Newsletter


async def add_user(new_user: User) -> User | None:
    return await new_user.insert_one(new_user)


async def add_newsletter(new_email: NewsletterRequestModel) -> Newsletter:
    return await brasa_newsletter_collection.insert_one(new_email.email)


async def find_user(user_info: UsernameModel) -> User:
    return await brasa_users_collection.find_one({"username": user_info.username})
