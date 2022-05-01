#!/usr/bin/env bash
set -e

export SCREENSHOTS_DIR=screenshots
export JUNIT_DIR=junit

#rm -rf ${SCREENSHOTS_DIR?}/* || mkdir -p ${SCREENSHOTS_DIR?}
#rm -rf ${JUNIT_DIR?}/* || mkdir -p ${JUNIT_DIR?}
#trap "chmod -R 777 ${SCREENSHOTS_DIR?} ${JUNIT_DIR?}" EXIT

export PYTEST_WORKERS=2

python -m pytest -m ui --tb short --junitxml ${JUNIT_DIR?}/1.xml -n ${PYTEST_WORKERS:-1} --env prod --browser chrome