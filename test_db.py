from project_database import kidsDAO
from project_database import adminsDAO

#create
#latestid=kidsDAO.create(("James1","Mahony1","Limerick1","John1", "1085639425"))
#latestid=kidsDAO.create(("James2","Mahony2","Limerick2","John2", "2085639425"))


# #create JSON object
# kid1={
#     "registration":"1",
#     "name":"Peter",
#     "surname":"Fitzpat",
#     "team":"Puchov",
#     "emergencyContactName":"jjjj",
#     "phoneNumber":"569236"
# }
# kid2={
#     "registration":"",
#     "name":"Alan",
#     "surname":"Crkon",
#     "team":"Blava",
#     "emergencyContactName":"Mar",
#     "phoneNumber":"569245"
# }
# returnValue=kidsDAO.create(kid1)
# print(returnValue)

# returnValue=kidsDAO.getAll()
# print(returnValue)

# returnValue=kidsDAO.findByID(kid1['registration'])
# print(returnValue)

# # returnValue=kidsDAO.update(kid2)
# # print(returnValue)

# returnValue=kidsDAO.findByID(kid2['registration'])
# print("find by ID")
# print(returnValue)

# # zmenena. vid dole
# # returnValue=kidsDAO.delete(kid1['registration'])
# # print(returnValue)

# returnValue=kidsDAO.delete(20)
# print(returnValue)

# returnValue=kidsDAO.getAll()
# print(returnValue)



#find by id
#result=kidsDAO.findByID(3)
 
#print(result)


#create JSON object
# admin1={
#     "id":"1",
#     "UserName":"Peter",
#     "Password":"Akosa"
    
# }

admin2={
    "id":" ",
    "UserName":"Michal",
    "Password":"A1236"
    
}

admin3={
    "id":" ",
    "UserName":"Mata",
    "Password":"B1236"
    
}

returnValue=adminsDAO.createAdmin(admin3)
print(returnValue)

# returnValue=adminsDAO.deleteAdmins(2)
# print(returnValue)

# returnValue=adminsDAO.deleteAll()
# print(returnValue)