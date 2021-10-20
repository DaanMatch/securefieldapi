# __Secure Field API Documentation (Draft)__

### Note:

This version of the documentation is neither complete nor robust. It (hopefully) contains enough information to help you understand how to get started using/working on the current version of the API. Both the documentation and the API itself are subject to change.

<br/>

## __Currently Implements:__

| URL | Method | Endpoint | Action | Notes |
| -- | -- | -- | -- | -- |
| /member/\<int:id\>/field_data | GET | field_data_many | Retrieve a list of all field_data entries associated with a member |
| /member/\<int:id\>/field_data | POST | field_data_many | Creates a field_data entry associated with a member |
| /field_data/\<int:id\> | GET | field_data_one | Retrieve details of a field_data entry |
| /field_data/\<int:id\> | PATCH | field_data_one | Updates a field_data entry |
| /member/\<int:id\> | GET | member_one | Retrieve details of a member | (except password)
| /member/\<int:id\> | PATCH | member_one | Updates a member's password | Use this to let members already in the database set a password. Nothing else can be updated.

<br/><br/><br/><br/>

## __Need To Implement:__

| URL | Method | Endpoint | Action | Notes |
| -- | -- | -- | -- | -- |
| /field_data/\<int:id\> | DELETE | field_data_one | Deletes a field_data entry | Need to create a workaround to prevent malicious deletion

<br/><br/><br/><br/>

# __Methods:__

## __member (GET):__

| URL | Method | Endpoint | Action | Notes |
|--|--|--|--|--|
| /member/\<int:id\> | GET | member_one | Retrieve details of a member | Allow user to see their own info (except password)

### Request:
```
GET /member/1 HTTP/1.0
Accept: application/vnd.api+json
```

### Response:
```
HTTP/1.0 200 OK
Content-Type: application/vnd.api+json

{
    "data":{
        "type":"member",
        "id":1,
        "attributes":{
            "mobile":"999999999",
            "name":"A Name",
            "mobile_device_id":"9596 4569 9455 5",
            "email":"email@email.com"
        },
        "links":{
            "self":"/member/1"
        }
    },
    "links":{
        "self":"/member/1"
    },
    "jsonapi":{
        "version":"1.0"
    }
}
```

<br/><br/><br/><br/>

## __member (PATCH):__

| URL | Method | Endpoint | Action | Notes |
|--|--|--|--|--|
| /member/\<int:id\> | PATCH | member_one | Updates a member's password | Use this to let members already in the database set a password. Nothing else can be updated.

### Request:
```
PATCH /member/1 HTTP/1.0
Content-Type: application/vnd.api+json
Accept: application/vnd.api+json

{
    "data":{
        "type":"member",
        "id":1,
        "attributes":{
            "password":"new_password"
        }
    }
}
```

### Response:
Note: the password is not returned.
```
HTTP/1.0 200 OK
Content-Type: application/vnd.api+json

{
    "data":{
        "type":"member",
        "attributes":{
            "name":"A Name",
            "email":"email@email.com",
            "mobile":"999999999",
            "mobile_device_id":"9596 4569 9455 5"
        },
        "id":1,
        "links":{
            "self":"/member/1"
        }
    },
    "links":{
        "self":"/member/1"
    },
    "jsonapi":{
        "version":"1.0"
    }
}
```



<br/><br/><br/><br/>





## __field_data (POST):__

| Method | URL | Endpoint | Action
|-|-|-|-
| POST | /member/\<int:id\>/field_data | field_data_many | Create a field_data entry associated with a member. The field_data.recorded_by field is automatically filled.

### Request:
```
POST /member/3/field_data HTTP/1.0
Content-Type: application/vnd.api+json
Accept: application/vnd.api+json

{
    "data":{
        "type":"field_data",
        "attributes":{
            "ngo_id":1,
            "date":"2000-10-10",
            "address":"NewAddress",
            "latitude":90.5,
            "longitude":456.565,
            "title":"NewTitle",
            "comment":"NewComment",
            "media":"New Media lnk",
            "media_type":"new photo/video/etc",
            "sector_id":645,
            "sdg":"NewGoal"
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
        "attributes":{
            "sector_id":645,
            "longitude":"456.5650000000",
            "comment":"NewComment",
            "latitude":"90.5000000000",
            "media":"New Media lnk",
            "date":"2000-10-10",
            "ngo_id":1,
            "address":"NewAddress",
            "title":"NewTitle",
            "sdg":"NewGoal",
            "recorded_by":3,
            "media_type":"new photo/video/etc"
        },
        "id":6,
        "links":{
            "self":"/field_data/6"
        }
    },
    "links":{
        "self":"/field_data/6"
    },
    "jsonapi":{
        "version":"1.0"
    }
}
```

<br/><br/><br/><br/>

## __field_data (GET):__

### Note:

This example is an example of getting a list of field_data entries associated with a user. To get a particular field_data entry, use the url /field_data/\<int:id\> instead of /field_data.

| Method | URL | Endpoint | Action
|-|-|-|-
| GET | /member/\<int:id\>/field_data | field_data_many | Retrieves a list of all field_data for a particular member

#### Request:
```
GET /member/1/field_data HTTP/1.0
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
            "attributes":{
                "sdg":"Goal",
                "comment":"Comment",
                "latitude":"90.5000000000",
                "title":"Title",
                "ngo_id":1,
                "recorded_by":1,
                "media_type":"photo/video/etc",
                "longitude":"456.5650000000",
                "date":"2000-10-10",
                "sector_id":645,
                "address":"Address",
                "media":"Media lnk"
            },
            "id":1,
            "links":{
                "self":"/field_data/1"
            }
        },
        {
            "type":"field_data",
            "attributes":{
                "sdg":"Goal222",
                "comment":"Comment22222",
                "latitude":"290.5000000000",
                "title":"Title222222",
                "ngo_id":1,
                "recorded_by":1,
                "media_type":"photo/video/etc222",
                "longitude":"2456.5650000000",
                "date":"2000-10-10",
                "sector_id":64522,
                "address":"Address22222",
                "media":"Media lnk222"
            },
            "id":5,
            "links":{
                "self":"/field_data/5"
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

## __field_data (PATCH):__

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

## __field_data (DELETE):__

| Method | URL | Endpoint | Action
|-|-|-|-
| DELETE | /field_data/\<int:id\> | field_data_one | Delete an field_data entry

### Request:
```
DELETE /field_data/1 HTTP/1.0
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

### __Note: Member has additional mobile_device_id and password fields.__

<br/>

<img width="1283" alt="Screen Shot 2021-10-07 at 15 47 09" src="https://user-images.githubusercontent.com/70539478/136472836-0da6e844-ce13-4067-84ee-716fc90b3e09.png">



