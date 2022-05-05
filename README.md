# Asset-Tracking-CMMS
A Asset tracking and management computerized system

## Prerequisites
- Python 3.10
- requirement.txt file (included in the repository) must be installed.
- Postgresql
- Redis


## Instructions to run the project
- clone the project
- install the required packages using the command 
- pip install -r requirements.txt
- create .env file in your root directory if not exists.
- change the configuration according to your settings. below is the example for it.

```bash 

#DEBUG OPTION

DEBUG=on

#SECRET KEY

SECRET_KEY=django-insecure-+1mnl3=qvnldzhj3nsppa0%)0*=8lixnwt^gfq)j3l(_fmsa95

#DATABASE CONFIGURATION

DATABASE_NAME=postgres

DATABASE_USER=postgres

DATABASE_PASSWORD=farooq123

#https://console.cloud.google.com/sql/instances

#'34.65.219.241'(FOR CLOUD CHECK IP AND ADD IT TO THE GOOGLE CONSOLE) 

DATABASE_HOST=localhost

#at the moment of this writing google cloud postgresql is using the default postgresql port 5432

DATABASE_PORT=5432 
```

##Testing
- To test the apis install postman and hit the endpoints for example.
- http://localhost:8000/current_location/2
