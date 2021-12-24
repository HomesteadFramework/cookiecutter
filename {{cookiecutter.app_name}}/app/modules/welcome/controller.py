from fastapi import APIRouter, Request
import fastapi_jinja

router = APIRouter()


@router.get('/')
@fastapi_jinja.template('welcome.html')
async def welcome_html(request: Request):
    """A route that returns html data"""
    return {"framework": "Wrangler"}
