# TO-DO list
## Information
This document is used as a list of TO-DOs and other plans.

 [X] _IN DEVELOPMENT_ +++Implement the login panel.
  ^       ^            ^           ^
  |       |            |           |
  |       |            | Description of the plan.
  |       | If the description has three plus symbols (`+`), it is prioritized.
  |      Must be _On Hold_, _In Development_, or _Finished_.
  |
  ``X`` if the feature is done.





## General
+ [ ] _On Hold_ More logging verbosity.
+ [ ] _On Hold_ Module logging.
+ [X] _Finished_ Check for file integrity on boot.
+ [X] _Finished_ +++User can include arbitrary code when generating new module.
+ [X] _Finished_ +++When checking integrity of files, what if the file was not found?
+ [X] _Finished_ +++Configuration Files (files to exclude in file integrity test, default softwares to call, etc.)
+ [ ] _On Hold_ Web Interface.
+ [ ] _On Hold_ Web Interface's security mechanisms.

## Framework Commands
+ [ ] _On Hold_ Use subprocess on ``run`` command because os.system() is deprecated.
+ [ ] _On Hold_ Built-In Notepad.
+ [ ] _On Hold_ Module Manager (Included in `module` command.)
+ [ ] _On Hold_ Program and System Status / Information
+ [ ] _In Development_ Configuration File Editor.

## Framework Modules
+ 1.Reconnaissance Tools
    - [X] _Finished_ ReconMe (Web Reconnaissance Tool)
        * [X] More stable CMS detection.
        * [X] Continue to geolocation feature.
        * [X] Fix grab_banners.
    - [ ] _On Hold_ IPCalc (IP Calculator)

+ 2.Scanning Tools
    - [ ] _On Hold_ ArcháriosScanner
    - [ ] _On Hold_ Sensitive File Detector
    - [ ] _On Hold_ NetScan (Like Nmap)
    - [ ] _On Hold_ SimpleWP (WordPress Scanner and Backup Grabber)

+ 3.Vulnerability Analysis Tools
    - [ ] _In Development_ ArcháriosFlooder (DoS Tool)
        * [X] Validation of options.
        * [X] Default Attack
        * [X] ARP Attack
        * [X] DHCP Attack
        * [ ] Web Attack
        * [ ] +++DHCP error
    - [ ] _On Hold_ WPEnum (WordPress Username Enumerator)
    - [ ] _On Hold_ Cross-Site Scripter (XSS Vulnerability Analysis Tool)

+ 4.Database Assessment Tools
    - [ ] _On Hold_ SQLiScan (SQL Injection Vulnerability Scanner)

+ 5.Password Attacks
    - [ ] _In Development_ Hypothesis (Wordlist generator)
    - [ ] _On Hold_ CipherCracker (Encryption, Decryption, and Cracking Tool; Cipher Identifier)
    - [ ] _On Hold_ DefaultPass (Gather default credentials using various sources.)
    - [ ] _On Hold_ RARCrack (RAR Archive password cracker)

+ 6.Wireless Auditing Tools
    - [ ] _On Hold_ Kick 'Em (Kick devices out of the network.)
    - [ ] _On Hold_ WiCrack (WiFi Cracking Tool)
    - [ ] _On Hold_ Bluetooth Predator (Bluetooth Attacks)

+ 8.Exploitation Tools
    - [ ] _On Hold_ ShadowSploit
    - [ ] _On Hold_ SuggestMeExploit (Exploit Suggesting Tool using various sources.)

+ 9.Post-Exploitation Tools
    - [ ] _On Hold_ ArchaRAT (Remote Administration Tool)

+ 12.Reporting Tools
    - [ ] _On Hold_ Panalyze (Password Analyzer)
    - [ ] _On Hold_ Dtctv (Server/Client File Repository for Investigating cyber attacks.)

+ 13.Social Engineering Tools
    - [ ] _On Hold_ DarkFish (HTTP server for phishing)

+ 14.System Services
    - [ ] _On Hold_ Deception (HTTP, FTP, SMTP, Telnet, SSH, and SNMP honeypot)
    - [ ] _On Hold_ WebExpose
    - [ ] _On Hold_ SimpleIM_Server (Chat server that uses raw sockets and actual IP for connection)

+ 15.Others
    - [ ] _On Hold_ SimpleIM (SimpleIM client)
