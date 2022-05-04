#!/usr/bin/env bash
set -e

export SCREENSHOTS_DIR=screenshots
export JUNIT_DIR=junit

export PYTEST_WORKERS=4

sleep 10s
python -m pytest -m ui --tb short --junitxml ${JUNIT_DIR?}/1.xml -n ${PYTEST_WORKERS:-1} --env prod --browser remote