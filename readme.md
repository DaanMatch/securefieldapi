<<<<<<< HEAD
## Notes
- Working on user verification (login feature)
- Fetched from Mitchell's working branch `JSON` to keep the model, foldering consistent


## To - Dos
- [X] Add `mobile_device_id`, `password` column to `member` model
- [X] Implement a login route to register a new user
- [ ] Choose a hashing algorithm for the password (create a documentation on this)
- Login exception cases
    - [ ] Unique `mobile_device_id` : currently the member gets added regardless of `mobile_device_id`


## To - Discuss
- Which to use as a main feature for verification? `password` or `mobile_device_id`?
    - Use both?: `mobile_device_id` and `password` match -> existing user
- Should separate signup (new user), login (returning user) route?
- JWT token as a header
- `member` -- `field`: column `recorded_by` refers to the PK in `member` table but the data types are different
- Difference between `people` and `member`


## Running server
Create and start virtual environment
```
python -m venv .venv
source .venv/bin/activate or source .venv/scripts/activate

Install modules:
python -m pip install -r requirements.txt

Start the app:
python application.py
```

## Running API locally with postman runner

### Sends a GET request to retrieve all the field_data entries

``` GET http://localhost:5000/field_data```

<img width="900" alt="Screen Shot 2021-10-10 at 7 05 19 PM" src="https://user-images.githubusercontent.com/46921003/136723270-979fd45e-6b8c-4b9e-a007-8ff28c29bb88.png">


### Sends a POST request to register a user

``` POST http://127.0.0.1:5000/login```

**Request Body**

```JSON
{
    "data":{
        "type":"member",
        "attributes":{
            "name": "test",
            "email": "222@berkeley.edu",
            "mobile": "9092423124",
            "mobile_device_id": "234 2342 222",
            "password":"pwwww"
        }
    }
}
```

<img width="700" alt="Screen Shot 2021-10-11 at 12 13 01 PM" src="https://user-images.githubusercontent.com/46921003/136844153-0357fe03-276b-4521-bc4f-b92c5b405469.png">

=======
## Notes: 
* Files db.py and api.py are used to prevent circular imports.
* Currently implements API for `field_data` and `member` tables of the data model. 

## TODO:
* Clean up unnecessary code once core functionality inplace.
* Write the Documentation

## Run the API locally:
Create and start virtual environment<br/>
`python -m venv .venv`<br/>
`source .venv/bin/activate` or `source .venv/scripts/activate`

Install modules:<br/>
`python -m pip install -r requirements.txt`

Start the app:<br/>
`python application.py`

## API Interaction With cURL:
So far I've just been using curl to act as the client side. 
Below are a few example requests.

### Creates post request and adds a new field_data entry:<br/>
```
curl -i -X POST -H 'Content-Type: application/vnd.api+json' -d '{"data":{"type":"field_data", "attributes":{"ngo_id":152, "recorded_by":1234, "date":"2000-10-10", "address":"Address", "latitude":90.5, "longitude":456.565, "title":"Title", "comment":"Comment", "media":"Media lnk", "media_type":"photo/video/etc", "sector_id":645, "sdg": "Goal"}}}' http://localhost:5000/field_data
```


### Sends a GET request to retrieve all the field_data entries<br/>
```
curl -i -X GET http://localhost:5000/field_data
```
Alternatively, you can go directly to the url as indicated in the endpoints section at the bottom of application.py.
Go directly to http://localhost:5000/field_data and you should see the same JSON as when you used the command above.


### Sends a GET request to retrieve one field_data entry<br/>
```
curl -i -X GET http://localhost:5000/field_data/1
```


### Sends a PATCH request to update a field_data entry<br/>
```
curl -i -X PATCH -H 'Content-Type: application/vnd.api+json' -d '{"data":{"type":"field_data", "id":1, "attributes":{"title":"THIS WAS CHANGED"}}}' http://localhost:5000/field_data/1
```


>>>>>>> json
