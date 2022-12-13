"""empty message

Revision ID: first_data
Revises: 40044f9680ad
Create Date: 2022-12-04 00:31:20.291931

"""
from alembic import op
from sqlalchemy import orm
from datetime import datetime

from src.models import Employee, Shipment, Сontract, Organization


# revision identifiers, used by Alembic.
revision = 'first_data'
down_revision = '40044f9680ad'
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    ivanov = Employee(department_code='123', name='Иванов Иван Иванович', post='Director', salary='90000', premium='25000')
    petrov = Employee(department_code='123', name='Петров Сергей Денисович', post='Worker', salary='40000', premium='13500')

    session.add_all([ivanov, petrov])
    session.flush()

    geology = Сontract(Org_name='Geology', date_contract=datetime(2022-10-10))
    lab_Analysis = Сontract(Org_name='Laboratory Analysis Center', date_contract=datetime(2022, 3, 12, 12, 10))
    lidsey = Сontract(Org_name='Lidsey', date_contract=datetime(2022, 2, 12, 10, 10))
    invitlaf = Сontract(Org_name='Invitlaf', date_contract=datetime(2022, 2, 20, 12, 10))

    session.add_all([geology, lab_Analysis, lidsey, invitlaf])
    session.commit()

    centralized = Shipment(type_of_equipment='centralized',comment='functioning',employee_id=ivanov.id, contract_id=lab_Analysis.id)
    decentralized = Shipment(type_of_equipment='decentralized',comment='functioning',employee_id=petrov.id, contract_id=invitlaf.id)

    session.add_all([centralized, decentralized])
    session.commit()

    geology_org = Organization(contract_id=geology.id,country_code='44',city='London',address='London SW1A 1AA',telephone='+44-20-7930-4832',email='royalgov@gmail.com',website_address='royal.gov.uk')
    lab_Analysis_org = Organization(contract_id=lab_Analysis.id,country_code='49',city='Berlin',address='Spandauer Str., 3',telephone='+49-30-99280-0',email='visitlife36@gmail.com',website_address='visitsealife.com')
    lidsey_org = Organization(contract_id=lidsey.id,country_code='1',city='Los Angeles',address='South Hope Street, 333',telephone='1-043-865-681',email='lidsey@gmail.com',website_address='bankofamerica.com')
    invitlaf_org = Organization(contract_id=invitlaf.id,country_code='7',city='Moscow',address='Ленинские горы, д. 1',telephone='+7-495-939-29-51',email='info@rector.msu.ru',website_address='msu.ru ')

    session.add_all([geology_org, lab_Analysis_org, lidsey_org, invitlaf_org])
    session.commit()

def downgrade() -> None:
    pass
