#!/usr/bin/env bash
cd /home/pi/Bobo/ComputerVision442
sleep 30
ssh -i "/home/pi/.ssh/id_rsa" -R 6969:localhost:22 pi@laftr.ddns.net
while true;
do
if [[ $(git pull | tail -n +2) ]]; then
    killall python3
    python3 main.py
fi
sleep 1
done