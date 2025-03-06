from bson import ObjectId
from fastapi import APIRouter, Body, HTTPException, Request, status
from app.models.car_model import CarModel, CarCollection

cars_router = APIRouter()


@cars_router.post(
    "/",
    response_description="Add new car",
    response_model=CarModel,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def add_car(request: Request, car: CarModel = Body(...)):
    cars = request.app.db["cars"]
    document = car.model_dump(by_alias=True, exclude=["id"])
    inserted = await cars.insert_one(document)
    return await cars.find_one({"_id": inserted.inserted_id})


@cars_router.get(
    "/",
    response_description="List all cars",
    response_model=CarCollection,
    response_model_by_alias=False,
)
async def list_cars(request: Request):
    cars = request.app.db["cars"]
    results = []
    cursor = cars.find()
    async for document in cursor:
        results.append(document)
    return CarCollection(cars=results)


@cars_router.get(
    "/{id}",
    response_description="Get a single car by ID",
    response_model=CarModel,
    response_model_by_alias=False,
)
async def show_car(id: str, request: Request):
    cars = request.app.db["cars"]
    try:
        id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=404, detail=f"Car {id} not found")
    if (car := await cars.find_one({"_id": ObjectId(id)})) is not None:
        return car
    raise HTTPException(status_code=404, detail=f"Car {id} not found")
