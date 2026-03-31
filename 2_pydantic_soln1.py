from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
    weight: float

#here we will define the ideal Type Validation Schema which we want




def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print('inserted')


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print('updated')

patient_info = {'name': 'Omkar', 'age':22, 'weight': 62.5}

patient1 = Patient(**patient_info) # ** is used to unpack the dictionary

update_patient_data(patient1)