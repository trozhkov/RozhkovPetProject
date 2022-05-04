#!/usr/bin/env bash
set -e

sleep 10s
python -m pytest -m ui --tb short --junitxml ${JUNIT_DIR?}/1.xml -n ${PYTEST_WORKERS:-1} --env prod --browser remote