from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.services.course_services import (get_course,
                                          create_course_service,
                                          update_course_service,
                                          delete_course_service)
from app.models import (CourseResponse,
                        CourseCreate,
                        CourseUpdate)


router = APIRouter(tags=["Courses"])

@router.delete("/{course_id}", status_code=204)
async def delete_course_endpoint(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):
    await delete_course_service(db, course_id)
    return None


@router.patch("/{course_id}", response_model=CourseResponse)
async def update_course_endpoint(
    course_id: int,
    course_data: CourseUpdate,
    db: AsyncSession = Depends(get_db),
):
    return await update_course_service(db, course_id, course_data)


@router.get(
    "/courses/{course_id}",
    response_model=CourseResponse,
)
async def send_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):
    course = await get_course(db, course_id)
    return course


@router.post("/", response_model=CourseResponse, status_code=201)
async def create_course_endpoint(
    course_data: CourseCreate,
    db: AsyncSession = Depends(get_db),
):
    return await create_course_service(db, course_data)