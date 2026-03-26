from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='The name should not exceed 50 characters', examples=['Omkar', 'Karan'])] #here we are using Annotated to provide additional metadata for the name field, max_length is used to validate that the name should not exceed 50 characters, title and description are used to provide additional information about the field
    age: int = Field(gt=0, lt=120) #here we are using field function to validate that age should be greater than 0 and less than 120
    email: EmailStr
    linkedin_url: Optional[AnyUrl]=None
    weight: Annotated[float, Field(gt=0, strict=True)] #here we are using Annotated to provide additional metadata for the weight field, gt is used to validate that weight should be greater than 0, strict tells the pydantic to not do the type coercion(type conversion)
    married: bool = False #here we are providing a default value to married, if user does not provide any value for married, it will be considered as False
    allergies: Annotated[Optional[List[str]], Field(default=None, description='A list of allergies that the patient has')] = None #here we are using Annotated to provide additional metadata for the allergies field, default is set to None, which means that if user does not provide any value for allergies, it will be considered as None, description is used to provide additional information about the field
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