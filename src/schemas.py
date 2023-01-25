from pydantic import BaseModel
from datetime import date
from typing import List, Optional


class ShipmentBase(BaseModel):
    type_of_equipment: str
    comment: Optional[str] = None


class ShipmentCreate(ShipmentBase):
    pass


class Shipment(ShipmentBase):
    id: int
    employee_id: int
    contract_id: int

    class Config:
        """
        Задание настройки для возможности работать с объектами ORM
        """
        orm_mode = True




class OrganizationBase(BaseModel):
    country_code: int
    city: str
    address: str
    telephone: str
    email: str
    website_address: Optional[str] = None


class OrganizationCreate(OrganizationBase):
    pass


class Organization(OrganizationBase):
    id: int
    contract_id: int

    class Config:
        """
        Задание настройки для возможности работать с объектами ORM
        """
        orm_mode = True





class EmployeeBase(BaseModel):
    department_code: int
    name: str
    post: str
    salary: int
    premium: int


class EmployeeCreate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id: int
    shipments: List[Shipment] = []


    class Config:
        """
        Задание настройки для возможности работать с объектами ORM
        """
        orm_mode = True




class СontractBase(BaseModel):
    Org_name: str
    date_contract: date


class СontractCreate(СontractBase):
    pass


class Сontract(СontractBase):
    id: int
    shipments: List[Shipment] = []
    organizations: List[Organization] = []



    class Config:
        """
        Задание настройки для возможности работать с объектами ORM
        """
        orm_mode = True
