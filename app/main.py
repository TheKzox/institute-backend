from fastapi import FastAPI

from app.routers import users, security, students, buildings, rooms, exam, calendar1, course, lesson, category
from app.routers import schedules, credit, teachers, credit, enrollment, permission, presenting, survey

# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()

app.include_router(calendar1.router)
app.include_router(users.router)
app.include_router(security.router)
app.include_router(students.router)
app.include_router(buildings.router)
app.include_router(exam.router)
app.include_router(rooms.router)

app.include_router(schedules.router)

app.include_router(survey.router)
app.include_router(enrollment.router)
app.include_router(credit.router)
app.include_router(teachers.router)
app.include_router(permission.router)
app.include_router(presenting.router)
app.include_router(course.router)
app.include_router(lesson.router)
app.include_router(category.router)

# app.include_router(items.router)
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}