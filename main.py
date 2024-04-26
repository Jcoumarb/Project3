from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()


# Defines API route
@app.get("/api/v1/hello")
async def api():
    return {"message": "Hello Coders. I'm literally Mark Zuckerberg"}


# Defines root route to UI
# @app.get("/")
# async def root():
#    return {"message": "Welcome to the UI (more functionality to come"}

app.mount("/", StaticFiles(directory="ui/dist", html=True), name="ui")
