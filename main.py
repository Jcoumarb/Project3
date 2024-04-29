from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.future import select
from models import AutoModels

engine = create_async_engine("postgresql+asyncpg://postgres:postgres@db:5432/dvdrental", echo=True)

auto_models = None

async def lifespan(app):
    print("startup")
    global auto_models
    auto_models = await AutoModels.create(engine)
    yield
    print("shutdown")

app = FastAPI(lifespan=lifespan)

# Defines API route to hello
@app.get("/api/v1/hello")
async def api():
    return {"message": "Hello Coders. I'm literally Mark Zuckerberg"}

#Defines API route to db query
@app.get("/api/v1/films")
async def films():
    Film = await auto_models.get("film")

    results = []

    async with AsyncSession(engine) as session:
        films = await session.execute(select(Film))
        for film in films.scalars().all():
            results.append(
                {
                    "title": film.title,
                    "description": film.description,
                    "id": film.film_id,
                })
    
    return results
            
# Defines root route to UI
# @app.get("/")
# async def root():
#    return {"message": "Welcome to the UI (more functionality to come"}

app.mount("/", StaticFiles(directory="ui/dist", html=True), name="ui")
