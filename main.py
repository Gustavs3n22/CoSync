from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from models.student_by_group import get_students_by_group
from models.get_groups import get_groups

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")

@app.get("/", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    return templates.TemplateResponse(request, "login.html")

@app.get("/groups", response_class=HTMLResponse)
async def get_study_groups(request: Request):
    groups_table = get_groups()
    return templates.TemplateResponse(
        request,
        "groups.html",
        {"request": request,
         "groups_table": groups_table}
    )

@app.get("/marks", response_class=HTMLResponse)
async def get_dashboard(request: Request, group_name: str):
    marks_table = get_students_by_group(group_name)
    return templates.TemplateResponse(
        request,
        "marks.html",
        {"request": request,
         "marks_table": marks_table}
    )