#Problem 1: Type Validation
#Problem 2: Value Validation

def insert_patient_data(name, age):

    print(name)
    print(age)
    print('inserted into database')

insert_patient_data('Omkar', 'Twenty') #here we were expecting that the Age will be in int, but the junior dev made it both into a string 
#this is a MAJOR FAILUR, cause it gets stored into the DB, soo we need to perform type validation and need to make sure that the data follows a strict schema. i.e -> name = str, age = int. this is ingenral python problem because it is a dynamic lang
#To solce this : Type Hinting(that name: str, age:int) and Pydantic
#type hinting is just a hint, it does not show errors if the type is not correct
#we can strictly enfore the type using pydantic

def insert_patient_data_soln1(name: str, age: int):

    if type(name) == str and type(age)== int:
        if age < 0:  #here we are making sure that the age is not negative, this is value validation, we are validating the value of age
            raise ValueError('Age cannot be negative')
        else:
            print(name)
            print(age)
            print('inserted into db')
    else:
        raise TypeError('Incorrect data type')    

insert_patient_data_soln1('Omkar', 'Twenty One') #ts will raise a type error    
#this "JUGAAD" we performed above is not wrong, it is right but it is not scalable!

def update_patient_data(name: str, age: int):

    if type(name) == str and type(age)== int:
        if age < 0:  #here to we have to perform the same loop for value validation, this is code repetition, and if we have to perform this for 100s of fields, then it becomes a nightmare to maintain the code, and it is not scalable
            raise ValueError('Age cannot be negative')
        else:
            print(name)
            print(age)
            print('inserted into db')
    else:
        raise TypeError('Incorrect data type')
    

#Pydantic solves this problem, so that we dont face any Type Validation and Value Validation problem