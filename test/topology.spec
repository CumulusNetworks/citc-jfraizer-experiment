vm oob-mgmt-server netq-1.3.0 2 10 40

vm spine01.p01 cumulus-vx-3.4.3 1 2 2
vm spine02.p01 cumulus-vx-3.4.3 1 2 2
vm spine03.p01 cumulus-vx-3.4.3 1 2 2
vm spine04.p01 cumulus-vx-3.4.3 1 2 2
vm spine05.p01 cumulus-vx-3.4.3 1 2 2
vm spine06.p01 cumulus-vx-3.4.3 1 2 2
vm spine07.p01 cumulus-vx-3.4.3 1 2 2
vm spine08.p01 cumulus-vx-3.4.3 1 2 2
vm leaf01.p01 cumulus-vx-3.4.3 1 2 2
vm leaf02.p01 cumulus-vx-3.4.3 1 2 2
vm leaf03.p01 cumulus-vx-3.4.3 1 2 2
vm leaf04.p01 cumulus-vx-3.4.3 1 2 2
vm leaf05.p01 cumulus-vx-3.4.3 1 2 2
vm leaf06.p01 cumulus-vx-3.4.3 1 2 2
vm leaf07.p01 cumulus-vx-3.4.3 1 2 2
vm leaf08.p01 cumulus-vx-3.4.3 1 2 2
vm server01.p01 ubuntu-16.04 2 4 4
vm server02.p01 ubuntu-16.04 2 4 4

vm spine01.p02 cumulus-vx-3.4.3 1 2 2
vm spine02.p02 cumulus-vx-3.4.3 1 2 2
vm spine03.p02 cumulus-vx-3.4.3 1 2 2
vm spine04.p02 cumulus-vx-3.4.3 1 2 2
vm spine05.p02 cumulus-vx-3.4.3 1 2 2
vm spine06.p02 cumulus-vx-3.4.3 1 2 2
vm spine07.p02 cumulus-vx-3.4.3 1 2 2
vm spine08.p02 cumulus-vx-3.4.3 1 2 2
vm leaf01.p02 cumulus-vx-3.4.3 1 2 2
vm leaf02.p02 cumulus-vx-3.4.3 1 2 2
vm leaf03.p02 cumulus-vx-3.4.3 1 2 2
vm leaf04.p02 cumulus-vx-3.4.3 1 2 2
vm leaf05.p02 cumulus-vx-3.4.3 1 2 2
vm leaf06.p02 cumulus-vx-3.4.3 1 2 2
vm leaf07.p02 cumulus-vx-3.4.3 1 2 2
vm leaf08.p02 cumulus-vx-3.4.3 1 2 2
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

network spine01.p01 eth0 192.168.1.1 255.255.0.0
network spine02.p01 eth0 192.168.1.2 255.255.0.0
network spine03.p01 eth0 192.168.1.3 255.255.0.0
network spine04.p01 eth0 192.168.1.4 255.255.0.0
network spine05.p01 eth0 192.168.1.5 255.255.0.0
network spine06.p01 eth0 192.168.1.6 255.255.0.0
network spine07.p01 eth0 192.168.1.7 255.255.0.0
network spine08.p01 eth0 192.168.1.8 255.255.0.0
network leaf01.p01 eth0 192.168.1.11 255.255.0.0
network leaf02.p01 eth0 192.168.1.12 255.255.0.0
network leaf03.p01 eth0 192.168.1.13 255.255.0.0
network leaf04.p01 eth0 192.168.1.14 255.255.0.0
network leaf05.p01 eth0 192.168.1.15 255.255.0.0
network leaf06.p01 eth0 192.168.1.16 255.255.0.0
network leaf07.p01 eth0 192.168.1.17 255.255.0.0
network leaf08.p01 eth0 192.168.1.18 255.255.0.0
network server01.p01 eth0 192.168.1.21 255.255.0.0
network server02.p01 eth0 192.168.1.22 255.255.0.0

network spine01.p02 eth0 192.168.2.1 255.255.0.0
network spine02.p02 eth0 192.168.2.2 255.255.0.0
network spine03.p02 eth0 192.168.2.3 255.255.0.0
network spine04.p02 eth0 192.168.2.4 255.255.0.0
network spine05.p02 eth0 192.168.2.5 255.255.0.0
network spine06.p02 eth0 192.168.2.6 255.255.0.0
network spine07.p02 eth0 192.168.2.7 255.255.0.0
network spine08.p02 eth0 192.168.2.8 255.255.0.0
network leaf01.p02 eth0 192.168.2.11 255.255.0.0
network leaf02.p02 eth0 192.168.2.12 255.255.0.0
network leaf03.p02 eth0 192.168.2.13 255.255.0.0
network leaf04.p02 eth0 192.168.2.14 255.255.0.0
network leaf05.p02 eth0 192.168.2.15 255.255.0.0
network leaf06.p02 eth0 192.168.2.16 255.255.0.0
network leaf07.p02 eth0 192.168.2.17 255.255.0.0
network leaf08.p02 eth0 192.168.2.18 255.255.0.0
network server01.p02 eth0 192.168.2.21 255.255.0.0
network server02.p02 eth0 192.168.2.22 255.255.0.0

autoconfig oob-mgmt-server

 connect leaf01 swp51 spine01 swp1
 connect leaf02 swp51 spine01 swp2
 connect leaf03 swp51 spine01 swp3
 connect leaf04 swp51 spine01 swp4
 connect leaf01 swp52 spine02 swp1
 connect leaf02 swp52 spine02 swp2
 connect leaf03 swp52 spine02 swp3
 connect leaf04 swp52 spine02 swp4
 connect leaf01 swp49 leaf02 swp49
 connect leaf01 swp50 leaf02 swp50
 connect leaf03 swp49 leaf04 swp49
 connect leaf03 swp50 leaf04 swp50
 connect spine01 swp31 spine02 swp31
 connect spine01 swp32 spine02 swp32
 connect server01 eth1 leaf01 swp1
 connect server01 eth2 leaf02 swp1
 connect server02 eth1 leaf01 swp2
 connect server02 eth2 leaf02 swp2
 connect server03 eth1 leaf03 swp1
 connect server03 eth2 leaf04 swp1
 connect server04 eth1 leaf03 swp2
 connect server04 eth2 leaf04 swp2
 connect leaf01 swp44 oob-mgmt-server eth2
 connect leaf02 swp44 oob-mgmt-server eth3
 connect leaf01 swp45 leaf01 swp46
 connect leaf01 swp47 leaf01 swp48
 connect leaf02 swp45 leaf02 swp46
 connect leaf02 swp47 leaf02 swp48
 connect leaf03 swp45 leaf03 swp46
 connect leaf03 swp47 leaf03 swp48
 connect leaf04 swp45 leaf04 swp46
 connect leaf04 swp47 leaf04 swp48
