#!/usr/bin/env bash

java -Dwebdriver.chrome.driver="./drivers/ubuntu/chromedriver" \
    -Dwebdriver.gecko.driver="./drivers/ubuntu/geckodriver" \
    -jar selenium-server-standalone-3.141.59.jar \
    -role node \
    -hub http://127.0.0.1:4444/grid/register \
    -browser browserName=chrome,maxInstances=2 \
    -browser browserName=firefox,maxInstances=2
