#!/bin/sh
# gunicorn worker_class default is `-k sync`

venv/bin/gunicorn -b 127.0.0.1:8888 _1_1_pure_flask:app
