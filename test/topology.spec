

vm oob-mgmt-server netq-1.3.0 2 10 40

vm h3c01 cumulus-vx-3.6.0 1 2 2
vm h3c02 cumulus-vx-3.6.0 1 2 2
vm h3c03 cumulus-vx-3.6.0 1 2 2
vm h3c04 cumulus-vx-3.6.0 1 2 2

vm spine01.f01 cumulus-vx-3.5.3 1 2 2
vm spine02.f01 cumulus-vx-3.4.3 1 2 2
vm spine03.f01 cumulus-vx-3.4.3 1 2 2
vm spine04.f01 cumulus-vx-3.4.3 1 2 2
vm spine05.f01 cumulus-vx-3.4.3 1 2 2
vm spine06.f01 cumulus-vx-3.4.3 1 2 2
vm spine07.f01 cumulus-vx-3.4.3 1 2 2
vm spine08.f01 cumulus-vx-3.4.3 1 2 2
vm leaf01.p01 cumulus-vx-3.5.3 1 2 2
vm leaf02.p01 cumulus-vx-3.6.2 1 2 2
vm leaf03.p01 cumulus-vx-3.4.3 1 2 2
vm leaf04.p01 cumulus-vx-3.4.3 1 2 2
vm leaf05.p01 cumulus-vx-3.4.3 1 2 2
vm leaf06.p01 cumulus-vx-3.4.3 1 2 2
vm leaf07.p01 cumulus-vx-3.4.3 1 2 2
vm leaf08.p01 cumulus-vx-3.4.3 1 2 2
vm tor01.p01 cumulus-vx-3.5.3 1 2 2
vm tor02.p01 cumulus-vx-3.6.2 1 2 2
vm server01.p01 ubuntu-16.04 2 4 4
vm server02.p01 ubuntu-16.04 2 4 4

vm spine01.f02 cumulus-vx-3.5.3 1 2 2
vm spine02.f02 cumulus-vx-3.4.3 1 2 2
vm spine03.f02 cumulus-vx-3.4.3 1 2 2
vm spine04.f02 cumulus-vx-3.4.3 1 2 2
vm spine05.f02 cumulus-vx-3.4.3 1 2 2
vm spine06.f02 cumulus-vx-3.4.3 1 2 2
vm spine07.f02 cumulus-vx-3.4.3 1 2 2
vm spine08.f02 cumulus-vx-3.4.3 1 2 2
vm leaf01.p02 cumulus-vx-3.5.3 1 2 2
vm leaf02.p02 cumulus-vx-3.4.3 1 2 2
vm leaf03.p02 cumulus-vx-3.4.3 1 2 2
vm leaf04.p02 cumulus-vx-3.4.3 1 2 2
vm leaf05.p02 cumulus-vx-3.4.3 1 2 2
vm leaf06.p02 cumulus-vx-3.4.3 1 2 2
vm leaf07.p02 cumulus-vx-3.4.3 1 2 2
vm leaf08.p02 cumulus-vx-3.4.3 1 2 2
vm tor01.p02 cumulus-vx-3.4.3 1 2 2
vm tor02.p02 cumulus-vx-3.4.3 1 2 2
vm server01.p02 ubuntu-16.04 2 4 4
vm server02.p02 ubuntu-16.04 2 4 4

network oob-mgmt-server eth0 10.255.0.1 255.255.0.0 public
service oob-mgmt-server ssh eth0 22 TCP public
service oob-mgmt-server http eth0 80 TCP public
service oob-mgmt-server https eth0 443 TCP public
service oob-mgmt-server http2 eth0 1337 TCP public
service oob-mgmt-server grafana eth0 3000 TCP public
service oob-mgmt-server novnc eth0 6080 TCP public
service oob-mgmt-server netq eth0 9000 TCP public
service oob-mgmt-server mesos eth0 5050 TCP public
service oob-mgmt-server marathon eth0 8080 TCP public
service oob-mgmt-server mesosapp eth0 8088 TCP public

network oob-mgmt-server eth1 192.168.0.254 255.255.0.0

network spine01.f01 eth0 192.168.1.1 255.255.0.0
network spine02.f01 eth0 192.168.1.2 255.255.0.0
network spine03.f01 eth0 192.168.1.3 255.255.0.0
network spine04.f01 eth0 192.168.1.4 255.255.0.0
network spine05.f01 eth0 192.168.1.5 255.255.0.0
network spine06.f01 eth0 192.168.1.6 255.255.0.0
network spine07.f01 eth0 192.168.1.7 255.255.0.0
network spine08.f01 eth0 192.168.1.8 255.255.0.0
network leaf01.p01 eth0 192.168.1.11 255.255.0.0
network leaf02.p01 eth0 192.168.1.12 255.255.0.0
network leaf03.p01 eth0 192.168.1.13 255.255.0.0
network leaf04.p01 eth0 192.168.1.14 255.255.0.0
network leaf05.p01 eth0 192.168.1.15 255.255.0.0
network leaf06.p01 eth0 192.168.1.16 255.255.0.0
network leaf07.p01 eth0 192.168.1.17 255.255.0.0
network leaf08.p01 eth0 192.168.1.18 255.255.0.0
network tor01.p01 eth0 192.168.1.21 255.255.0.0
network tor02.p01 eth0 192.168.1.22 255.255.0.0
network server01.p01 eth0 192.168.1.31 255.255.0.0
network server02.p01 eth0 192.168.1.32 255.255.0.0

network spine01.f02 eth0 192.168.2.1 255.255.0.0
network spine02.f02 eth0 192.168.2.2 255.255.0.0
network spine03.f02 eth0 192.168.2.3 255.255.0.0
network spine04.f02 eth0 192.168.2.4 255.255.0.0
network spine05.f02 eth0 192.168.2.5 255.255.0.0
network spine06.f02 eth0 192.168.2.6 255.255.0.0
network spine07.f02 eth0 192.168.2.7 255.255.0.0
network spine08.f02 eth0 192.168.2.8 255.255.0.0
network leaf01.p02 eth0 192.168.2.11 255.255.0.0
network leaf02.p02 eth0 192.168.2.12 255.255.0.0
network leaf03.p02 eth0 192.168.2.13 255.255.0.0
network leaf04.p02 eth0 192.168.2.14 255.255.0.0
network leaf05.p02 eth0 192.168.2.15 255.255.0.0
network leaf06.p02 eth0 192.168.2.16 255.255.0.0
network leaf07.p02 eth0 192.168.2.17 255.255.0.0
network leaf08.p02 eth0 192.168.2.18 255.255.0.0
network tor01.p02 eth0 192.168.2.21 255.255.0.0
network tor02.p02 eth0 192.168.2.22 255.255.0.0
network server01.p02 eth0 192.168.2.31 255.255.0.0
network server02.p02 eth0 192.168.2.32 255.255.0.0

network h3c01 eth0 192.168.3.1 255.255.0.0
network h3c02 eth0 192.168.3.2 255.255.0.0
network h3c03 eth0 192.168.3.3 255.255.0.0
network h3c04 eth0 192.168.3.4 255.255.0.0


autoconfig oob-mgmt-server

#h3c
connect h3c01 swp1 spine01.f01 swp5
connect h3c01 swp2 spine02.f01 swp5
connect h3c01 swp3 spine03.f01 swp5
connect h3c01 swp4 spine04.f01 swp5

connect h3c02 swp1 spine01.f01 swp6
connect h3c02 swp2 spine02.f01 swp6
connect h3c02 swp3 spine03.f01 swp6
connect h3c02 swp4 spine04.f01 swp6

connect h3c03 swp1 spine01.f01 swp7
connect h3c03 swp2 spine02.f01 swp7
connect h3c03 swp3 spine03.f01 swp7
connect h3c03 swp4 spine04.f01 swp7

connect h3c04 swp1 spine01.f01 swp8
connect h3c04 swp2 spine02.f01 swp8
connect h3c04 swp3 spine03.f01 swp8
connect h3c04 swp4 spine04.f01 swp8

 # Pod01
 connect leaf01.p01 swp1 spine01.f01 swp1
 connect leaf01.p01 swp2 spine01.f01 swp2
 connect leaf01.p01 swp3 spine01.f02 swp1
 connect leaf01.p01 swp4 spine01.f02 swp2
 connect leaf01.p01 swp5 tor01.p01 swp1
 connect leaf01.p01 swp6 tor02.p01 swp1

 connect leaf02.p01 swp1 spine02.f01 swp1
 connect leaf02.p01 swp2 spine02.f01 swp2
 connect leaf02.p01 swp3 spine02.f02 swp1
 connect leaf02.p01 swp4 spine02.f02 swp2
 connect leaf02.p01 swp5 tor01.p01 swp2
 connect leaf02.p01 swp6 tor02.p01 swp2

 connect leaf03.p01 swp1 spine03.f01 swp1
 connect leaf03.p01 swp2 spine03.f01 swp2
 connect leaf03.p01 swp3 spine03.f02 swp1
 connect leaf03.p01 swp4 spine03.f02 swp2
 connect leaf03.p01 swp5 tor01.p01 swp3
 connect leaf03.p01 swp6 tor02.p01 swp3

 connect leaf04.p01 swp1 spine04.f01 swp1
 connect leaf04.p01 swp2 spine04.f01 swp2
 connect leaf04.p01 swp3 spine04.f02 swp1
 connect leaf04.p01 swp4 spine04.f02 swp2
 connect leaf04.p01 swp5 tor01.p01 swp4
 connect leaf04.p01 swp6 tor02.p01 swp4

 connect leaf05.p01 swp1 spine05.f01 swp1
 connect leaf05.p01 swp2 spine05.f01 swp2
 connect leaf05.p01 swp3 spine05.f02 swp1
 connect leaf05.p01 swp4 spine05.f02 swp2
 connect leaf05.p01 swp5 tor01.p01 swp5
 connect leaf05.p01 swp6 tor02.p01 swp5

 connect leaf06.p01 swp1 spine06.f01 swp1
 connect leaf06.p01 swp2 spine06.f01 swp2
 connect leaf06.p01 swp3 spine06.f02 swp1
 connect leaf06.p01 swp4 spine06.f02 swp2
 connect leaf06.p01 swp5 tor01.p01 swp6
 connect leaf06.p01 swp6 tor02.p01 swp6

 connect leaf07.p01 swp1 spine07.f01 swp1
 connect leaf07.p01 swp2 spine07.f01 swp2
 connect leaf07.p01 swp3 spine07.f02 swp1
 connect leaf07.p01 swp4 spine07.f02 swp2
 connect leaf07.p01 swp5 tor01.p01 swp7
 connect leaf07.p01 swp6 tor02.p01 swp7

 connect leaf08.p01 swp1 spine08.f01 swp1
 connect leaf08.p01 swp2 spine08.f01 swp2
 connect leaf08.p01 swp3 spine08.f02 swp1
 connect leaf08.p01 swp4 spine08.f02 swp2
 connect leaf08.p01 swp5 tor01.p01 swp8
 connect leaf08.p01 swp6 tor02.p01 swp8

 connect tor01.p01 swp9 server01.p01 eth1
 connect tor02.p01 swp9 server02.p01 eth1

 # Pod02
 connect leaf01.p02 swp1 spine01.f01 swp3
 connect leaf01.p02 swp2 spine01.f01 swp4
 connect leaf01.p02 swp3 spine01.f02 swp3
 connect leaf01.p02 swp4 spine01.f02 swp4
 connect leaf01.p02 swp5 tor01.p02 swp1
 connect leaf01.p02 swp6 tor02.p02 swp1

 connect leaf02.p02 swp1 spine02.f01 swp3
 connect leaf02.p02 swp2 spine02.f01 swp4
 connect leaf02.p02 swp3 spine02.f02 swp3
 connect leaf02.p02 swp4 spine02.f02 swp4
 connect leaf02.p02 swp5 tor01.p02 swp2
 connect leaf02.p02 swp6 tor02.p02 swp2

 connect leaf03.p02 swp1 spine03.f01 swp3
 connect leaf03.p02 swp2 spine03.f01 swp4
 connect leaf03.p02 swp3 spine03.f02 swp3
 connect leaf03.p02 swp4 spine03.f02 swp4
 connect leaf03.p02 swp5 tor01.p02 swp3
 connect leaf03.p02 swp6 tor02.p02 swp3

 connect leaf04.p02 swp1 spine04.f01 swp3
 connect leaf04.p02 swp2 spine04.f01 swp4
 connect leaf04.p02 swp3 spine04.f02 swp3
 connect leaf04.p02 swp4 spine04.f02 swp4
 connect leaf04.p02 swp5 tor01.p02 swp4
 connect leaf04.p02 swp6 tor02.p02 swp4

 connect leaf05.p02 swp1 spine05.f01 swp3
 connect leaf05.p02 swp2 spine05.f01 swp4
 connect leaf05.p02 swp3 spine05.f02 swp3
 connect leaf05.p02 swp4 spine05.f02 swp4
 connect leaf05.p02 swp5 tor01.p02 swp5
 connect leaf05.p02 swp6 tor02.p02 swp5

 connect leaf06.p02 swp1 spine06.f01 swp3
 connect leaf06.p02 swp2 spine06.f01 swp4
 connect leaf06.p02 swp3 spine06.f02 swp3
 connect leaf06.p02 swp4 spine06.f02 swp4
 connect leaf06.p02 swp5 tor01.p02 swp6
 connect leaf06.p02 swp6 tor02.p02 swp6

 connect leaf07.p02 swp1 spine07.f01 swp3
 connect leaf07.p02 swp2 spine07.f01 swp4
 connect leaf07.p02 swp3 spine07.f02 swp3
 connect leaf07.p02 swp4 spine07.f02 swp4
 connect leaf07.p02 swp5 tor01.p02 swp7
 connect leaf07.p02 swp6 tor02.p02 swp7

 connect leaf08.p02 swp1 spine08.f01 swp3
 connect leaf08.p02 swp2 spine08.f01 swp4
 connect leaf08.p02 swp3 spine08.f02 swp3
 connect leaf08.p02 swp4 spine08.f02 swp4
 connect leaf08.p02 swp5 tor01.p02 swp8
 connect leaf08.p02 swp6 tor02.p02 swp8

 connect tor01.p02 swp9 server01.p02 eth1
 connect tor02.p02 swp9 server02.p02 eth1

