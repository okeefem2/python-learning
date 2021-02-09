#!/usr/bin/env python

import subprocess
import optparse
import re


def parse_input():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Interface to change the MAC Address of')
    parser.add_option('-m', '--mac', dest='new_mac', help='New MAC Address')
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error('[-] Please specify an Interface, use --help for more info.')
    elif not options.new_mac:
        # Error
        parser.error('[-] Please specify a new MAC Address, use --help for more info.')
    else:
        return options


def change_mac(interface, new_mac):
    # Passing the commands as an array keeps the user from being able to pass extra commands
    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    # Not actually allowed in docker btw
    subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])

def get_mac(interface):
    ifconfig_result = subprocess.check_output(['ifconfig', interface]) \
        .decode("utf-8")  # Needed to cast bytes to string, str() also works...
    print(ifconfig_result)
    # (\w{2}:){5}(\w{2})

    mac_address_search_result = re.search(r'(\w{2}:){5}(\w{2})', ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print(f'Could not read mac address for interface {interface}')


options = parse_input()
current_mac = str(get_mac(options.interface))
change_mac(options.interface, options.new_mac)
new_mac = str(get_mac(options.interface))

if new_mac == options.new_mac:
    print(f'[+] MAC address was changed to {new_mac}')
else:
    print(f'[-] MAC address was not changed')

