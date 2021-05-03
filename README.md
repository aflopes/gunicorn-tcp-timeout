## Run with Docker
`docker run --rm -it -v $(pwd):/app python /app/test.sh `

## What does this do?
Simple test scenario with:
* A gunicorn server that sleeps for 10 seconds on the first request
* A python script to do simple http calls with a given timeout, and that on timeout or not, properly tries to close the TCP connection to the server
* A shell script that:
    - Starts the gunicorn server with a single `sync` worker
    - Does a first HTTP request in background (it will take 10 seconds) with a timeout of 15 seconds
    - Does a seconds HTTP request with a timeout of 1 second
    - Prints the server and clients related TCP connections state
    - Waits to see if the client timed out request is processed


## What was expected?
Given what is stated in https://github.com/benoitc/gunicorn/issues/1492 and in https://github.com/benoitc/gunicorn/issues/1190 I was expecting for the second request to be dropped and not processed by gunicorn


## What happens in reality?
The second request gets processed, despite that it as timed out on the client side, and that the client as properly started the connection close