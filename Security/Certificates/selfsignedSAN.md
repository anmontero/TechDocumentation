1. Create a private key and a self-signed certificate for the root CA (Certificate Authority). This will be the top of the certificate chain.

openssl genrsa -out rootCA.key 2048
openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 1024 -out rootCA.pem

2. Create a private key and a certificate signing request (CSR) for the server.

openssl genrsa -out server.key 2048

Config file

[req]
distinguished_name = req_distinguished_name
req_extensions = req_ext
prompt = no

[req_distinguished_name]
C   = IN
ST  = Karnataka
L   = Bengaluru
O   = GoLinuxCloud
OU  = R&D
CN  = ban21.example.com

[req_ext]
subjectAltName = @alt_names

[alt_names]
IP.1 = 10.10.10.13
IP.2 = 10.10.10.14
IP.3 = 10.10.10.17
DNS.1 = centos8-2.example.com
DNS.2 = centos8-3.example.com


Generate the CSR

openssl req -new -key server.key -out server.csr -config server_cert.cnf

Verify CSR SAN

 openssl req -noout -text -in server.csr | grep -A 1 "Subject Alternative Name"


Generate the SAN cert

openssl x509 -req -days 365 -in server.csr -CA /root/tls/certs/cacert.pem -CAkey /root/tls/private/cakey.pem -CAcreateserial -out server.crt -extensions req_ext -extfile server_cert.cnf


Check SAN

openssl x509 -text -noout -in server.crt | grep -A 1 "Subject Alternative Name" 


https://support.citrix.com/article/CTX135602/how-to-create-a-selfsigned-san-certificate-using-openssl-on-citrix-adc-appliance

https://www.golinuxcloud.com/openssl-subject-alternative-name/