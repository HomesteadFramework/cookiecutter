import os
import fastapi_jinja
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config import settings, Settings
from app.cors import get_cors_domains

app = FastAPI()

# Mount static file directory
app.mount("/static", StaticFiles(directory="static"), name="static")


def configure(settings_obj: Settings):
    configure_cors(settings_obj.app_env)
    configure_views(settings_obj)
    configure_middleware()
    configure_routes()


def configure_views(settings):
    # Setup Jinja2 templates
    dev_mode = settings.dev_mode
    folder = os.path.dirname(__file__)
    template_folder = os.path.join(folder, 'app/views')
    template_folder = os.path.abspath(template_folder)
    fastapi_jinja.global_init(template_folder, auto_reload=dev_mode)


def configure_cors(env: str):
    origins = get_cors_domains(env)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def configure_middleware():
    pass


def configure_db():
    pass


def configure_routes():
    @app.get("/health")
    async def root():
        return {"message": "Health Response"}

    # Routes from other routers
    from app.modules.welcome.controller import router as welcome_router
    app.include_router(welcome_router)
    

configure(settings.app_env)
