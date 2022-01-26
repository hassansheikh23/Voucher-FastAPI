# Voucher-API

### Requirement
* Docker Installed on system

### Libraries
Pandas\
Psycopg2\
FastAPI\
PyArrow\
Pydantic\
Uvicorn

### How to run
1) Download the repo on your system or clone it using below command if git is installed\
    git clone https://github.com/hassansheikh23/Voucher-FastAPI.git
2) Move into Voucher-API folder\
    cd Voucher-API
3) Run below command to run the docker containers\
    docker-compose up
4) Once containers are up and running, open another terminal and run below command\
    docker exec -it app /bin/bash
5) Once connected to app conatiner, run below command\
    python /Voucher-API/main.py
6) After script completed, API is ready to be use
7) Go to browser and type 127.0.0.1:8000/docs
8) It will open FastAPI built in SwaggerUI to test Api request
9) Click the "POST" button on UI and then select "Try it out"
10) Enter below json in request body to be send from client\
    {\
  "customer_id": 247,\
  "country_code": "Peru",\
  "last_order_ts": "2021-02-27 00:00:00",\
  "first_order_ts": "2020-08-07 00:00:00",\
  "total_orders": 15,\
  "segment_name": "recency_segment"\
}
11) Click Execute to see response from API
    
