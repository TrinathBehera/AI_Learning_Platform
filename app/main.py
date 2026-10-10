import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.routers.courses import router as courses_router
from app.routers.resources import router as resources_router
from app.exceptions import (
    CourseNotFoundError,
    ResourceNotFoundError,
    CourseCreationError,
    CourseUpdateError,
    CourseDeleteError,
    CourseReadError
)

app = FastAPI(
    title="AI Learning Platform",
    description="AI powered learning resource and tutorial platform",
    version="0.1.0",
)


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.exception_handler(CourseNotFoundError)
async def course_not_found_handler(
    request: Request,
    exc: CourseNotFoundError,
):
    return JSONResponse(
        status_code=404,
        content={"detail": "Course not found"},
    )
@app.exception_handler(CourseReadError)
async def course_read_error_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"},
    )

@app.exception_handler(CourseCreationError)
async def course_creation_error_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": "Unable to create course"},
    )


@app.exception_handler(CourseUpdateError)
async def course_update_error_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": "Unable to Update course"},
    )
@app.exception_handler(CourseDeleteError)
async def course_delete_error_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": "Unable to delete course"},
    )


@app.exception_handler(ResourceNotFoundError)
async def resource_not_found_handler(
    request: Request,
    exc: ResourceNotFoundError,
):
    return JSONResponse(
        status_code=404,
        content={"detail": "Resource not found"},
    )


@app.middleware("http")
async def log_requests(request, call_next):
    logger.info(
        "Request received: %s %s",
        request.method,
        request.url.path,
    )
    logger.info(
        "Debugging received: %s %s", 
        request.method, 
        request.url.path
    )

    response = await call_next(request)

    logger.info(
        "Response sent: status_code=%s",
        response.status_code,
    )

    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"Message": "AI Learning Platform"}


app.include_router(courses_router, prefix="/api/LIpu")
app.include_router(resources_router, prefix="/api/v1")