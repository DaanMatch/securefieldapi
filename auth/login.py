from flask import jsonify, request, make_response
import jwt
import datetime

from config import SECRET_KEY
from models import Member

def login_member(): 
 
    auth = request.authorization   

    if not auth or not auth.username or not auth.password:  
        return make_response('could not verify', 401, 
            {'WWW.Authentication': 'Basic realm: "login required"'})    

    member = Member.query.filter_by(id=auth.username).first()   
        
    if member.password == auth.password:  
        token = jwt.encode(
            {
                'member_id': member.id, 
                'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }, 
            SECRET_KEY)  
        
        return jsonify({'data' : {'token' : token.decode('utf-8')}}) 

    return make_response('could not verify',  401, 
        {'WWW.Authentication': 'Basic realm: "login required"'})