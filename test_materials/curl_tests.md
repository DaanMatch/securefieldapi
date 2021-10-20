
## Post a member __FOR TESTING PURPOSES ONLY NOT FOR PRODUCTION__
### Request
```
curl -i -X POST -H 'Content-Type: application/vnd.api+json' -d '{"data":{"type":"member", "attributes":{}}}' http://localhost:5000/member
```

### Response
```
HTTP/1.0 201 CREATED
Location: http://localhost:5000/member/1 
Content-Type: application/vnd.api+json   
Content-Length: 288
Server: Werkzeug/2.0.1 Python/3.9.6      
Date: Fri, 08 Oct 2021 02:18:45 GMT      

{"data": {"type": "member", "attributes": {"data_manager": null, "mobile": null, "email": null, "name": null}, "relationships": {"field_data": {"links": {"self": "/member/3/field_data", "related": "/field_data/3"}}}, "id": 3, "links": {"self": "/member/3"}}, "links": {"self": "/member/3"}, "jsonapi": {"version": "1.0"}}
```

<br/>
<br/>
<br/>


# __field_data Tests__

## Post a field_data associated with a member
### Request
```
curl -i -X POST -H 'Content-Type: application/vnd.api+json' -d '{"data":{"type":"field_data", "attributes":{"ngo_id":1, "date":"2000-10-10", "address":"NewAddress", "latitude":90.5, "longitude":456.565, "title":"NewTitle", "comment":"NewComment", "media":"New Media lnk", "media_type":"new photo/video/etc", "sector_id":645, "sdg": "NewGoal"}}}' http://localhost:5000/member/3/field_data
```

### Response
```
HTTP/1.0 201 CREATED
Location: http://localhost:5000/field_data/6
Content-Type: application/vnd.api+json
Content-Length: 443
Server: Werkzeug/2.0.1 Python/3.9.6
Date: Wed, 20 Oct 2021 03:00:59 GMT

{"data": {"type": "field_data", "attributes": {"sector_id": 645, "longitude": "456.5650000000", "comment": "NewComment", "latitude": "90.5000000000", "media": "New Media lnk", "date": "2000-10-10", "ngo_id": 1, "address": "NewAddress", "title": "NewTitle", "sdg": "NewGoal", "recorded_by": 3, "media_type": "new photo/video/etc"}, "id": 6, "links": {"self": "/field_data/6"}}, "links": {"self": "/field_data/6"}, "jsonapi": {"version": "1.0"}}
```

## Get all field data associated with a member.id
### Request
```
curl -i -X GET http://localhost:5000/member/1/field_data
```

### Response
```
HTTP/1.0 200 OK
Content-Type: application/vnd.api+json
Content-Length: 843
Server: Werkzeug/2.0.1 Python/3.9.6
Date: Wed, 20 Oct 2021 02:26:07 GMT

{"data": [{"type": "field_data", 
"attributes": {"sdg": "Goal", "comment": "Comment", "latitude": "90.5000000000", "title": "Title", "ngo_id": 1, "recorded_by": 1, "media_type": "photo/video/etc", "longitude": "456.5650000000", "date": "2000-10-10", "sector_id": 645, "address": "Address", "media": "Media lnk"}, "id": 1, "links": {"self": "/field_data/1"}}, {"type": "field_data", "attributes": {"sdg": "Goal222", "comment": "Comment22222", "latitude": "290.5000000000", "title": "Title222222", "ngo_id": 1, "recorded_by": 1, "media_type": "photo/video/etc222", "longitude": "2456.5650000000", "date": "2000-10-10", "sector_id": 64522, "address": "Address22222", "media": "Media lnk222"}, "id": 5, "links": {"self": "/field_data/5"}}], "links": {"self": "http://localhost:5000/field_data"}, "meta": {"count": 2}, "jsonapi": {"version": "1.0"}}
```

## Get one field data
### Request
```
curl -i -X GET http://localhost:5000/field_data/1
```

### Response
```
HTTP/1.0 200 OK
Content-Type: application/vnd.api+json   
Content-Length: 428
Server: Werkzeug/2.0.1 Python/3.9.6      
Date: Fri, 08 Oct 2021 00:06:23 GMT

{"data": {"type": "field_data", "attributes": {"media": "Media lnk", "date": "2000-10-10", "latitude": "90.5000000000", "comment": "Comment", "sector_id": 645, "media_type": "photo/video/etc", "recorded_by": 1234, "longitude": "456.5650000000", "sdg": "Goal", "title": "Title", "address": "Address", "ngo_id": 152}, "id": 1, "links": {"self": "/field_data/1"}}, "links": {"self": "/field_data/1"}, "jsonapi": {"version": "1.0"}}
```

## Update field data
### Request
```
curl -i -X PATCH -H 'Content-Type: application/vnd.api+json' -d '{"data":{"type":"field_data", "id":1, "attributes":{"title":"THIS WAS CHANGED"}}}' http://localhost:5000/field_data/1
```

### Response
```
HTTP/1.0 200 OK
Content-Type: application/vnd.api+json   
Content-Length: 439
Server: Werkzeug/2.0.1 Python/3.9.6      
Date: Fri, 08 Oct 2021 00:08:09 GMT      

{"data": {"type": "field_data", "attributes": {"media": "Media lnk", "date": "2000-10-10", "latitude": "90.5000000000", "comment": "Comment", "sector_id": 645, "media_type": "photo/video/etc", "recorded_by": 1234, "longitude": "456.5650000000", "sdg": "Goal", "title": "THIS WAS CHANGED", "address": "Address", "ngo_id": 152}, "id": 1, "links": {"self": "/field_data/1"}}, "links": {"self": "/field_data/1"}, "jsonapi": {"version": "1.0"}}
```


<br/>
<br/>
<br/>


# __member Tests__

__Note: Use the ngo.db file in member_preloaded_db folder to run these tests.__

<br/>
<br/>
<br/>

## Get a member:
### Request:
```
curl -i -X GET  http://localhost:5000/member/1
```

### Response:
```
HTTP/1.0 200 OK
Content-Type: application/vnd.api+json
Content-Length: 257
Server: Werkzeug/2.0.1 Python/3.9.6
Date: Fri, 08 Oct 2021 23:00:32 GMT

{"data": {"type": "member", "id": 1, "attributes": {"mobile": "999999999", "name": "A Name", "data_manager": "9596 4569 9455 5", "email": "email@email.com"}, "links": {"self": "/member/1"}}, "links": {"self": "/member/1"}, "jsonapi": {"version": "1.0"}}
```



## Update member
### Request
```
curl -i -X PATCH -H 'Content-Type: application/vnd.api+json' -d '{"data":{"type":"member", "id":1, "attributes":{"password":"new_password"}}}' http://localhost:5000/member/1
```

### Response
```
HTTP/1.0 200 OK
Content-Type: application/vnd.api+json
Content-Length: 257
Server: Werkzeug/2.0.1 Python/3.9.6
Date: Fri, 08 Oct 2021 23:07:00 GMT

{"data": {"type": "member", "attributes": {"data_manager": "9596 4569 9455 5", "mobile": "999999999", "name": "A Name", "email": "email@email.com"}, "id": 1, "links": {"self": "/member/1"}}, "links": {"self": "/member/1"}, "jsonapi": {"version": "1.0"}}
```



