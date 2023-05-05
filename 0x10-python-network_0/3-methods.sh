#!/bin/bash
# Display all HTTP methods that the server of the given URL will accept.
curl -sI -X OPTIONS "$1" | awk '/^Allow:/{print substr($0,8)}'
