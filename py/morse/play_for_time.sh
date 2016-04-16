#!/bin/bash -x

speaker-test -t sine -f 600 &

sleep $1

kill -9 %1