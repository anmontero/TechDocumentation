# **Overview of the SSL Process**

## **Terms**

### **Certificate Authority**

- CA has the Public key and a Private Key.
- CA has a self-Signed Certificate.

### **Server**

- Wants to acquire a certificate.
- Generates a Public key and a private Key.
- Generates a Certificate Signing request (CSR)
   - CSR contains the Server's Public Key.
   - CSR is signed by the Server's Private Key.
- The server gives the signed CSR to the CA.
- The CA inspects and validates the information in the CSR.
- The CA creates a Certificate using the information from the CSR.
- The CA signs the certificate using the CA's Private Key.
- The CA gives the certificate to the server.
- The server can then provide the certificate to prove its identity.

### **What is in a certificate?**

The **x.509** is a Standard which outlines the content of certificates.

### **Three sections of a Certificate**:

- Certificate Data.
   - Version.
   - Serial number.
   - Signature algorithm.
   - Validity.
   - Subject and Issuer.
   - Public Key.
   - Extensions.
- Signature Algorithm.
- Signature.

#### **Certificate Data**

**Version**

- Version of the x509 specification.

**Serial Number**

- Uniquely identifies a certificate issued by a given CA.
- Used to lookup the validity of a certificate.
   - Request is made to the CA which issued the Certificate by Serial Number.
      - CRL - Certificate Revocation List.
      - OCSP - Online Certificate Status Protocol.

 **Signature Algorithm**

 - Algorithms used to generate the certificate's signature:
    - Hashing algorithm.
    - Asymmetric Encryption algorithm which generates the keys.

**Validity**

- Duration a Certificate is valid for.
- Specifies with two values:
   - Not before.
   - Not After.

**Subject and Issuer**

**Subject**

- What the certificate is trying to Identify.

**Issuer**

- The CA that issued and signed the Certificate.


**Extensions**

- Optional Fields that add features and restrictions to Certificates.
- Added in x509 v3.

**Useful Openssl Commands***

- Get the certiricate data: openssl s_client -connect domain:port
- View cert data (after saving the base64 data to a file): openssl x509 -in cert_file_path -text -noout
  
### **Certificate Extensions**

- Requires x509 v3 certificates.
- Optional field that adds features and restrictions to Certificates.

#### **Common extensions**

##### **Key usage, Extended Key Usage**

- Sets uses/limits for certificate keys:
   - Encrypt Data.
   - Establish Symmetric Keys.
   - Verify Certificate Signature (Sign certificates).
   - Verify Signatures.
   - Verify CRL Signatures.
 
###### **Key Usage**:

- Limits by Purpose.

###### **Extended Key Usage**:

- Limits by Protocol and/or Role.
 

##### **Basic Constraints**

- Determines whther the Subject is:
  - A Certificate Authority.
  - End-Entity (google.com, etc.)
  - CA Certificates **can** be Issuers.
  - E.E certs **cannot** be Issuers.


##### **Name Constraints**

- Limits signing to a specific domain.


##### **Subject Alternative Name**

- Allows one certificate to protect multiple domains.

##### **Authority Information Access (AIA)**

- Provides information from the ca.
- Link to download the Issuer Cert.
- URI for the OCSP Responder.

### **What is a Private Key?**

All TLS certificates require a private key to work. The private key is a separate file that’s used in the encryption/decryption of data sent between your server and the connecting clients. A private key is created by you — the certificate owner — when you request your certificate with a Certificate Signing Request (CSR). The certificate authority (CA) providing your certificate (such as DigiCert) does not create or have your private key.

> **Reference**: https://www.digicert.com/blog/where-is-your-private-key

### **What is in a CSR?**

A Certificate Signing Request (CSR) is a block of encoded text that is given to a Certificate Authority when applying for an SSL/TLS certificate. It contains information that will be included in your certificate such as your Organization Name, Common Name (domain name), Locality, and Country. It also includes the public key that will be included in the certificate. The private key is paired with this public key and should be kept secure and not included in the CSR.

There are three sections of a certificate Signing Request:

- Certificate Request Information.
- Signature Algorithm.
- Signature.
