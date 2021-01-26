#!/bin/sh
service ssh start
exec python -u /src/server_secure.py
