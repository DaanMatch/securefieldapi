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


