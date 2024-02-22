import os
from dotenv import dotenv_values
from fastapi import FastAPI, Body, HTTPException, status
import motor.motor_asyncio

from pydantic.functional_validators import BeforeValidator

from typing_extensions import Annotated

config = dotenv_values(".env")

client = motor.motor_asyncio.AsyncIOMotorClient(config["MONGODB_URL"],
                                                username=config["MONGODB_USERNAME"], 
                                                password=config["MONGODB_PASSWORD"])
db = client.get_database("store")
products_collection = db.get_collection("products")

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]
