import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import engine, Base

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("✅ Database connected successfully!")
    yield  # Continue running the app
    logger.info("🛑 Shutting down the application...")


# Initialize FastAPI app with lifespan event handler
app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
