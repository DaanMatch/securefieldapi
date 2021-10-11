## Notes
- Working on primarily on user verification (login feature)
- Currently implements API for `member`, `people`, `field_data`, of the data model.
- Merged from Mitchell's working branch `JSON`


## To - Dos
1. Added a `mobile_device_id`, `password` column
2. Coming up with a hashing algorithm for the password (create a documentation on this)
3. Establish relationship within following tables
    - `member` --- `people`
    - `member` --- `field_data`


## To - Discuss
- `member` -- `field`: column `recorded_by` refers to the PK in `member` table but the data types are different
- Difference between `people` and `member`


## Running server
Create and start virtual environment
python -m venv .venv
source .venv/bin/activate or source .venv/scripts/activate

Install modules:
python -m pip install -r requirements.txt

Start the app:
python application.py

## Running API locally with postman

### Sends a GET request to retrieve all the field_data entries

``` GET http://localhost:5000/field_data```

<img width="900" alt="Screen Shot 2021-10-10 at 7 05 19 PM" src="https://user-images.githubusercontent.com/46921003/136723270-979fd45e-6b8c-4b9e-a007-8ff28c29bb88.png">
