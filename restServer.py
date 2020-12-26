
from flask import Flask, jsonify, url_for, request, abort, session, render_template, flash, redirect
from project_database import kidsDAO
from project_database import adminsDAO
import os

# app = Flask(__name__, static_url_path='', static_folder='staticpages')
app = Flask(__name__, static_url_path='')


@app.route('/',  methods=['GET'])
def home():
    print(session.get('logged_in'))
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return home_page()

@app.route('/membership',  methods=['GET'])
def membership():
    print(session.get('logged_in'))
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('membership.html')

@app.route('/administrators',  methods=['GET'])
def admins():
    print(session.get('logged_in'))
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('admins.html')

@app.route('/home', methods=['POST', 'GET'])
def home_page():
    if not session.get('logged_in'):
        return home()
    else:
        return render_template('home.html')     

def get_users():
    return adminsDAO.getAllAdmins() 


def current_user(username, password):
    users = get_users()
    for i in range(len(users)):
        if users[i]['UserName'] == username:
            if users[i]['Password'] == password:      
                session['user_id'] = users[i]['id']
                session['user_name'] = username
                return True

@app.route('/login', methods=['POST'])
def do_admin_login():
    login = request.form
    userName = login['username']
    password = login['password']
    access = current_user(userName, password)
    
    if access:
        session['logged_in'] = True
    else:
        flash('wrong password!') 
        session['logged_in'] = False           
    return home()

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return render_template('login.html')

#curl"Http://127.0.0.1:5000/kids"
@app.route('/kids')
def getAll():
    return jsonify(kidsDAO.getAll())

#curl " Http://127.0.0.1:5000/kids/2"
@app.route('/kids/<int:registration>')
def findById(registration):    
    return jsonify(kidsDAO.findByID(registration))


# curl  -i -H "Content-Type:application/json" -X POST -d "{\"registration\":2,\"name\":\"Zuza\",\"surname\":\"Marchevka\",\"belt\":\"Kosice\",\"status\":\"Jano\",\"Inactive\":\"5689\"}" http://127.0.0.1:5000/kids
@app.route('/kids', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    kid = {
        "registration":request.json["registration"],
        "name":request.json["name"],
        "surname":request.json["surname"],
        "belt":request.json["belt"],
        "status":request.json["status"],
        "phoneNumber":request.json["phoneNumber"]
    }
    
    return jsonify(kidsDAO.create(kid))

#curl -i -H "Content-Type:application/json" -X PUT -d "{\"name\":\"Miro\"}" http://127.0.0.1:5000/kids/16
@app.route('/kids/<int:registration>', methods=['PUT'])
def update(registration):
    foundkids=kidsDAO.findByID(registration)
    
    if foundkids == {}:
        return jsonify({}),404
    found_kid = foundkids
              
    if 'name' in request.json:
        found_kid['name'] = request.json['name']
    if 'surname' in request.json:
        found_kid['surname'] = request.json['surname']
    if 'belt' in request.json:
        found_kid['belt'] = request.json['belt']
    if 'status' in request.json:
        found_kid['status'] = request.json['status']
    if 'phoneNumber' in request.json:
        found_kid['phoneNumber'] = request.json['phoneNumber']
    
    kidsDAO.update(found_kid)
    return jsonify(found_kid)
        

    # return "in update for id "+str(registration)

# curl -i -H "Content-Type:application/json" -X DELETE http://127.0.0.1:5000/kids/16
@app.route('/kids/<int:registration>' , methods=['DELETE'])
def delete(registration):
    kidsDAO.delete(registration)
    return jsonify({"done":True})

# -----------------------------------------------------
# ------------------- Admin section -------------------
# -----------------------------------------------------
   

# curl "http://127.0.0.1:5000/admins"
@app.route('/admins', methods=['GET'])
def getAllAdmins():
    return jsonify(adminsDAO.getAllAdmins())

# curl  -i -H "Content-Type:application/json" -X POST -d "{\"id\":9,\"UserName\":\"Zuza\",\"Password\":\"Marchevka\"}" http://127.0.0.1:5000/admins
@app.route('/admins', methods=['POST'])
def createAdmin():
    
    if not request.json:
        abort(400)
    # other checking 
    admin = {
        "id":request.json["id"],
        "UserName":request.json["UserName"],
        "Password":request.json["Password"]
        
    }
    return jsonify(adminsDAO.createAdmin(admin))


# curl -i -H "Content-Type:application/json" -X DELETE http://127.0.0.1:5000/admins/8
@app.route('/admins/<int:id>' , methods=['DELETE'])
def deleteAdmin(id):
    if session['user_id']==id:
        return jsonify({}),400
    else:
        adminsDAO.deleteAdmin(id)
        return jsonify(adminsDAO.deleteAdmin(id))

# curl -i -H "Content-Type:application/json" -X DELETE http://127.0.0.1:5000/admins
@app.route('/admins' , methods=['DELETE'])
def deleteAll():
    adminsDAO.deleteAll()    
    return jsonify(adminsDAO.deleteAll())


if __name__ == '__main__' :
    app.secret_key = os.urandom(12)
    app.run(debug= True)