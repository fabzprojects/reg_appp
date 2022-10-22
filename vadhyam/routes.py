from flask import Flask, render_template, request, redirect,  flash, abort, url_for
from vadhyam import app,db
from vadhyam import app
from vadhyam.models import *
from flask import Flask, request, jsonify, make_response


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(email=data['email'], name=data['name'], password=data['password'], contact=data['contact'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message' : 'New user created!'})



@app.route('/user', methods=['GET'])
def get_all_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['email'] = user.email
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['contact'] = user.contact
        output.append(user_data)
    return jsonify(output)


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email=data['email'] 
    password=data['password']
    user = User.query.filter_by(email=email,password=password).first()
    output=[]
    if user:
        user_data = {}
        user_data['id'] = user.id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['email'] = user.email
        user_data['contact'] = user.contact
        user_data['usertype'] = user.usertype
        output.append(user_data)

        return jsonify(output)

        # return jsonify({'Success' : 'Successfully Login'})
    else:
        return jsonify({'Failed' : 'Unauthorized Access'})




@app.route('/user/<id>', methods=['GET'])
def get_one_user( id):
    user = User.query.filter_by(id=id).first()
    output=[]
    if not user:
        return jsonify({'message' : 'No user found!'})

    user_data = {}
    user_data['id'] = user.id
    user_data['name'] = user.name
    user_data['password'] = user.password
    user_data['email'] = user.email
    user_data['contact'] = user.contact
    output.append(user_data)

    return jsonify(output)




@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.filter_by(id=id).first()

    if not user:
        return jsonify({'message' : 'No user found!'})

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message' : 'The user has been deleted!'})
