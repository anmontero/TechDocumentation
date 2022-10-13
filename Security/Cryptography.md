# **Hashing**

### **Definition**

Algorithm which takes an input a message of arbitrry lenght and produces as output a "fingerprint" of the original message. The result of the hashing algorithm is called a **Digest**.

The purpose of the Digest is to compare 2 messages and check if they are the same or different.

Real world Hasing Algotirhms must satisfy 4 requiremtns:

- Infeasible to produce a given digest.
- Impossible to extract the original message.
- Slight changes produce drastic differences.
- The resulting digest is fixed width (length).



### **Collisions**

- Two messages result on identical digests.
- They cannotbe avoided.
    - It is a byproduct of "fixed width digests".

### **Common Hashing Algorithms**

- MD5 - 128 bits.
- SHA/SHA1 - 160 bits
- SHA2 Family
    - SHA-224 - 224 bits
    - SHA-256 - 256 bits
    - SHA-384 - 384 bits
    - SHA-512 - 512 bits

_Examples:_

```
echo -n "hello" | md5sum_
5d41402abc4b2a76b9719d911017c592  -

echo -n "hello" | sha1sum
aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d  -

echo -n "hello" | sha256sum
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824  -

 echo -n "hello" | sha512sum
9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043  -
```

# **Data Integrity**

Hashing is used to provide Integrity.

- The sender sends a Message and a Digest.
- The receiver calculates the Digest  from the received Message
- The Receiver compares both digests.
    - If the digests are identical, the messages was not modified in transit.

### **Hashing problem**

- If there is someone in the middle who captures the message, it can send a different message with a new calculated hash. The receiver will then calculate the digest based on the modified message.

### **Solution**

- Before each party shared the meesage, they shared a mutual secret key.
- The sender combines the message with the key to generate the digest.
- The receiver recalculates the has with his key and message.

This is known as Message Authentication Code (MAC) which provides Integrity (Hashing) and Authentication (key). The sender and receiver must agree on how to combine the message and the key. If the combination is done in a different order, the resulting dihest will be different.

_Example:_

- Combination 1: message + key == 1 digest.
- Combination 2: key + message == different digest.

The industry standard implementation of MAC is known as HMAC. HMAC defines how to use MAC and how combine the mesaage and the key.

---

# **Encryption**

Encryption is used to provide Confidentiality. Only the intended receipient can interpret the Data.

- **Plain Text**: Data before encryptin.
- **Cypher Text**: Data while encrypted.

**Simple Encryption**: Transforms Plaintext into Cypher Text. It does not escale as for it to be secured, I need to figure out a different way to transform the data. If I used the same transformation method for all users, data can be decrypted by other users data was not intended for.

**Key Based Encryption**: Combines industry vetted algorithms with a Secret Key.
- Algorithms are created by experts.
- Secret Keys can be randomly generated.

### **There are two types of Key Based Encryption:**

- Symmetric Encryption
    - Encrypt and Decrypt using the **same** key.
- Asymmetric Encryption
    - Encrypt and Decrypt using **different** keys.
    - Two different keys are mathematically related.
    - What one key encrypts, only the other can decrypt.
        - One key will be made **Public**.
        - Other key will be kept **Private**.


### **List of Encryption Algorithms:**

- Asymmetric Encryption
    - DSA
    - RSA
    - Diffie-Hellman
    - ECDSA
    - ECDH
- Symmetric Encryption
    - DES - 56 bit key
    - RC4 - 128 bit key
    - 3DES - 168 bit key
    - AES - 128,192, or 256 bit keys
    - ChaCha20 - 128 or 256 bit keys

---
# **Public and Private Keys**

Asymmetric Key Pairs can be used used for **Signatures**.

Asymmetric Encryption is used to share a Symmetric key for bulk data encryption. Public and Private keys are used to share a Symmetric key.


### **Hybrid Encryption**

Concept of using both encryption types.

- Asymmetric to facilitate a Key Exchange.
- Secret Key used with Symmetric Encryption for bulk data.

### **Signatures**

Encrypt a message with you private key that can be decrypted only with your associated Public key, proving you are the only person that could have sent the message as you are the only one who has the private key.

---
# **How SSL/TLS uses Cryptography**

![TLS Encryption](https://github.com/anmontero/TechDocumentation/blob/main/Security/Images/HowTLSUSESENCRY.png)

![TLS Encryption1](https://github.com/anmontero/TechDocumentation/blob/main/Security/Images/HowTLSUSESENCRY1.png)