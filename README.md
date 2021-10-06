
## Notes
- Currently implements API for `member`, `people`,  `field_data`, of the data model.
- User verification with mobile device id

## To - Dos
1. Adding a `mobile_id` column
2. Coming up with a hashing algorithm for the password (create a documentation on this)
3. Establish relationship within following tables
    - `member` --- `people`
    - `member` --- `field_data`


## To Discuss
- `member` -- `field`: column `recorded_by` refers to the PK in `member` table but the data types are different
- Difference between `people` and `member`


## Running the API Locally

```
Create and start virtual environment
python -m venv .venv
source .venv/bin/activate or source .venv/scripts/activate

Install modules:
python -m pip install -r requirements.txt

Start the app:
python application.py
```

## API Interactino with cURL

