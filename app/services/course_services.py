from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from app.repositories.course_repository import (get_course_by_id,
                                                create_course,
                                                update_course,
                                                delete_course)
from app.exceptions import (CourseNotFoundError,
                            CourseCreationError,
                            CourseUpdateError,
                            CourseDeleteError,
                            CourseReadError)

import logging
logger = logging.getLogger(__name__)

async def delete_course_service(db, course_id: int):
    try:
        result = await delete_course(db, course_id)
        if result is None:
            raise CourseNotFoundError()

        return result
    except SQLAlchemyError as exc:
            logger.exception("Database error while deleting course")
            raise CourseDeleteError() from exc

async def update_course_service(db, course_id: int, course_data):
    
    try:
        course = await update_course(db, course_id, course_data)

        if course is None:
            raise CourseNotFoundError()

        return course
    except SQLAlchemyError as exc:
        logger.exception("Database error while updating course")
        logger.debug("Updating course_id=%s", course_id)
        raise CourseUpdateError() from exc
    

async def create_course_service(db, course_data):
    try:
        return await create_course(db, course_data)

    except SQLAlchemyError as exc:
        logger.exception("Database error while creating course")
        raise CourseCreationError() from exc


    
async def get_course(
    db: AsyncSession,
    course_id: int,
):
    try: 
    
        course = await get_course_by_id(db, course_id)

        if course is None:
            
            raise CourseNotFoundError()

        return course
    except SQLAlchemyError as exc:
            logger.exception("Database error while fetching course")
            raise CourseReadError() from exc