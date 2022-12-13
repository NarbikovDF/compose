from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

class BaseModel(Base):
    """
    Абстартный базовый класс, где описаны все поля и методы по умолчанию
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    def __repr__(self):
        return f"<{type(self).__name__}(id={self.id})>" # pragma: no cover

class Employee(BaseModel):
    __tablename__ = "employees"

    department_code = Column(Integer)
    name = Column(String)
    post = Column(String)
    salary = Column(Integer)
    premium = Column (Integer)

    shipment = relationship("Shipment", back_populates="employee")

class Shipment(BaseModel):
    __tablename__ = "shipments"

    type_of_equipment = Column(String)
    comment = Column(String)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    employee = relationship("Employee", back_populates="shipment")
    contract_id = Column(Integer, ForeignKey("contracts.id"))
    contract = relationship("Сontract", back_populates="shipment")


class Сontract(BaseModel):
    __tablename__ = "contracts"

    Org_name = Column(String)
    date_contract = Column(DateTime)
    shipment = relationship("Shipment", back_populates="contract")
    organization = relationship("Organization", back_populates="contract")

class Organization(BaseModel):    
    __tablename__ = "organizations"

    contract_id = Column(Integer, ForeignKey("contracts.id"))
    contract = relationship("Сontract", back_populates="organization")
    country_code = Column(Integer)
    city = Column(String)
    address = Column(String)
    telephone = Column(String)
    email = Column(String)
    website_address = Column(String)


