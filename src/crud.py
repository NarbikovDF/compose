from sqlalchemy.orm import Session

from src import models, schemas

def create_employee(db: Session, employee: schemas.EmployeeCreate):

    db_employee = models.Employee(department_code=employee.department_code, name=employee.name, post=employee.post, salary=employee.salary, premium=employee.premium)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def create_shipment_for_employee_contract(db: Session, shipment: schemas.ShipmentCreate, contract_id: int, employee_id: int):

    db_shipment = models.Shipment(**shipment.dict(), contract_id=contract_id, employee_id=employee_id)
    db.add(db_shipment)
    db.commit()
    db.refresh(db_shipment)
    return db_shipment

def create_contract(db: Session, contract: schemas.СontractCreate):

    db_contract = models.Сontract(Org_name=contract.Org_name, date_contract=contract.date_contract)
    db.add(db_contract)
    db.commit()
    db.refresh(db_contract)
    return db_contract    

def create_organization_for_contract(db: Session, organization: schemas.OrganizationCreate, contract_id: int):

    db_organization = models.Organization(**organization.dict(), contract_id=contract_id)
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization


def get_employee_by_id(db: Session, employee_id: int):

    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def get_shipment_by_id(db: Session, shipment_id: int):

    return db.query(models.Shipment).filter(models.Shipment.id == shipment_id).first() 

def get_contract_by_id(db: Session, contract_id: int):
 
    return db.query(models.Сontract).filter(models.Сontract.id == contract_id).first()


def get_organization_by_id(db: Session, organization_id: int):
    return db.query(models.Organization).filter(models.Organization.id == organization_id).first()




def get_employee_by_name(db: Session, name: str):
    return db.query(models.Employee).filter(models.Employee.name == name).first()


def get_employees(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Employee).offset(skip).limit(limit).all()

def get_shipments(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Shipment).offset(skip).limit(limit).all()

def get_contracts(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Сontract).offset(skip).limit(limit).all()

def get_organizations(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Organization).offset(skip).limit(limit).all()