# CMPE273Assignment1
Implementing a dynamic Python invoker REST service
This flask application runs on Python and has 2 features:
 1. Python Script Uploader (POST)
 2. Python Script Invoker (GET)

Full instructions here: URL: https://github.com/sithu/cmpe273-fall17/tree/master/assignment1#request-1

----------

Resources Used:

 - https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
 - http://flask.pocoo.org/docs/0.12/patterns/fileuploads/

----------

To run the program, run app.py in one terminal window (python3 app.py) and in another terminal window run the curl commands. 

curl commands used in this homework assignment:

 - curl -i -X POST -H "Content-Type: multipart/form-data" -F "data=@tmp/foo.py" http://localhost:8000/api/v1/scripts
 - curl -i http://localhost:8000/api/v1/scripts/2
