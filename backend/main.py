from fastapi import FastAPI
from database import engine, Base
from routers import auth, notes
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(title="Secure Notes API", version="1.0.0")

# Create database tables (ensure models are imported in database.py)
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router)
app.include_router(notes.router)


# Startup event
@app.on_event("startup")
async def startup_event():
    logger.info("🚀 Application is starting up...")


# Root route
@app.get("/")
def root():
    return {"message": "Welcome to the Secure Notes API!"}
