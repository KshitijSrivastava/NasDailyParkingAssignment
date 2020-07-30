
# Car Parking API

## Backend Python Assignment | Nas Daily


The candidate will create three API endpoints which are mentioned below:

1. Park a Car: The Endpoint will be given the car number as input and outputs the slot
where it is parked. If the parking lot is full, the appropriate error message is returned.
2. Unpark the Car: This endpoint takes the slot number from which the car is to be removed
from and frees that slot up to be used by other cars.
3. Get the Car/Slot Information: This endpoint can take either the slot number or car
number and return both the car number and slot number for the input.


# Documentation

# Setup

Make a python virtual environment
run `python manage.py migrate`
run `python manage.py runserver`



# Creates a Parking for a Car

**URL** : `/park/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data example** All fields must be sent.

* car_number: Number of Car (String)

```json
{
    "car_number": "MP10F9999"
}
```

## Success Response

**Code** : `201 Created`

**Content examples**

```json
{
    "slot": 1
}
```

**Error Response**

```json
{
   "error": "Parking is full"
}
```

# Unparks a car in Parking


**URL** : `/unpark/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data example** All fields must be sent.

* slot: slot number of car parking (Integer)

```json
{
    "slot": "2"
}
```

## Success Response

**Code** : `201 Created`

**Content examples**

```json
{
    "message": "Car unparked"
}
```

**Error Response**

```json
{
    "error": "Slot Not Present"
}
```


# Get all info about the car parking

**URL for getting info from slot** : `/getparkinginfo?slot=1`
**URL for getting info from car_number** : `/getparkinginfo?car_number=MP20F6529`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

## Success Response

**Code** : `200 OK`

**Content examples**


```json
{
    "car_number": "MP20F6529"
}
```

**Error Response**

```json
{
    "error": "No Car parked"
}
```
