from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    linkedin_url: Optional[AnyUrl]=None
    weight: float
    married: bool = False #here we are providing a default value to married, if user does not provide any value for married, it will be considered as False
    allergies: Optional[List[str]] = None #list of strings, to validate that every value in the list is a string we used [str], None is the default value here, it means if user does not provide any allergies it will be considered as None
    contact_details: Dict[str, str] #dictionary with string keys and string values





def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print('inserted')


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print('updated')

patient_info = {'name': 'Omkar', 'age':22, 'email': 'omkar@gmail.com', 'linkedin_url':'http://linkedin.com', 'weight': 62.5, 'contact_details': {'phone': '4433445635'}}

patient1 = Patient(**patient_info) # ** is used to unpack the dictionary

insert_patient_data(patient1)