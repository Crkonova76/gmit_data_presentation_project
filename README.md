## Data representation and querying 
### Martina Crkonova
### December 2020

## BJJ Limerick 
#### *Repositary https://github.com/Crkonova76/gmit_data_presentation_project*

The simplified flow of data is represented by illustration below:

### *Business Logic*

The reason for this assigned was to demonstrate the knowledge of the technologies learned in the subject.

Sipmle application used by local BJJ (sport ) club to track the current kids members. Kid member can be active or inactive and also kid member can be deleted. All data can be edited. This is all entry entry for more sofisticated application which I plan to develope in the future. Only the registered users can use application. Application does not use any encrypted password storage . In the future some third party technology can be used for this reason.

The superuser access is created (userName -admin, password -superuser) which can not be deleted by anyone. The plan is to exclude superuser from admin page in he future.

### *Database*

A database created named competition.

It contains two tables. The tables are not link by any foreign key. Below are displayed the description of both tables:



* creating_database.py is python file containing the code to initiate the database and tables. The SQL queries added to create, update and delete records from tables.

* db config.py created as configuration file


### *Server*

Flask web framework written in Python was used in this project. The file is called restServer.py. 
Two classes -KidsDAO and AdminsDAO are defined in project_database.py.

#### Authentication

Project uses sessions. Sessions are validated for each route. If session does not exist, user is redirected to login page. Also, if session does not exist user can not directly access any page. Session stores also the current user ID used in delete admin operation. User can not delete themself. Project also stores currently logged user, which is not further used in the application.

### *Templates-HTML*

Following files are saved ubder templates:
  * home.html
  * login.html
  * admins.html
  * membership.html

#### Encounted difficulties

  * problems with CSS style, intention to use separate separate file which can be linked to all pages
