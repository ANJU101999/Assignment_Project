from typing import List
from .models import AddressInDB


class AddressDistanceQuery(BaseModel):
    latitude: float
    longitude: float
    distance: float


class AddressListSchema(BaseModel):
    addresses: List[AddressInDB]
