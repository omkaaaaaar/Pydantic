from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
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


    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Emergency contact is required for patients above 60 years old')
        return model



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

patient_info = {'name': 'Omkar', 'age':65, 'email': 'omkar@hdfc.com', 'linkedin_url':'http://linkedin.com', 'weight': 62.5,'allergies':{'pollen', 'dust'} ,'contact_details': {'phone': '4433445635', 'emergency': '9876543210'}}

patient1 = Patient(**patient_info) # ** is used to unpack the dictionary

insert_patient_data(patient1)