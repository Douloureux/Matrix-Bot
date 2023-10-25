#!/bin/bash
source vars
export PYTHONPATH=$SOURCE_LOCATION
cd $SOURCE_LOCATION/scheduler
source ../.venv/bin/activate
python youtube.py