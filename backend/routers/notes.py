from fastapi import APIRouter

router = APIRouter()


@router.get("/notes")
async def get_notes():
    return {"notes": []}  # Currently returns an empty list
