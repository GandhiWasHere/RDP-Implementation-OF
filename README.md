# RDP-Implementation-OF
Creating os fingerprint using RDP.

My main goals:
1) Implement SSL handshake
2) Get the init mcs 
3) get minor and major versions
4) detect os
-----
5) was not enough so i parsed ntlmm challange - got minor, major and build
6) add windowsize for more checks


![image](https://user-images.githubusercontent.com/40568399/137641469-a0100d37-b088-46b0-9575-ce990f649168.png)







Thanks to,
https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rdpbcgr/18a27ef9-6f9a-4501-b000-94b1fe3c2c10
https://www.cyberark.com/resources/threat-research-blog/explain-like-i-m-5-remote-desktop-protocol-rdp
https://github.com/jiansiting/CVE-2019-0708/blob/master/poc.py
https://medium.com/@0x4d31/rdp-client-fingerprinting-9e7ac219f7f4

