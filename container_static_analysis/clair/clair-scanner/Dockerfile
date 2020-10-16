FROM golang:1.14.2-buster

RUN curl -vv https://raw.githubusercontent.com/golang/dep/master/install.sh  | sh

RUN git clone https://github.com/arminc/clair-scanner.git /go/src/clair

WORKDIR /go/src/clair

RUN make ensure; make build

EXPOSE 9279

ENTRYPOINT ["./clair-scanner"]