from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address #nested model

Address_dict = {'city': 'Pune', 'state': 'Maharashtra', 'pin': '411001'}

address1 = Address(**Address_dict)

Patient_dict = {'name': 'Omkar', 'gender': 'Male', 'age': 22, 'address': address1} 

Patient1 = Patient(**Patient_dict)

#converting in py dict

temp = Patient1.model_dump() #this will convert the pydantic model object into a python dictionary

print(temp)
print(type(temp))


#converting in JSON

temp1 = Patient1.model_dump_json() #this will convert the pydantic model object into a JSON string

print(temp1)
print(type(temp1))
#Python will recieve this as a str, but when you'll export it'll be in JSON Format


#include paramester - This parameter only provides the particular fields

temp2 = Patient1.model_dump(include=['name', 'age'])
print(temp2)

#exclude parameter - This parameter will exclude the particular fields

temp3 = Patient1.model_dump(exclude=['name', 'age'])
print(temp3)

temp4 = Patient1.model_dump(exclude={'address':['state']})
print(temp4)

# exclude_unset - This parameter will exclude the fields which are not set by the user, it will only include the fields which are set by the user, even if there are default values for the fields, it will exclude those fields if the user has not provided any value for those fields