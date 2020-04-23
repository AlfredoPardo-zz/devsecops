# Docker Bench Security

Surprisingly, [docker-bench-security](https://github.com/docker/docker-bench-security.git) outputs a JSON file within the container and doesn't have an option to copy it outside. So these are the steps to obtain the results file from the outside:

1. Cloning the repository

> $ git clone https://github.com/docker/docker-bench-security.git

2. Adding lines to the end at the `docker-bench-security.sh` file

> $ vim docker-bench-security.sh

```console
echo "Copying files to /tmp ..."
cp /usr/local/bin/*.json /tmp
```

3. Building the docker image

> $ docker build --no-cache -t docker-bench-security .

4. Running the Benchmark. **Please notice the output will be mounted from the /tmp folder of the container to your current directory**.

> $ docker run -it --rm --net host --pid host --userns host --cap-add audit_control \
-e DOCKER_CONTENT_TRUST=$DOCKER_CONTENT_TRUST \
-v /etc:/etc:ro \
-v /lib/systemd/system:/lib/systemd/system:ro \
-v /usr/bin/containerd:/usr/bin/containerd:ro \
-v /usr/bin/runc:/usr/bin/runc:ro \
-v /usr/lib/systemd:/usr/lib/systemd:ro \
-v /var/lib:/var/lib:ro \
-v /var/run/docker.sock:/var/run/docker.sock:ro \
-v $PWD:/tmp \
--name docker_bench_security \
--label docker_bench_security \
docker-bench-security