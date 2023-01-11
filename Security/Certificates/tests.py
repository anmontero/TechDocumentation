import os
import subprocess


#os.mkdir("new_folder")



opensslconf = """[ ca ]
default_ca = CA_default
[ CA_default ]
certs          = certs               # Where the issued certs are kept
crl_dir        = crl                 # Where the issued crl are kept
database       = index.txt           # database index file.
new_certs_dir  = newcerts            # default place for new certs.
certificate    = cacert.pem          # The CA certificate
serial         = serial              # The current serial number
crl            = crl.pem             # The current CRL
private_key    = ca.key.pem          # The private key
RANDFILE       = .rnd                # private random number file
nameopt        = default_ca
certopt        = default_ca
policy         = policy_match
default_days   = 365
default_md     = sha256

[ policy_match ]
countryName            = optional
stateOrProvinceName    = optional
organizationName       = optional
organizationalUnitName = optional
commonName             = supplied
emailAddress           = optional

[req]
req_extensions = v3_req
distinguished_name = req_distinguished_name

[req_distinguished_name]

[v3_req]
basicConstraints = CA:TRUE"""

os.chdir("new_folder")
with open("example.txt", "w") as file:
    file.write(opensslconf)


#output = subprocess.run("dir", shell=True, stdout=subprocess.PIPE)
#print(output.stdout.decode())