
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.models.database import get_db_session

from src.services.userService import UserService


# ------>

scheduler = AsyncIOScheduler()

async def regenEnergy():
    session = get_db_session()
    user_service = UserService(session)
    user_service.refill
    print('users energy refill')

@asynccontextmanager
async def lifespan(app: FastAPI):

    scheduler.add_job(
        regenEnergy,
        trigger="cron",
        hour=0,
        minute=0,
    )

    scheduler.start()
    yield
    scheduler.shutdown()