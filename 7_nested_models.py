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

address1 = Address(**Address_dict) #unpacking the dictionary to create an instance of the Address model | Built a object of the Address model using the dictionary

Patient_dict = {'name': 'Omkar', 'gender': 'Male', 'age': 22, 'address': address1} #here we are creating a dictionary for the Patient model, and we are using the address1 object which is an instance of the Address model

Patient1 = Patient(**Patient_dict) #unpacking the dictionary to create an instance of the Patient model | Built a object of the Patient model using the dictionary

print(Patient1)

#Testing the nested model
print(Patient1.address.city) #accessing the city of the address of the patient
print(Patient1.address.state) #accessing the state of the address of the patient
print(Patient1.address.pin) #accessing the pin of the address of the patient