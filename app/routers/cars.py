from turtle import update
from bson import ObjectId
from fastapi import APIRouter, Body, Depends, HTTPException, Request, status
from pymongo import ReturnDocument
from app.models.car_model import CarModel, CarCollection, UpdateCarModel

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


@cars_router.put(
    "/{id}",
    response_description="Update car",
    response_model=CarModel,
    response_model_by_alias=False,
)
async def update_car(
    id: str,
    request: Request,
    # user=Depends(auth_handler.auth_wrapper),
    car: UpdateCarModel = Body(...),
):
    try:
        id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=404, detail=f"Car {id} not found")

    car = {
        k: v
        for k, v in car.model_dump(by_alias=True).items()
        if v is not None and k != "_id"
    }

    if len(car) >= 1:
        cars = request.app.db["cars"]

        update_result = await cars.find_one_and_update(
            {"_id": id},
            {"$set": car},
            return_document = ReturnDocument.AFTER,
        )
        if update_result is not None:
            return update_result
        else:
            raise HTTPException(status_code=404, detail=f"Car {id} not found")

    if (existing_car := await cars.find_one({"_id": id})) is not None:
        return existing_car
    raise HTTPException(status_code=404, detail=f"Car {id} not found")

@cars_router.delete(
    "/{id}",
    response_description="Delete a car",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_car(id: str, request: Request):
    try:
        id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=404, detail=f"Car {id} not found")

    cars = request.app.db["cars"]
    delete_result = await cars.delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return
    raise HTTPException(status_code=404, detail=f"Car {id} not found")

