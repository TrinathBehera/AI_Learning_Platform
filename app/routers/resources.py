from fastapi import APIRouter
from app.models import *

router=APIRouter()

@router.get("/resources")
def send_resource(platform:str):
    return{
        "Message":"course Fetch",
        "Platform":platform
    }

@router.post("/resources", response_model=ResourceResponse)
def create_resource(resource: ResourceCreate):
    return{
        "id":30,
        "title":resource.title,
        "platform":resource.platform,
        "url": resource.url
    }
