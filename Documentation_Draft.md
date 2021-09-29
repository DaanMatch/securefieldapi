# Secure Field API Documentation (Draft)

### Note:

This version of the documentation is neither complete nor robust. As of right now, the documentation does not contain information regarding relationships between tables (relationship routes might not be necessary for the final API?). It (hopefully) contains enough information to help you understand how to get started using/working on the current version of the API. This documentation and the API itself is subject to change.

<br/>

## Currently Implements:

| URL                             | Method | Endpoint                 | Action                                      |
|---------------------------------|--------|--------------------------|---------------------------------------------|
| /activities                     | GET    | activity_many            | Retrieve a list of all activities           |
| /activities                     | POST   | activity_many            | Creates an activity                         |
| /activity/\<int:id\>            | GET    | activity_one             | Retrieve details of an activity             |
| /activity/\<int:id\>            | PATCH  | activity_one             | Updates an activity                         |
| /activity/\<int:id\>            | DELETE | activity_one             | Deletes an activity                         |
| /operations                     | GET    | operation_many           | Retrieve a list of all operations           |
| /operations                     | POST   | operation_many           | Creates an operation                        |
| /operation/\<int:id\>           | GET    | daanmatch_ngo_one        | Retrieve details of an operation            |
| /operation/\<int:id\>           | PATCH  | daanmatch_ngo_one        | Updates an operation                        |
| /operation/\<int:id\>           | DELETE | daanmatch_ngo_one        | Deletes an operation                        |

<br/><br/><br/><br/>

## Need To Implement:

| URL                           | Method   | Endpoint               | Action                                    |
|-------------------------------|----------|------------------------|-------------------------------------------|

| /memberships                  | GET      | membership_many        | Retrieve a list of all memberships        |   
| /memberships                  | POST     | membership_many        | Creates an membership                     |   
| /membership/\<int:id\>        | GET      | membership_one         | Retrieve details of an membership         |   
| /membership/\<int:id\>        | PATCH    | membership_one         | Updates an membership                     |   
| /membership/\<int:id\>        | DELETE   | membership_one         | Deletes an membership                     |  


<br/><br/><br/><br/>

### Note:

The following examples hold the same pattern for all the routes defined above. You just need to substitute the correct URL, type, and attributes (type and attributes refer to the keys in the JSON request body). Lists of attributes for each table will be at the end of the documentation.

<br/>

## Example 1 (POST):

| Method | URL | Endpoint | Action
|-|-|-|-
| POST | /activities | activity_many | Create an activity

### Request:
```
POST /activities HTTP/1.0
Content-Type: application/vnd.api+json
Accept: application/vnd.api+json

{
    "data":{
        "type":"activity",
        "attributes":{
            "ngo_id":"Unique id",
            "name":"Activity Name",
            "description":"Descriptive description",
            "date":"2021:09:27",
            "issue":"A big issue",
            "sdg":null,
            "beneficiaries":"Some beneficiaries",
            "address":"An address",
            "state":"Some state",
            "district":"Some district",
            "city":"Some city",
            "gram_panchayat":"village-governing institute in Indian village",
            "latitude":123.123,
            "longitude":456.456
        }
    }
}
```

### Response:
```
HTTP/1.0 201 CREATED
Content-Type: application/vnd.api+json

{
    "data":{
        "type":"activity",
        "attributes":{
            "ngo_id":"Unique id",
            "name":"Activity Name",
            "description":"Descriptive description",
            "date":"2021:09:27",
            "issue":"A big issue",
            "sdg":null,
            "beneficiaries":"Some beneficiaries",
            "address":"An address",
            "state":"Some state",
            "district":"Some district",
            "city":"Some city",
            "gram_panchayat":"village-governing institute in Indian village",
            "latitude":123.123,
            "longitude":456.456
        },
        "id":1,
        "links":{
            "self":"/activity/1"
        }
    },
    "links":{
        "self":"/activity/1"
    },
    "jsonapi":{
        "version":"1.0"
    }
}
```

<br/><br/><br/><br/>

## Example 2 (GET):

### Note:

This example is an example of getting a list of activities. To get a particular activity, use the url /activity/\<int:id\> instead of /activities.

| Method | URL | Endpoint | Action
|-|-|-|-
| GET | /activities | activity_many | Retrieves a list of all activities

#### Request:
```
GET /activities HTTP/1.1
Accept: application/vnd.api+json
```

#### Response:
```
HTTP/1.0 200 OK
Content-Type: application/vnd.api+json

{
    "data":[
        {
            "type":"activity",
            "attributes":{
                "ngo_id":"Unique id",
                "name":"Activity Name",
                "description":"Descriptive description",
                "date":"2021:09:27",
                "issue":"A big issue",
                "sdg":null,
                "beneficiaries":"Some beneficiaries",
                "address":"An address",
                "state":"Some state",
                "district":"Some district",
                "city":"Some city",
                "gram_panchayat":"village-governing institute in Indian village",
                "latitude":123.123,
                "longitude":456.456
            },
            "id":1,
            "links":{
                "self":"/activity/1"
            }
        },
        {
            "type":"activity",
            "attributes":{
                "ngo_id":"Second Unique id",
                "name":"Second Activity Name",
                "description":"Second Descriptive description",
                "date":"2021:09:27",
                "issue":"Second  big issue",
                "sdg":null,
                "beneficiaries":"Second beneficiaries",
                "address":"Second address",
                "state":"Second state",
                "district":"Second district",
                "city":"Second city",
                "gram_panchayat":"Second village-governing institute",
                "latitude":123.123,
                "longitude":456.456
            },
            "id":2,
            "links":{
                "self":"/activity/2"
            }
        }
    ],
    "links":{
        "self":"http://localhost:5000/activities"
    },
    "meta":{
        "count":2
    },
    "jsonapi":{
        "version":"1.0"
    }
}
```
<br/><br/><br/><br/>

## Example 3 (PATCH):

| Method | URL | Endpoint | Action
|-|-|-|-
| PATCH | /activity/\<int:id\> | activity_one | Update an activity

### Request:
```
PATCH /activity/1 HTTP/1.0
Content-Type: application/vnd.api+json
Accept: application/vnd.api+json

{
    "data":{
        "type":"activity",
        "id":1,
        "attributes":{
            "ngo_id":"Changed id",
            "name":"Changed Activity Name",
            "description":"Changed Descriptive description",
            "date":"2021:09:27",
            "issue":"Changed big issue",
            "sdg":null,
            "beneficiaries":"Changed beneficiaries",
            "address":"Changed address",
            "state":"Changed state",
            "district":"Changed district",
            "city":"Changed city",
            "gram_panchayat":"Changed village-governing institute",
            "latitude":123.123,
            "longitude":456.456
        }
    }
}
```

### Response:
```
HTTP/1.0 200 OK
Content-Type: application/vnd.api+json

{
    "data":{
        "type":"activity",
        "attributes":{
            "ngo_id":"Changed id",
            "name":"Changed Activity Name",
            "description":"Changed Descriptive description",
            "date":"2021:09:27",
            "issue":"Changed big issue",
            "sdg":null,
            "beneficiaries":"Changed beneficiaries",
            "address":"Changed address",
            "state":"Changed state",
            "district":"Changed district",
            "city":"Changed city",
            "gram_panchayat":"Changed village-governing institute",
            "latitude":123.123,
            "longitude":456.456
        },
        "id":1,
        "links":{
            "self":"/activity/1"
        }
    },
    "links":{
        "self":"/activity/1"
    },
    "jsonapi":{
        "version":"1.0"
    }
}
```

<br/><br/><br/><br/>

## Example 4 (DELETE):

| Method | URL | Endpoint | Action
|-|-|-|-
| DELETE | /activity/\<int:id\> | activity_one | Delete an activity

### Request:
```
DELETE /activity/1 HTTP/1.1
Accept: application/vnd.api+json
```

### Response:
```
HTTP/1.0 200 OK
Content-Type: application/vnd.api+json

{
    "meta":{
        "message":"Object successfully deleted"
    },
    "jsonapi":{
        "version":"1.0"
    }
}
```

<br/><br/><br/><br/>

## Attribute Tables:

Reference the following table for attributes of the registration_number table, otherwise reference the datatypes in the data model. 

<br/>


<img width="897" alt="Screen Shot 2021-09-12 at 15 30 12" src="https://user-images.githubusercontent.com/70539478/133004826-5c9d8312-e067-4418-97f4-5dc8986990a6.png">
