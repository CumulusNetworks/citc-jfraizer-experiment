#!/bin/bash
sleep 5
sudo systemctl restart networking.service
sudo systemctl restart frr.service
