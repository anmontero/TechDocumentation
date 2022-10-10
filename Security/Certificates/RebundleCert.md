# **Rebundle a Certificate using Windows**

1. Open **Manage user certificates**.
2. Naviga to the proper certificate location.
3. Doble click on the certificate. A new window opens.

    ![rebundle1](https://github.com/anmontero/TechDocumentation/blob/main/Security/Images/rebundle1.png)

4. Click **Details** > **Copy to File...** > **Next** > Select **No** > **Next** > **Base-64 enconded** > **Next**

    ![rebundle2](https://github.com/anmontero/TechDocumentation/blob/main/Security/Images/rebundle2.png)

5. Select the destination Folder and File name
6. Click **Next** > **Finish**
7. On the same Certificate window > click **Certification Path** > Click on the Intermediate certificate > **View Certificate**

![rebundle3](https://github.com/anmontero/TechDocumentation/blob/main/Security/Images/rebundle3.png)

8. A new Certificate window opens for the intermediate cert.
9. Repeat steps 4 - 6. Make sure to name the certificate with an easy to identify name so you know this is the intermediate (needed for step 10). For example: myintermediatecertificate.cer.  
    a. Make sure to use a proper naming in case the chain contains more than 1 intermediate certificate.
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

> **Note:** Add as many intermediate certificates in the right order as needed.

11. Save the file with extension .cer.

You now have a properly bundled certificate.