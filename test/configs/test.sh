#!/bin/bash

echo "Configuring SPINES..."
for i in spine*
do
echo -e "\n$i\n============"
echo "Copying config bundle."
scp $i/configs.tgz $i:
scp ./resolv.conf $i:
echo "Applying configuration."
ssh $i "cd /; sudo tar xf ~/configs.tgz; sudo systemctl restart networking.service; sudo systemctl restart frr.service; sudo cp ~/resolv.conf /etc/; sudo ip route del default" >/dev/null 2>/dev/null
echo
done
