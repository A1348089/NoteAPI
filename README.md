 how to set up the project in local system.
 step-1: download the project anlong with the .venv
 step-2: open the root folder and then go to .venv/scripts and activate the virtual Environment 
 step-3: come back to the root folder
 step-4: open terminal and run python manage.py runserver.
 step-5: now follow the local host link "http://127.0.0.1:8000/"
 step-6: search "http://127.0.0.1:8000/notes/" to GET all the Notes from the database and also POST to create a new Note
 step-7: search "http://127.0.0.1:8000/notes/<int:pk>/ to retrive or Update the specific Note
 step-8: search "http://127.0.0.1:8000/notes?title=<substring> to get the list of Notes based on the title "<substring>"
