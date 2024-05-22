# Code by Sergio1260

"""
SLIF (ServiceListeningInterfaceFixer)

A fixer for services when you want to listen to ifaces that
can be off when it autostarts and the service will not listen
to it until you restart the service. This code checks for the
changes and if it detects the interface is now UP and the
service was not listening to it (because it was off) it will
restart that service until all are up and exits.

Must be runned as root
"""

ifaces = [ "ens4f1", "ens2" ]
srv = [ "kea-dhcp4-server", "nginx" ]

from subprocess import check_output as chout
from os import system as cmd
from time import sleep as delay

def getstatus(ifaces):
    ext="ip link show "; out=[]
    for x in ifaces:
        raw=chout(ext+x, shell=True)
        raw=str(raw, encoding="UTF-8")
        raw=raw[raw.find("state")+6:]
        raw=raw[:raw.find(" ")]
        out.append(raw=="UP")
    return out

def restart(srv):
    ext="systemctl restart "
    cmd(ext+" ".join(srv))

def main():
    orig = getstatus(ifaces); wasup = orig[:]
    if not all(orig):
        while True:
            delay(1); st=getstatus(ifaces)
            if all(st): restart(srv); break
            for x in st:
                idx = st.index(x)
                y = orig[idx]
                z = wasup[idx]
                if not x == y and x and not z:
                    wasup=st[:]; orig = st[:]
                    restart(srv); break 

if __name__=="__main__": main()
    
