from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict



class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float #kg
    height: float #mtr


    @computed_field #decorator 
    @property #decorator
    def calculate_bmi(self) -> float:
        bmi = round(self.weight / (self.height**2),2) #BMI = weight(kg) / height(m)^2
        return bmi





def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.height)
    print('inserted')


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print('BMI', patient.calculate_bmi)
    print('updated')

patient_info = {'name': 'Omkar', 'age':65, 'email': 'omkar@hdfc.com', 'weight': 63, 'height':1.66}

patient1 = Patient(**patient_info) # ** is used to unpack the dictionary

update_patient_data(patient1)