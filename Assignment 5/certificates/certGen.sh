#!/bin/bash
# Generate CA key
openssl genrsa -out ca.key 2048
echo CA KEY GENERATED
# Generate Server key
openssl genrsa -out server.key 2048
echo SERVER KEY GENERATED
# Self-sign CA certificate
openssl req -new -x509 -days 3650 -key ca.key -out ca.crt
echo CA CERTIFICATE GENERATED
# Generate Server certificate request
openssl req -new -key server.key -out server.csr
echo SERVER CSR GENERATED
# Sign Server's certificate request
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 1024
echo SERVER CERTIFICATE GENERATED
