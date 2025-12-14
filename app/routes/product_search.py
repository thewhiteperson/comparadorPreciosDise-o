from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/product_search", response_class=HTMLResponse)
def index (request:Request):
    return templates.TemplateResponse("product-search.html", {"request":request})