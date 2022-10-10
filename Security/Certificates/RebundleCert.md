# **Rebundle a Certificate using Windows**

1. Open **Manage user certificates**.
2. Open the proper certificate location Folder.
3. Doble click on the certificate. A Certificate window opens.
4. Click Details > Copy to File... > Next > Select No > Next > Base-64 enconded > Next 
5. Select the destination Folder and File name
6. Click Next > Finish
7. On the same Certificate window > Certification Path > Click on the Intermediate certificate > View Certificate
8. A new Certificate window open for the intermediate cert
9. Repeat steps 4 - 6. Make sure to name the certificate so you knwo this is the intermeduate. For example: myintermediatecertificate.cer.
    a. Make sure to use a proper naming in case the cahin has more than 1 intermediate certificate.
10. Open a text editor (such as notepad, notepad++) and paste the entire body of each certificate into one text file in the following order:
    - The Primary/Leaf Certificate.
    - The Intermediate Certificate(s).
    - The Root Certificate.
    Make sure to include the beginning and end tags on each certificate. The result should look like this:
 ```
        -----BEGIN CERTIFICATE-----
            (Leaf certificate)
        -----END CERTIFICATE-----
        -----BEGIN CERTIFICATE-----
            (Intermediate certificate)
        -----END CERTIFICATE-----
        -----BEGIN CERTIFICATE-----
            (Root certificate)
        -----END CERTIFICATE-----
```

> Note: Add as many intermediate certificates in the right order as needed.

11. Save the file with extension .cer.

You now have a properly bundled certificate.