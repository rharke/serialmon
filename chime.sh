#!/bin/bash

# This is just an example of script that you could run in response to a serial event

/usr/bin/curl --silent --output /dev/null --max-time 5 http://192.168.0.50:8000/chime?type=doorbell &
