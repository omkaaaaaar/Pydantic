### Video 5: Pydantic Crash Course | Data Validation in Python

#### Why Pydatanic we need here?

Overview: pydantic solves 2 major problems

- Type Validation
- Data Validation

#### Pydantic

- **Define a Pydantic model**(class) that represents the **ideal schema** of the data.
  - This includes the expected fields, their types and any validation constraints (e.g. _gt=0_ for positive numbers)
- **Instantiate the model with raw input data** (usually a dict or JSON-like structure)
  - Pydantic will automatically **validate** the date and **coerce** it into the correct Python types (if possible)
  - if the data doesn't meet the model's requirements. pydantic raises a _ValidationError_ ((e.g. {name -> Omkar, age -> 21}) -> this dict is traferred to the class obj (in this process the data ets automatically validated)) -> here we get the validated pydantic model
- **Pass the validated model object** to functions or use it throughout your codebase
  - This ensures that every part of your program works with **clean, type-safe, and logically valid data**
    (the validated pydantic object we recieve here, our function performs the logic when it recieves this obj )

##### 2 versions of Pydantic, Use Pydantic v2 cause it is written in Rust and it is FAST because of it and it is mostly used now

##### Flow

- pydantic_why_1.py
-
-
- pydantic_type_validation.py
- pydantic_data_validation.py
  - pydantic provides built in data type for data validation, ex:- _EmailStr_, _AnyUrl_

##### Field Function

It is used for putting some customs field,
i.e. If your business requires age between 0-60,then these functions come to the help
This can be used for Numerical and Str based data types bpth
Ex; - weight: float = field(gt=0), age: int = Field(gt=0, lt=120)

It is not only used for **Data Validation** but it is also used to _attach_ **Metadata**

To attach _Metadata_(description, title, etc) we need to import and use _Annotated_ from typing module

#### Field Validator
