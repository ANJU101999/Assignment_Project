from pydantic import BaseModel


class AddressBase(BaseModel):
    street: str
    city: str
    state: str
    postal_code: str
    latitude: float
    longitude: float


class AddressCreate(AddressBase):
    pass


class AddressUpdate(BaseModel):
    street: str = None
    city: str = None
    state: str = None
    postal_code: str = None
    latitude: float = None
    longitude: float = None


class AddressInDB(AddressBase):
    id: int
