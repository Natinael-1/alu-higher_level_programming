#!/bin/bash
# Script sends a GET request to the given URL with a custom header and displays the response body
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
