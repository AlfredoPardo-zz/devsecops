# [Kube-bench](https://github.com/aquasecurity/kube-bench)

## Install from a container

> $ docker run --rm -v `pwd`:/host aquasec/kube-bench:latest install

> $ ./kube-bench master

> $ ./kube-bench node

## This command installs kube-bench locally

$ sudo docker run --rm -v `pwd`:/host aquasec/kube-bench:latest install

### Run with sudo (the results are different)

$ sudo ./kube-bench

$ sudo ./kube-bench --json

$ sudo ./kube-bench master --json

$ sudo ./kube-bench node --json

----------

# [Kube-hunter](https://github.com/aquasecurity/kube-hunter)

## Test it within the host

> $ sudo docker run -it --rm --network host aquasec/kube-hunter

## Scanning the Master Node from the outside

> $ docker run --rm aquasec/kube-hunter --remote 192.168.33.10

## Scanning the Worker Node from the outside
> $ docker run --rm aquasec/kube-hunter --remote 192.168.33.20

> $ docker run --rm aquasec/kube-hunter --remote 192.168.33.10 --report=json

----

# [KubiScan](https://github.com/cyberark/KubiScan)

## Prepare the Container
$ sudo docker run -it --rm -e CONF_PATH=~/.kube/config -v /:/tmp cyberark/kubiscan

> $ kubiscan --all

----
