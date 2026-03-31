from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Optional, Dict, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Patient Name", description="The full name of the patient.")]
    email: EmailStr
    linkedIn: Optional[AnyUrl] = None
    age: int = Field(gt=0, ls=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description="Is patient married or not.")]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]


    #for Validation (email validation)
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com -> the below code will extract the domain name from the email address it will split the email address by '@' and take the last part which is the domain name
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError(f"Not a valid domain")
        
        return value



    #for Transformation
    @field_validator('name')
    @classmethod
    def transform_name(cls, name):
        return name.upper() #this will transform the name to uppercase before storing it in the database, this is called transformation, we are transforming the data before storing it in the database


    # @field_validator('age', mode='before')
    # @classmethod
    # def validate_age(cls, value):
    #     if 0<value<100:
    #         return value
    #     else:
    #         raise ValueError('Age must be between 0 and 100')
    # #it will raise a value error here, because we used before mode, so the value we will recieve here will be before the type cohercion, so it will be a string, and we are trying to compare it with an int, so it will raise a value error, if we want to avoid this error we can use the after mode, so that we will recieve the value after the type cohercion, so it will be an int and we can compare it with another int    



def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedIn)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print('inserted')


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print('updated')

patient_info = {'name': 'Omkar', 'age':22, 'email': 'omkar@hdfc.com', 'linkedin_url':'http://linkedin.com', 'weight': 62.5, 'contact_details': {'phone': '4433445635'}}

patient1 = Patient(**patient_info) # ** is used to unpack the dictionary

insert_patient_data(patient1)