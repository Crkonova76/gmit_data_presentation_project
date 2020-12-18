
from flask import Flask, jsonify, request, abort
from project_database import kidsDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

#app = Flask(__name__)

@app.route('/')
def index():
   return "Hmatattaorld!"

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




if __name__ == '__main__' :
    app.run(debug= True)