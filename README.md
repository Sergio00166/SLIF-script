# SLIF-script

SLIF (ServiceListeningInterfaceFixer)

A very symple script that fixes a bug with some services when
you want to listen to ifaces that can be off when it autostarts
and the service will not listen to it until you restart the service.
<br>
This code checks for the changes and if it detects the interface is
now UP and the service was not listening to it (because it was off)
it will restart that service until all are up and exits.

Lets put an example, you start your home server and your kea-dhcp4-server starts, but you forgot to connect all cables,
kea-dhcp4-server wont listen that interface until you set all interfaces to up and restart the service, this script
is running at the background and when you plug a new cable it will restart the service automatically.

Must be runned as root and with a crontab @reboot clause if the service starts automatically

Works under ubuntu server
