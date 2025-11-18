from fastapi import FastAPI
from .controller import router
from .dependencies import init_dependencies

app = FastAPI(title="User Service", version="1.0.0")

init_dependencies()
app.include_router(router)
