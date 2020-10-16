# Kube-bench
https://github.com/aquasecurity/kube-bench

## Install from a container
docker run --rm -v `pwd`:/host aquasec/kube-bench:latest install

./kube-bench master
./kube-bench node

## This command installs kube-bench locally
$ sudo docker run --rm -v `pwd`:/host aquasec/kube-bench:latest install

### Run with sudo (the results are different)
$ sudo ./kube-bench
$ sudo ./kube-bench --json
$ sudo ./kube-bench master --json
$ sudo ./kube-bench node --json

----------



# Kube-hunter
https://github.com/aquasecurity/kube-hunter
kube-hunter hunts for security weaknesses in Kubernetes clusters. The tool was developed to increase awareness and visibility for security issues in Kubernetes environments. You should NOT run kube-hunter on a Kubernetes cluster that you don't own!

## Test it within the host?
sudo docker run -it --rm --network host aquasec/kube-hunter

## Scanning the Master Node
docker run --rm aquasec/kube-hunter --remote 192.168.33.10

## Scanning the Worker Node
docker run --rm aquasec/kube-hunter --remote 192.168.33.20

$ docker run --rm aquasec/kube-hunter --remote 192.168.33.10 --report=json

----
# KubiScan

## Prepare the Container
$ sudo docker run -it --rm -e CONF_PATH=~/.kube/config -v /:/tmp cyberark/kubiscan

> # kubiscan --all






----


Running via Kubernetes

## On Master ???

$ kubectl run --rm -i -t kube-bench-master --image=aquasec/kube-bench:latest --restart=Never --overrides="{ \"apiVersion\": \"v1\", \"spec\": { \"hostPID\": true, \"nodeSelector\": { \"node-role.kubernetes.io/master\": \"\" }, \"tolerations\": [ { \"key\": \"node-role.kubernetes.io/master\", \"operator\": \"Exists\", \"effect\": \"NoSchedule\" } ] } }" -- master -c 1.4.3 --version 1.11 -v 5

## On Worker Node ????

$ kubectl label node k8s-node-1 node-role.kubernetes.io/worker=worker

$ kubectl run --rm -i -t kube-bench-node1 --image=aquasec/kube-bench:latest --restart=Never --overrides="{ \"apiVersion\": \"v1\", \"spec\": { \"hostPID\": true, \"nodeSelector\": { \"node-role.kubernetes.io/worker\": \"\" }, \"tolerations\": [ { \"key\": \"node-role.kubernetes.io/worker\", \"operator\": \"Exists\", \"effect\": \"NoSchedule\" } ] } }" -- node -c 1.4.3 --version 1.11 -v 5



## This command installs kube-bench locally
$ sudo docker run --rm -v `pwd`:/host aquasec/kube-bench:latest install

### Run with sudo (the results are different)
$ sudo ./kube-bench
$ sudo ./kube-bench --json
$ sudo ./kube-bench master --json
$ sudo ./kube-bench node --json


$ sudo ./kube-bench master --pgsql

export KUBE_BENCH_PGSQL_HOST=192.168.33.30
export KUBE_BENCH_PGSQL_USER=superset
export KUBE_BENCH_PGSQL_DBNAME=superset
export KUBE_BENCH_PGSQL_SSLMODE=False
export KUBE_BENCH_PGSQL_PASSWORD=superset







docker run --pid=host -v /etc:/etc:ro -v /var:/var:ro -t aquasec/kube-bench:latest [master|node] --version 1.13






kubectl run --rm -i -t kube-bench-node --image=aquasec/kube-bench:latest --restart=Never --overrides="{ \"apiVersion\": \"v1\", \"spec\": { \"hostPID\": true } }" -- node --version 1.11


kubectl run --rm -i -t kube-bench-node --image=aquasec/kube-bench:latest --restart=Never --overrides="{ \"apiVersion\": \"v1\", \"spec\": { \"hostPID\": true } }" -- node --version 1.17