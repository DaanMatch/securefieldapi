## Notes: 
* Files db.py and api.py are used to prevent circular imports.
* Currently implements API for `activity`, `daanmatch_ngo`, `operation`, `registration_office`, and `registration_number` tables of the data model. 
* For the `registration_number` table, field names starting with a number (i.e. `35AC_regdate`) are preceded with "rn_" (i.e. `rn_35AC_regdate`) because python variable names cannot start with a number.

## TODO:
* Create SDG class (for sdg/sdgs in `operation` and `activity` tables)
* Determine Field Constraints (required fields?, string/text length in db?)
* Implement API For Tables: `city`, `district`, `exec_staff`, `finance`, `membership`, `operational_issue`, `partnership`, `state`
* Implement Relationships Between: `daanmatch_ngo---membership`, `daanmatch_ngo--<partnership`, `daanmatch_ngo---exec_staff`, `operation---operational_issue`, `operation---state`, `operation---city`, `operation---district`
* Write the Documentation

## Run the API locally:
Create and start virtual environment<br/>
`python -m venv .venv`<br/>
`source .venv/bin/activate` or `source .venv/scripts/activate`

Install modules:<br/>
`pip install flask-rest-jsonapi flask-sqlalchemy marshmallow_enum`

Start the app:<br/>
`python application.py`

## API Interaction With cURL:
So far I've just been using curl to act as the client side. 
Below are a few example requests.

Creates post request and adds a new registration_office:<br/>
`curl -i -X POST -H 'Content-Type: application/vnd.api+json' -d '{"data":{"type":"registration_office", "attributes":{"ngo_id":"ngo1", "registered_with":"Registration Office 1", "date":"2000-10-10", "address":"Address 1", "latitude":123.456, "longitude":654.321}}}' http://localhost:5000/registration_offices`

Creates post request and adds a new registration_number:<br/>
`curl -i -X POST -H 'Content-Type: application/vnd.api+json' -d '{"data":{"type":"registration_number", "attributes":{"ngo_id":"ngo1", "pan_no":"pan1", "pan_regdate":"2000-10-10", "fcra_no":"fcra1", "fcra_regdate":"2000-10-10", "rn_12A_no":"12A1", "rn_12A_regdate":"2000-10-10", "rn_80G_no":"80G", "rn_80G_regdate":"2000-10-10", "rn_35AC_no":"35AC", "rn_35AC_regdate":"2000-10-10"}}}' http://localhost:5000/registration_numbers`

Sends a GET request to retrieve all the registration_offices<br/>
`curl -i GET http://localhost:5000/registration_offices`

Alternatively, you can go directly to the url as indicated in the endpoints section at the bottom of application.py.
Go directly to http://localhost:5000/registration_offices and you should see the same JSON as when you used the command above.
After doing the above two post requests, you should be able to see the relationship at http://127.0.0.1:5000/registration_number/1/relationships/registration_office.



