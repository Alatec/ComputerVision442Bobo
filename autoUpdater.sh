#!/usr/bin/env bash
cd /home/pi/Bobo/ComputerVision442
export DISPLAY=:0.0
while true;
do
if [[ $(git pull | tail -n +2) ]]; then
    killall python3
    python3 main.py
fi
sleep 1
done