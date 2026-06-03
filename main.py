from fastapi import FastAPI, Request, Query, Form
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from models.student_by_group import get_students_by_group, get_unique_subjects
from models.get_mappings import get_mappings
from models.get_groups import get_groups
from models.map import add_mapping_by_code
from models.delete_mapping import delete_mapping_by_code

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse("static/images/favicon.ico")

@app.get("/", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    return templates.TemplateResponse(request, "login.html")

@app.get("/menu", response_class=HTMLResponse)
async def get_study_groups(request: Request):
    return templates.TemplateResponse(request, "main_menu.html")

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
    subjects = get_unique_subjects(group_name)
    return templates.TemplateResponse(
        request, "marks.html",
        {"request": request, "marks_table": marks_table, "subjects": subjects}
    )

@app.get("/mapping", response_class=HTMLResponse)
async def get_dashboard(request: Request, q: str = Query('', alias='q')):
    mappings_table = get_mappings()
    if q:
        q_lower = q.lower()
        mappings_table = [
            m for m in mappings_table
            if q_lower in (
                str(m.get("ithub_name", "")).lower() + " " +
                str(m.get("code_dis", "")).lower() + " " +
                str(m.get("vvsu_name", "")).lower() + " " +
                str(m.get("vvsu_id", "")).lower()
            )
        ]
    return templates.TemplateResponse(
        request, "mapping.html",
        {"request": request, "mappings_table": mappings_table, "q": q}
    )

@app.post("/map")
async def create_mapping(request: Request, code_dis: str = Form(...), vvsu_id_dis: str = Form(...), q: str = Query('', alias='q')):
    try:
        add_mapping_by_code(code_dis, vvsu_id_dis)
    except Exception as e:
        mappings_table = get_mappings()
        if q:
            q_lower = q.lower()
            mappings_table = [
                m for m in mappings_table
                if q_lower in (
                    str(m.get("ithub_name", "")).lower() + " " +
                    str(m.get("code_dis", "")).lower() + " " +
                    str(m.get("vvsu_name", "")).lower() + " " +
                    str(m.get("vvsu_id", "")).lower()
                )
            ]
        return templates.TemplateResponse(
            request, "mapping.html",
            {"request": request, "mappings_table": mappings_table, "q": q, "error": e}
        )

@app.post("/delete")
async def create_mapping(request: Request, code_dis: str = Form(...), vvsu_id_dis: str = Form(...), q: str = Query('', alias='q')):
    try:
        delete_mapping_by_code(code_dis, vvsu_id_dis)
        mappings_table = get_mappings()
        if q:
            q_lower = q.lower()
            mappings_table = [
                m for m in mappings_table
                if q_lower in (
                    str(m.get("ithub_name", "")).lower() + " " +
                    str(m.get("code_dis", "")).lower() + " " +
                    str(m.get("vvsu_name", "")).lower() + " " +
                    str(m.get("vvsu_id", "")).lower()
                )
            ]
        return templates.TemplateResponse(
            request, "mapping.html",
            {"request": request, "mappings_table": mappings_table, "q": q}
        )
    except Exception as e:
        mappings_table = get_mappings()
        if q:
            q_lower = q.lower()
            mappings_table = [
                m for m in mappings_table
                if q_lower in (
                    str(m.get("ithub_name", "")).lower() + " " +
                    str(m.get("code_dis", "")).lower() + " " +
                    str(m.get("vvsu_name", "")).lower() + " " +
                    str(m.get("vvsu_id", "")).lower()
                )
            ]
        return templates.TemplateResponse(
            request, "mapping.html",
            {"request": request, "mappings_table": mappings_table, "q": q, "error": e}
        )