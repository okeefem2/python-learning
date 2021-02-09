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

