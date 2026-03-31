# Video 5: Pydantic Crash Course | Data Validation in Python

## Why Pydatanic we need here?

Overview: pydantic solves 2 major problems

- Type Validation
- Data Validation

## Pydantic

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

- 1_pydantic_why_1.py
- 2_pydantic_soln1.py
- 3_type_validation.py
- 4_data_validation.py
- 5_model_validator.py
- 6_computed_fields.py
- 7_nested_models.py
- 8_serialization.py

pydantic provides built in data type for data validation, ex:- _EmailStr_, _AnyUrl_

### Field Function

It is used for putting some customs field,
i.e. If your business requires age between 0-60,then these functions come to the help
This can be used for Numerical and Str based data types bpth
Ex; - weight: float = field(gt=0), age: int = Field(gt=0, lt=120)

It is not only used for **Data Validation** but it is also used to _attach_ **Metadata**

To attach _Metadata_(description, title, etc) we need to import and use _Annotated_ from typing module

### Field Validator

PS: The hospital has tie-ups with banks (icici, hdfc, etc). The employees of these bank can get treatment in low fees.
Soln: We can check it by checking the e-mail of the user; i.e - hdfc users will have @hdfc.com in the email!
Now we will deal with custom buisness specific data validation techniques - _Field Validator_ it helps us to perform pn the fields custom validations and also can do transformation(name should be capital, etc)

### Field Validator, operates in 2 modes

- Before Mode
- After Mode

Default mode used here is _after_
When using the mode after, the value we will recieve will be after the _type cohercion_
But if we did mode 'Befor' we will recieve the value before of the _type cohercion_

### Model Validator

Ps:- We need to add an _'Emergency Contact'_ for patients _> age60_, we not save the patient info if the Emergency Contact is not provided for our criteria
Soln: For this we will use, ModelValidator. Here we will need to work with 2 Fields _age, contact_
We can't use Field Validtor here because the field validator works on only a single Field

### Computed Fields

This field is a field whose value is not provided by the user but it is computed based on the other fields
ex:- _Weight and Height_ is provided by the user, so based on this we will Dynamically create _BMI_
Since the BMI is calculated on the go with the help of the other fields that why it will be called as a 'Computed Fields'

### Nested Models

To use a model in another model as a **field** is called as a Nested Modelss

Ex: The patient addr wll look like:- Income Tax Colony, Indira Nagar, Jogeshwari-East, Mumbai - 400060
But now we need to only extract the _Nagar_ or _Pincode_, this process will be very hectic to extract a particulat str, etc Because addr is a complex data which is built up of multiple more data

So, in this situation, we should build a Address model and use it in Patient Model as a field | **Nested Model**

Benifits of Nested Models

- Better organization of related data(e.g., vitals, address, insurance)
- Reusability: Use Vitals in multiple models (e.g. Patient, Medical Records)
- Readability: Easier for developers and API consumers to understand
- Validation: Nested models are validated successfully-no extra work needed

### Serializtion

How to export pydantic model objects as Python Dictionary or JSON
Pydatic provides built-in methods to export existing pydantic models as Python Dict

## Source:- https://youtu.be/lRArylZCeOs?si=pM7RujnaIFrn7uIO
