
## Post a member __FOR TESTING PURPOSES ONLY NOT FUNCTIONAL IN PRODUCTION__
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

{"data": {"type": "member", "attributes": {"mobile_device_id": null, "mobile": null, "email": null, "name": null}, "relationships": {"field_data": {"links": {"self": "/member/3/field_data", "related": "/field_data/3"}}}, "id": 3, "links": {"self": "/member/3"}}, "links": {"self": "/member/3"}, "jsonapi": {"version": "1.0"}}
```

<br/>
<br/>
<br/>


# __field_data Tests__

## Post a field_data
### Request
```
curl -i -X POST -H 'Content-Type: application/vnd.api+json' -d '{"data":{"type":"field_data", "attributes":{"ngo_id":152, "recorded_by":1, "date":"2000-10-10", "address":"Address", "latitude":90.5, "longitude":456.565, "title":"Title", "comment":"Comment", "media":"Media lnk", "media_type":"photo/video/etc", "sector_id":645, "sdg": "Goal"}}}' http://localhost:5000/field_data
```

### Response
```
HTTP/1.0 201 CREATED
Location: http://localhost:5000/field_data/1
Content-Type: application/vnd.api+json   
Content-Length: 428
Server: Werkzeug/2.0.1 Python/3.9.6      
Date: Fri, 08 Oct 2021 00:05:22 GMT      

{"data": {"type": "field_data", "attributes": {"media": "Media lnk", "date": "2000-10-10", "latitude": "90.5000000000", "comment": "Comment", "sector_id": 645, "media_type": "photo/video/etc", "recorded_by": 1, "longitude": "456.5650000000", "sdg": "Goal", "title": "Title", "address": "Address", "ngo_id": 152}, "id": 1, "links": {"self": "/field_data/1"}}, "links": {"self": "/field_data/1"}, "jsonapi": {"version": "1.0"}}
```

## Get all field data
### Request
```
curl -i -X GET http://localhost:5000/field_data
```

### Response
```
HTTP/1.0 200 OK
Content-Type: application/vnd.api+json   
Content-Length: 471
Server: Werkzeug/2.0.1 Python/3.9.6      
Date: Fri, 08 Oct 2021 00:05:48 GMT      

{"data": [{"type": "field_data", "attributes": {"media": "Media lnk", "date": "2000-10-10", "latitude": "90.5000000000", "comment": "Comment", "sector_id": 645, "media_type": "photo/video/etc", "recorded_by": 1234, "longitude": "456.5650000000", "sdg": "Goal", "title": "Title", "address": "Address", "ngo_id": 152}, "id": 1, "links": {"self": "/field_data/1"}}], "links": {"self": "http://localhost:5000/field_data"}, "meta": {"count": 1}, "jsonapi": {"version": "1.0"}}
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

{"data": {"type": "member", "id": 1, "attributes": {"mobile": "999999999", "name": "A Name", "mobile_device_id": "9596 4569 9455 5", "email": "email@email.com"}, "links": {"self": "/member/1"}}, "links": {"self": "/member/1"}, "jsonapi": {"version": "1.0"}}
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

{"data": {"type": "member", "attributes": {"mobile_device_id": "9596 4569 9455 5", "mobile": "999999999", "name": "A Name", "email": "email@email.com"}, "id": 1, "links": {"self": "/member/1"}}, "links": {"self": "/member/1"}, "jsonapi": {"version": "1.0"}}
```



