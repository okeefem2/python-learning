# Ethical Hacking

To run the kali linux container
`docker build -t okeefem/kali .`
`docker run --network=host -it --name kali --volume $(pwd):/develop okeefem/kali`
`docker start -i kali` to restart the container and interact with it
## Lab

Virtual machines/Containers?
https://www.kali.org/docs/containers/using-kali-docker-images/


## Network scanner

Create a new container to use for networking

`docker run -dit --network=host --name alpine-target alpine ash`



## ARP Spoofing

Clients can accept responses even if they did not send a request without any verification, this can be leveraged to tell a (victim) computer that
you are the IP of the router, and you can tell the router you are at the IP of the viction, so all traffic goes
through your machine first.

So to guard from that how would you do that... some form of verification

`arpspoof -i eth0 -t {target} {gateway}` with the interface to spoof the target ip that you want to spoof and the gateway
    - run `arp -a` on target to spoof and grab the interface address for target
    - run `arp -a` on spoof machine to grab the gateway address
this will fool the target into thinking you are the gateway

Then also run the same command with {target} and {gateway} flipped to reverse the spoof so the gateway believes you are the target

in linux, port forwarding must be on for traffic to flow through the spoofer, otherwise no responses will make it through to either side from the other.

echo 1 > `/proc/sys/net/ipv4/ip_forward` 

  