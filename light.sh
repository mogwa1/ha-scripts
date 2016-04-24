#!/bin/bash
gpio mode $1 output
gpio write $1 1
sleep $2
gpio write $1 0
