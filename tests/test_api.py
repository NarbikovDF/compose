from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app, get_db
from src.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite_base.db"  # Тестовая БД

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)  # Удалем таблицы из БД
Base.metadata.create_all(bind=engine)  # Создаем таблицы в БД

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db  # Делаем подмену

client = TestClient(app)  # создаем тестовый клиент к нашему приложению


def test_create_employee():
    response = client.post(
        "/employees/",
        json={'department_code':'123', 'name':'Иванов Иван Иванович', 'post':'Director', 'salary':'90000', 'premium':'25000'}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Иванов Иван Иванович"

def test_create_exist_employee():
    response = client.post(
        "/employees/",
        json={'department_code':'123', 'name':'Иванов Иван Иванович', 'post':'Director', 'salary':'90000', 'premium':'25000'}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Employee name is already exist"

def test_read_employee():
    response = client.get("/employees/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]['name'] == 'Иванов Иван Иванович'

def test_get_employee_by_id():
    response = client.get("/employees/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['name'] == 'Иванов Иван Иванович'

def test_employee_not_found():
    response = client.get("/employees/2")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Employee not found"  



def test_create_contract():
    response = client.post(
        "/contracts/",
        json={'Org_name':'Geology', 'date_contract':'2022-10-10'}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["Org_name"] == "Geology"

def test_contract_not_found():
    response = client.get("/contracts/7")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Contract not found"  


def test_create_shipment_for_employee_contract():
    response = client.post(
        "/shipments/1/employee/1",
        json={'type_of_equipment':'centralized', 'comment':'functioning'}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["type_of_equipment"] == "centralized"





def test_create_organization_for_contract():
    response = client.post(
        "/organizations/1/contract",
        json={'country_code':'44','city':'London','address':'London SW1A 1AA','telephone':'+44-20-7930-4832','email':'royalgov@gmail.com','website_address':'royal.gov.uk'}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["city"] == "London"

def test_organization_not_found():
    response = client.get("/organizations/2")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Organization not found"  




def test_shipment_not_found():
    response = client.get("/shipments/2")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Shipment not found"  




def test_get_contract_by_id():
    response = client.get("/contracts/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['Org_name'] == 'Geology'

def test_get_shipment_by_id():
    response = client.get("/shipments/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['type_of_equipment'] == 'centralized'

    
def test_get_organization_by_id():
    response = client.get("/organizations/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['city'] == 'London'





def test_get_employees():
    response = client.get("/employees/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["department_code"] == 123
    assert data[0]["name"] == 'Иванов Иван Иванович'
    assert data[0]["post"] == 'Director'
    assert data[0]["salary"] == 90000
    assert data[0]["premium"] == 25000

def test_get_contracts():
    response = client.get("/contracts/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["Org_name"] == 'Geology'
    assert data[0]["date_contract"] == '2022-10-10'

def test_get_organizations():
    response = client.get("/organizations/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["country_code"] == 44
    assert data[0]["city"] == 'London'
    assert data[0]["address"] == 'London SW1A 1AA'
    assert data[0]["telephone"] == '+44-20-7930-4832'
    assert data[0]["email"] == 'royalgov@gmail.com'
    assert data[0]["website_address"] == 'royal.gov.uk'

def test_get_shipments():
    response = client.get("/shipments/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["type_of_equipment"] == 'centralized'
    assert data[0]["comment"] == 'functioning'