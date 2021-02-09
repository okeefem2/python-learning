# MAC Address Changer

Mac (Media Access Control) addresses are permanent, physical and unique to the machine
are assigned by the manufacturer, used to id devices for data transfer 
packets have a source and destination mac address

Changing the mac address can make you anon on the network
MAC address is used for filters in networks, so you can impersonate, or bypass these filters

Manually changing the mac address in kali:
`apt install iproute2` -- for ip
`apt install net-tools` -- for ifconfig
`ifconfig`

eth0:
...
ether 02:42:ac:11:00:03  txqueuelen 0  (Ethernet) -- this line has the mac address
 
`ifconfig eth0 down`
`ifconfig eth0 hw ether {address}` -- 12 characters split every two with a colon `:`
`ifconfig eth0 up`

subprocess python module will let us run system commands for the OS

`python3 changeMacAddress.py -i eth0 -m a1:b0:00:bf:3r:o0` 