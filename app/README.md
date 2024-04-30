# Application and its division

In this folder, there are two different sub-divisions:

## 1 -> flaskapp
Contains the information from the backend of our product. There are two different programming languages in this file: python (.py) and SQL (.sql). In this folder you will find:

### app.py 
-> where the code for database connection with @routes is stored, as well as main portions of the structure of the database/application connection.

### migrations.json
_> migrations.json is a file indicating the destination ID of an application where one or multiple tables will be transferred. It facilitates users in relocating table and field data, like moving from a code customization within the primary application to an extension of the same application.

### models.py
-> this file contains the backbone of our database. all of the models are defined here and it is used by reset.from.peewee when creating the database.

### requirements.txt
-> description of all of the technologies and their versions used in this section of the project. 

### reset.from.peewee.sh
-> file that drops and creates tables based on the rest of the program. It initializes the database.

### tables.sql
-> file containing the code for creating the tables to UP database in SQL.

## 2 -> Frontend
Contains information for the frontend portion of UP application. It is divided in two sub-folders: public (a system convention, for this application it contains UP logo file used in the web application) and src (containing the code for the application's frontend). The other files in the folder (babel.config.js, jsconfig.json, package-lock.json, package.json, vue.config.js) are system files to ensure the operationality of json, javascript, and vue, main parts of the application. src, the file with the coding portion uses the framework vue for frontend development, and it is explained below:

### src 
# Frontend Folder Structure
### Folders
This folder contains the source code for the frontend application. It includes the following subfolders:

components: This folder contains reusable UI components that are used throughout the application.
pages: This folder contains the different pages of the application, each representing a specific route or view.
assets: This folder contains static assets such as images, fonts, or other media files used in the application.
router: This folder contain the file index.js, which defines the routes for the application. It maps URLs to specific components or pages.
views: This folder contains .vue framework usage. To ensure usability and UI advances, UP application uses .vue, which compiles the information and makes the backend-frontend correspondence.

# How to put database to work:
Step 1 -> download all required files: package.json, pipfile.lock, requirements.md
Step 2 -> Open a backend server: on the terminal, open "flaskapp directory", start the "pipenv shell" virtual environment, run app.py "python app.py" (send API calls to frontend)
# For backend, on the terminal, type
cd flaskapp
pipenv shell
python app.py
Step 3 -> Open a frontend server: directory ""frontend" and start node.js. The below commands run a local environment, but creating the site will need npm to build.
## For frontend, on the terminal, type:
cd frontend
npm run serve 