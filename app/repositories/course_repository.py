from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from app.models import Course

async def delete_course(db, course_id: int):
    course = await get_course_by_id(db, course_id)

    if course is None:
        return None

    try:
        await db.delete(course)
        await db.commit()
        return True

    except SQLAlchemyError:
        await db.rollback()
        raise

async def get_course_by_id(
    db: AsyncSession,
    course_id: int,
):
    statement = select(Course).where(Course.id == course_id)

    result = await db.execute(statement)

    return result.scalar_one_or_none()

async def update_course(db, course_id: int, course_data):
    course = await get_course_by_id(db, course_id)

    if course is None:
        return None

    try:
        update_data = course_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(course, field, value)

        await db.commit()
        await db.refresh(course)

        return course

    except SQLAlchemyError:
        await db.rollback()
        raise

    return course

async def create_course(db, course_data):
    try:
        course = Course(
            title=course_data.title,
            category=course_data.category,
            level=course_data.level,
        )

        db.add(course)
        await db.commit()
        await db.refresh(course)

        return course

    except SQLAlchemyError:
        await db.rollback()
        raise