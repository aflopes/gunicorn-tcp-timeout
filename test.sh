#!/bin/bash

pip install gunicorn==20.1.0

cd /app
gunicorn -w 1 myapp:app &

# Give it time to start
sleep 2 

echo "Doing first request in background that will take 10 seconds"
python httpcall.py 20 &> first-request.out &

echo "Doing second request with a 1 second timeout, that will timeout and it should not processed by gunicorn worker"
python httpcall.py 1 &> second-request.out

# give time to client to timeout
sleep 2 

# print out tcp connections state
ss --tcp 

# give time for the first request to be processed and for the 
# second to make the gunicorn print the error message
sleep 10 
