from fastapi import APIRouter
import fastapi_jinja

router = APIRouter()


@router.get('/')
async def welcome_json():
    """A route that returns json data"""
    return {"Hello": "World"}


@router.get('/welcome')
@fastapi_jinja.template('welcome.html')
async def welcome_html():
    """A route that returns html data"""
    return {"framework": "Wrangler"}
