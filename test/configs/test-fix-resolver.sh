#!/bin/bash

echo "Configuring SPINES..."
for i in $1*
do
echo -e "\n$i\n============"
echo "Copying config bundle."
scp ./resolv.conf $i:
echo "Applying configuration."
ssh $i "sudo cp ~/resolv.conf /etc/" >/dev/null 2>/dev/null
echo
done
