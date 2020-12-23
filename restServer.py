
from flask import Flask, jsonify, url_for, request, abort, session, render_template, flash, redirect
from project_database import kidsDAO
from project_database import adminsDAO
import os

app = Flask(__name__, static_url_path='', static_folder='staticpages')

#app = Flask(__name__)

# @app.route('/')
# def index():
#    return "Hmatattaorld!"

@app.route('/',  methods=['GET'])
def home():
    print(session.get('logged_in'))
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return competitors()

@app.route('/competitors', methods=['POST', 'GET'])
def competitors():
    if not session.get('logged_in'):
        # return render_template('login.html')
        return home()
    else:
        return render_template('index.html')      

@app.route('/login', methods=['POST'])
def do_admin_login():
    login = request.form
    userName = login['username']
    password = login['password']
 
    if userName == 'password' and password=='admin':
        session['logged_in'] = True
        session['username'] = 'username'
        session['password'] = 'admin'
        print(f"username {session['username']}")
        print(f"password {session['password']}")
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


# curl  -i -H "Content-Type:application/json" -X POST -d "{\"registration\":2,\"name\":\"Zuza\",\"surname\":\"Marchevka\",\"team\":\"Kosice\",\"emergencyContactName\":\"Jano\",\"phoneNumber\":\"5689\"}" http://127.0.0.1:5000/kids
@app.route('/kids', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    kid = {
        "registration":request.json["registration"],
        "name":request.json["name"],
        "surname":request.json["surname"],
        "team":request.json["team"],
        "emergencyContactName":request.json["emergencyContactName"],
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
    if 'team' in request.json:
        found_kid['team'] = request.json['team']
    if 'emergencyContactName' in request.json:
        found_kid['emergencyContactName'] = request.json['emergencyContactName']
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