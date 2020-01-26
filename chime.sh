#!/bin/bash

# This is just an example of script that you could run in response to a serial event

/usr/bin/curl --silent --output --max-time 5 /dev/null http://192.168.0.50:8000/chime?type=doorbell &
