#!/usr/bin/env bash
set -e

# environment
export SCREENSHOTS_DIR="rozhkovPetProject/screenshots"
export JUNIT_DIR="rozhkovPetProject/junit"
export SELENIUM_URL="http://172.19.0.2:4444"
export PROD_URL="http://rozhkovqa.tilda.ws/test_form"
export DEV_URL="http://rozhkovqa.tilda.ws/test_form"
export PYTEST_WORKERS=4

sleep 10s
python -m pytest -m "dev" --tb short --junitxml ${JUNIT_DIR?}/1.xml -n ${PYTEST_WORKERS:-1} --env local --browser chrome