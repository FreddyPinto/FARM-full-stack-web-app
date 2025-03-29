from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import BaseConfig
from app.routers.cars import cars_router
from app.routers.users import users_router

settings = BaseConfig()


async def lifespan(app: FastAPI):
    app.client = AsyncIOMotorClient(settings.DB_URL)
    app.db = app.client[settings.DB_NAME]
    try:
        # Prueba la conexión a MongoDB
        await app.client.admin.command("ping")
        print("Pinged your deployment. You have successfully connected to MongoDB!")
        print("Mongo address:", settings.DB_URL)
    except Exception as e:
        print("Failed to ping MongoDB:", e)
    yield
    # Cerrar la conexión a MongoDB al terminar
    app.client.close()


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(cars_router, prefix="/cars", tags=["cars"])
app.include_router(users_router, prefix="/users", tags=["users"])

@app.get("/")
async def get_root():
    return {"Message": "Root working"}
