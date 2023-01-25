from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src import crud, models, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db(): # pragma: no cover

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/employees/", response_model=List[schemas.Employee])
def get_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    employees = crud.get_employees(db, skip=skip, limit=limit)
    return employees      

@app.get("/employees/{employee_id}", response_model=schemas.Employee)
def read_employee_by_id(employee_id: int, db: Session = Depends(get_db)):

    db_employee = crud.get_employee_by_id(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@app.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):

    db_employee = crud.get_employee_by_name(db, name=employee.name)
    if db_employee:
        raise HTTPException(status_code=400, detail="Employee name is already exist")
    return crud.create_employee(db=db, employee=employee)




@app.get("/contracts/", response_model=List[schemas.Сontract])
def read_contracts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    contracts = crud.get_contracts(db, skip=skip, limit=limit)
    return contracts

@app.get("/contracts/{contract_id}", response_model=schemas.Сontract)
def read_contract_by_id(contract_id: int, db: Session = Depends(get_db)):

    db_contract = crud.get_contract_by_id(db, contract_id=contract_id)
    if db_contract is None:
        raise HTTPException(status_code=404, detail="Contract not found")
    return db_contract

@app.post("/contracts/", response_model=schemas.Сontract)
def create_contract(contract: schemas.СontractCreate, db: Session = Depends(get_db)):

    return crud.create_contract(db=db, contract=contract)










@app.get("/organizations/", response_model=List[schemas.Organization])
def read_organizations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    organizations = crud.get_organizations(db, skip=skip, limit=limit)
    return organizations

@app.get("/organizations/{organization_id}", response_model=schemas.Organization)
def read_organization_by_id(organization_id: int, db: Session = Depends(get_db)):

    db_organization = crud.get_organization_by_id(db, organization_id=organization_id)
    if db_organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_organization

@app.post("/organizations/{contract_id}/contract/", response_model=schemas.Organization)
def create_organization_for_contract(contract_id: int, organization: schemas.OrganizationCreate, db: Session = Depends(get_db)):
    
    return crud.create_organization_for_contract(db=db, organization=organization, contract_id=contract_id)



@app.get("/shipments/", response_model=List[schemas.Shipment])
def read_shipments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    shipments = crud.get_shipments(db, skip=skip, limit=limit)
    return shipments

@app.get("/shipments/{shipment_id}", response_model=schemas.Shipment)
def read_shipment_by_id(shipment_id: int, db: Session = Depends(get_db)):

    db_shipment = crud.get_shipment_by_id(db, shipment_id=shipment_id)
    if db_shipment is None:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return db_shipment

@app.post("/shipments/{contract_id}/employee/{employee_id}", response_model=schemas.Shipment)
def create_shipment_for_employee_contract(employee_id: int, contract_id:int, shipment: schemas.ShipmentCreate, db: Session = Depends(get_db)):
    
    return crud.create_shipment_for_employee_contract(db=db, shipment=shipment, contract_id=contract_id, employee_id=employee_id)

