# Clair

## Terminal 1

### Starting Clair 

> $ docker-compose up

## Terminal 2

### Building the docker image

> $ cd clair-scanner

> $ docker build -t clair_scanner .

### Running a Scan

#### Exporting some variables

1. Defining the image to be analyzed (**example**)

> $ IMAGE_TO_ANALYZE=node:12-buster

> $ echo $IMAGE_TO_ANALYZE
  
2. Identifying the Clair Scanner IP Address

> $ CLAIR_SCANNER_IP_ADDRESS=**enter-your-local-ip-address-here"**

> $ echo $CLAIR_SCANNER_IP_ADDRESS

3. Pulling the image to analyze

> $ docker pull $IMAGE_TO_ANALYZE

4. Running the scan (**The report will be available on /tmp/clair_report.json**). **Please notice the network name must be the same than the one obtained from `docker network ls`**.

> $ docker run -it --rm -p 9279:9279 -v /var/run/docker.sock:/var/run/docker.sock -v /tmp/:/tmp/ --privileged=true **--network=clair_clair_nw** --name=clair_scanner clair_scanner --clair=http://clair_api:6060 --ip=$CLAIR_SCANNER_IP_ADDRESS --report=/tmp/clair_report.json $IMAGE_TO_ANALYZE

5. Removing the analyzed image (**optional to clean-up your system**)

> $ docker rmi $IMAGE_TO_ANALYZE