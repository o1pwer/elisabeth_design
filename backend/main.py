import asyncio
import logging

import uvicorn as uvicorn
from fastapi import FastAPI

from database import engine
from models import DatabaseModel
from routers.api import api_router

app = FastAPI()
app.include_router(api_router)
logger = logging.getLogger(__name__)


async def main():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(DatabaseModel.metadata.create_all)
    finally:
        await engine.dispose()


if __name__ == '__main__':
    try:
        asyncio.run(main())
        uvicorn.run("main:app", port=8888, log_level="info")
    except (KeyboardInterrupt, SystemExit):
        logger.error("App stopped!")
