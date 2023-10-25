#!/usr/bin/bash
cd `dirname $0`

source .env
./setup.sh

# Be sure to use `exec` so that termination signals reach the python process,
# or handle forwarding termination signals manually
exec $PYTHON -m src.main $@
