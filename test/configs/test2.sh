#!/bin/bash

echo "Configuring SPINES..."
for i in spine*
do
echo -e "\n$i\n============"
ssh $i "net add routing prefix-list ipv4 DEFAULT seq 5 permit 0.0.0.0/0; net add routing route-map NO-DEFAULT-IN deny 10 match ip address prefix-list DEFAULT; net add routing route-map NO-DEFAULT-IN permit 20; net add bgp ipv4 unicast neighbor LEAFS route-map NO-DEFAULT-IN in; net commit"
echo
done

