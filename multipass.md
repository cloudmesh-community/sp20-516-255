## E.Multipass.1: Windows 10 Home Installation Steps

Multipass by default does not support Windows 10 Home. You will need to install Virtual Box for using Multipass on Windows 10 Home.

* Download latest version of Virtual Box <https://www.oracle.com/virtualization/technologies/vm/downloads/virtualbox-downloads.html>
* Download latest version of Multipass <https://multipass.run/>
* Start an Admin Powershell and execute: multipass set local.driver=virtualbox.
*reboot

## E.Multipass.5:  Examples for ﬁnd 

prafu@DESKTOP-HFNEGFF MINGW64 ~

$ multipass find

Image                   Aliases           Version          Description

16.04                   xenial            20200129         Ubuntu 16.04 LTS

18.04                   bionic,lts        20200129.1       Ubuntu 18.04 LTS
