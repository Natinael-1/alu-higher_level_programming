#!/bin/bash
# A script that sends an HTTP DELETE request to the URL passed as the first argument
curl -sX DELETE "$1"
