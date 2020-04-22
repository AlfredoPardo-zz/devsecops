# Trivy

## Installing it in Ubuntu

These are the commands you have to run for setting it up in Ubuntu:

> $ sudo apt-get install wget apt-transport-https gnupg lsb-release

> $ wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
> $ echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list

> $ sudo apt-get update

> $ sudo apt-get install trivy

## Running a Scan

You can easily obtain a JSON file with the findings running the following command:

> $ trivy -f json -o trivy_results.json <image_name>
