import os
import subprocess

# save current sirectory in a variable
# this will be used for the leaf certificate creation part

current_directory = os.getcwd()

# Function to create the directories and files
def create_structure(C):
    os.mkdir(C)
    os.chdir(C)
    os.mkdir('certs')
    os.mkdir('crl')
    os.mkdir('newcerts')
    os.mkdir('private')
    os.chdir('..')

    with open(f'{C}/serial', 'w') as f:
        f.write('1000')
    open(f'{C}/index.txt', 'a').close()
    open(f'{C}/index.txt.attr', 'a').close()

    # create openssl config file
    with open(f'{C}/openssl.conf', 'w') as f:
        f.write("""
[ ca ]
default_ca = CA_default
[ CA_default ]
dir            = {C}                     # Where everything is kept
certs          = $dir/certs               # Where the issued certs are kept
crl_dir        = $dir/crl                 # Where the issued crl are kept
database       = $dir/index.txt           # database index file.
new_certs_dir  = $dir/newcerts            # default place for new certs.
certificate    = $dir/cacert.pem          # The CA certificate
serial         = $dir/serial              # The current serial number
crl            = $dir/crl.pem             # The current CRL
private_key    = $dir/private/ca.key.pem  # The private key
RANDFILE       = $dir/.rnd                # private random number file
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
basicConstraints = CA:TRUE
""".format(C=C))

# create root-ca key and certificate
for C in ['root-ca', 'intermediate']:
    create_structure(C)
    
subprocess.run(['openssl', 'genrsa', '-out', 'root-ca/private/ca.key', '2048'])
subprocess.run(['openssl', 'req', '-config', 'root-ca/openssl.conf', '-new', '-x509', '-days', '3650', '-key', 'root-ca/private/ca.key', '-sha256', '-extensions', 'v3_req', '-out', 'root-ca/certs/ca.crt', '-subj', '/CN=Root-ca'])

# create intermediate key and certificate
subprocess.run(['openssl', 'genrsa', '-out', 'intermediate/private/intermediate.key', '2048'])
subprocess.run(['openssl', 'req', '-config', 'intermediate/openssl.conf', '-sha256', '-new', '-key', 'intermediate/private/intermediate.key', '-out', 'intermediate/certs/intermediate.csr', '-subj', '/CN=Interm.'])
subprocess.run(['openssl', 'ca', '-batch', '-config', 'root-ca/openssl.conf', '-keyfile', 'root-ca/private/ca.key', '-cert', 'root-ca/certs/ca.crt', '-extensions', 'v3_req', '-notext', '-md', 'sha256', '-in', 'intermediate/certs/intermediate.csr', '-out', 'intermediate/certs/intermediate.crt'])

# create 'out' directory

os.mkdir('out')
os.chdir('out')
# create certificate for example.com

with open('req.cnf', 'w') as f:
        f.write("""
[req]
distinguished_name = req_distinguished_name
req_extensions = req_ext
prompt = no

[req_distinguished_name]
C   = CR
ST  = San Jose
L   = San Jose
O   = TonyWebtest
OU  = WWW
CN  = 10.6.0.4

[req_ext]
subjectAltName = @alt_names

[alt_names]
DNS.1 = tonywebtest.com
DNS.2 = *.tonywebtest.com
""".format(C=C))

# generate the leaf keyfile
subprocess.run(['openssl', 'genrsa', '-out', 'leaf.key', '2048'])
subprocess.run(['openssl', 'req', '-new', '-key', 'leaf.key', '-out', 'leaf.csr', '-config', 'req.cnf'])
subprocess.run(['openssl', 'x509', '-req', '-days', '365', '-in', 'leaf.csr', '-CA', f'{current_directory}/intermediate/certs/intermediate.crt', '-CAkey', f'{current_directory}/intermediate/private/intermediate.key', '-CAcreateserial', '-out', 'leaf.crt', '-extensions', 'req_ext', '-extfile', 'req.cnf'])


