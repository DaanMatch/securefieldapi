# Secure Field API Documentation (Draft)

### Note:

This version of the documentation is neither complete nor robust. It (hopefully) contains enough information to help you understand how to get started using/working on the current version of the API. This documentation and the API itself is subject to change.

<br/>

## Currently Implements:

| URL | Method | Endpoint | Action | Notes |
|--|--|--|--|--|
| /field_data | GET | field_data_many | Retrieve a list of all field_data entries |
| /field_data | POST | field_data_many | Creates a field_data entry |
| /field_data/\<int:id\> | GET | field_data_one | Retrieve details of a field_data entry |
| /field_data/\<int:id\> | PATCH | field_data_one | Updates a field_data |
| /field_data/\<int:id\> | DELETE | field_data_one | Deletes a field_data | Need to create a workaround to prevent malicious deletion
| /member | POST | member_many | Creates an member | Might not need?
| /member/\<int:id\> | GET | member_one | Retrieve details of a member | Allow user to see their own info (except password)
| /member/\<int:id\> | PATCH | member_one | Updates a member | Use this to let members already in the database set a password. Right now this can still update any all member fields.

<br/><br/><br/><br/>

## Need To Implement:

| URL | Method | Endpoint | Action | Notes |
|--|--|--|--|--|


<br/><br/><br/><br/>

### Note:

The following examples hold the same pattern for all the routes defined above. You just need to substitute the correct URL, type, and attributes (type and attributes refer to the keys in the JSON request body). Lists of attributes for each table will be at the end of the documentation.

<br/>

## Example 1 (POST):

| Method | URL | Endpoint | Action
|-|-|-|-
| POST | /field_data | field_data_many | Create a field_data entry

### Request:
```
POST /field_data HTTP/1.0
Content-Type: application/vnd.api+json
Accept: application/vnd.api+json

{
    "data":{
        "type":"field_data",
        "attributes":{
            "ngo_id":152,
            "recorded_by":1234,
            "date":"2000-10-10",
            "address":"Address",
            "latitude":90.5,
            "longitude":456.565,
            "title":"Title",
            "comment":"Comment",
            "media":"Media lnk",
            "media_type":"photo/video/etc",
            "sector_id":645,
            "sdg":"Goal"
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
        "type":"field_data",
        "id":1,
        "attributes":{
            "media_type":"photo/video/etc",
            "sector_id":645,
            "comment":"Comment",
            "address":"Address",
            "media":"Media lnk",
            "title":"Title",
            "recorded_by":1234,
            "ngo_id":152,
            "sdg":"Goal",
            "longitude":"456.5650000000",
            "date":"2000-10-10",
            "latitude":"90.5000000000"
        },
        "links":{
            "self":"/field_data/1"
        }
    },
    "links":{
        "self":"/field_data/1"
    },
    "jsonapi":{
        "version":"1.0"
    }
}
```

<br/><br/><br/><br/>

## Example 2 (GET):

### Note:

This example is an example of getting a list of field_data entries. To get a particular field_data entry, use the url /field_data/\<int:id\> instead of /field_data.

| Method | URL | Endpoint | Action
|-|-|-|-
| GET | /field_data | field_data_many | Retrieves a list of all field_data

#### Request:
```
GET /field_data HTTP/1.1
Accept: application/vnd.api+json
```

#### Response:
```
HTTP/1.0 200 OK
Content-Type: application/vnd.api+json

{
    "data":[
        {
            "type":"field_data",
            "id":1,
            "attributes":{
                "media_type":"photo/video/etc",
                "sector_id":645,
                "comment":"Comment",
                "address":"Address",
                "media":"Media lnk",
                "title":"Title",
                "recorded_by":1234,
                "ngo_id":152,
                "sdg":"Goal",
                "longitude":"456.5650000000",
                "date":"2000-10-10",
                "latitude":"90.5000000000"
            },
            "links":{
                "self":"/field_data/1"
            }
        },
        {
            "type":"field_data",
            "id":2,
            "attributes":{
                "media_type":"photo/video/etc",
                "sector_id":645,
                "comment":"Comment",
                "address":"Address",
                "media":"Media lnk",
                "title":"Title",
                "recorded_by":1234,
                "ngo_id":152,
                "sdg":"Goal",
                "longitude":"456.5650000000",
                "date":"2000-10-10",
                "latitude":"90.5000000000"
            },
            "links":{
                "self":"/field_data/2"
            }
        }
    ],
    "links":{
        "self":"http://localhost:5000/field_data"
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
| PATCH | /field_data/\<int:id\> | field_data_one | Update a field_data entry

### Request:
```
PATCH /field_data/1 HTTP/1.0
Content-Type: application/vnd.api+json
Accept: application/vnd.api+json

{
    "data":{
        "type":"field_data",
        "id":1,
        "attributes":{
            "title":"THIS WAS CHANGED"
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
        "type":"field_data",
        "id":1,
        "attributes":{
            "media_type":"photo/video/etc",
            "sector_id":645,
            "comment":"Comment",
            "address":"Address",
            "media":"Media lnk",
            "title":"THIS WAS CHANGED",
            "recorded_by":1234,
            "ngo_id":152,
            "sdg":"Goal",
            "longitude":"456.5650000000",
            "date":"2000-10-10",
            "latitude":"90.5000000000"
        },
        "links":{
            "self":"/field_data/1"
        }
    },
    "links":{
        "self":"/field_data/1"
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
| DELETE | /field_data/\<int:id\> | field_data_one | Delete an field_data entry

### Request:
```
DELETE /field_data/1 HTTP/1.1
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

<br/>

### Note: Member has additional mobile_device_id and password fields.

<img width="1283" alt="Screen Shot 2021-10-07 at 15 47 09" src="https://user-images.githubusercontent.com/70539478/136472836-0da6e844-ce13-4067-84ee-716fc90b3e09.png">



