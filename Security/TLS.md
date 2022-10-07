# **TLS Deep Dive**

The following article goes over the basic details of how TLS works.

## Contents
- [SSL vs LS](#SSL-vs-TLS)
- [SSL](#SSL)
- [TLS](#TLS)
- [SSL/TLS protect data in three ways](#SSL/TLS-protect-data-in-three-ways)
- [Anti-Replay and Non-Repudiation](#Anti-Replay-and-Non-Repudiation)
- [Key Players](#Key-Players)

---

## **SSL vs TLS**

SSL/TLS are secure communication protocols that helps protect data that goes over the Internet. SSL and TLS create a secure, protected tunnel accross the Internet.

## **SSL**

- Secure Sockets Layer.  
- Created by Netscape in 1994.

## **TLS**

- Transport Layer Security.  
- SSL was handed to IETF in 1999 renaming the protocol to TLS.  

> **Note**: These 2 terms are sometimes used interchangeably; however, they are not the exact same thing; they are diffferent versions of the protocol. TLS was built based on SSL, providing improvements to the protocol. It was renamed when it was handed over to the IETF.


---


## **SSL/TLS protect data in three ways**

- **Confidentiality**: Data is only accessible by the intended Client and Server. - **Encryption**
- **Integrity**: Detects if data is modified in transit. - **Hashing**
- **Authentication**: Client/Server are indeed who they say they are. - **PKI**

## **Anti-Replay and Non-Repudiation**

- **Anti-Replay**: make a copy of the message and send it back to the server to potentially repeat the action/transaction to either optain data or make modifications. This is solved by adding a sequence number to evey message sent by SSL/TLS. The server check if it has already received the message based on teh sequence number.
- **Non-Repudiation**: the dictionary definition is to refuse to have anything to do with. With Non-Repudiation, the sender cannot deny sending a message. No additional action need to be taken to enable Non-Repudiation, it is built as par of Integrity and Authentication.

## **Key Players**

When working with SSL/TLS, three key players are involved:

- Client
- Server
- Certificate Authority (CA)

> **Note**: In this article we use bowser to refer to a client and Web Server to refer to a server, understanding that these are only examples as there are other devices/software that can be both a client and a server.  


**Client**  

- It initiates the TLS handshake.
- Web Browser (normally).
- Optionally authenticated (rare).


 **Server**  

- It receives the TLS handshke.  
- Web Server (normally).  
- Always authenticated.
    - Providing a certificate.

**Certificate Auhtority (CA)**

- Entity that issues certificates.
- Trusted by both client and Server.
- Provides Trust Anchor
    - If we trust the CA, we trust what the CA trusts.
- Main CAs as of today
    - IdenTrust
        - Includes
            - Let's Encrypt
    - DigiCert
        - Includes
            - GeoTrust
            - Verisign
            - Thawte
    - Sectigo
    - GoDaddy
    - GlobalSign


> **Reference**: https://w3techs.com/technologies/overview/ssl_certificate

---

## **TLS/SSL Versions**

Many versions of SSL/TLS have existed over the years. As tehcnology evolves, the protocol has evolved. As of today, SSL has been deprecated and only TLS should be used.

![TLS Versions](https://github.com/anmontero/TechDocumentation/blob/main/Security/Images/TLSVersions.png)
> **TLS Versions**: pracnet.net | practical-tls



