from numpy.random import seed
from numpy.random import randint
import pyfiglet
import time

list1 = ["","","Generating matches","Cracking password matches","Brute Forcing...","hgdasgadg1313gf1h","yfewtr63rt36y6","3tr6trg6tfg6wrt","h7xewyf7y47fy7efye4","matching failing...","ugd674dgw67gd","huehuwhf43f","hf4hff48wfh4fef4e","Match Confirmimng...""Setting Failed...""Retrying", "\n \n \n 08/22/2021  02:21 AM    <DIR>          . \n 08/22/2021  02:21 AM    <DIR>          .. \n 08/22/2021  02:20 AM    <DIR>          .android \n 01/10/2021  11:35 PM    <DIR>          .AndroidStudio3.1 \n 09/16/2021  02:51 PM                99 .bash_history \n 08/22/2021  02:20 AM    <DIR>          .BigNox \n 01/10/2021  01:14 AM    <DIR>          .eclipse \n 08/21/2021  11:01 PM               191 .gitconfig \n 08/21/2021  07:58 PM    <DIR>          .matplotlib \n 01/30/2021  12:47 PM    <DIR>          .nbi \n 04/24/2021  09:59 PM    <DIR>          .nvidia-omniverse \n 01/20/2021  05:48 PM    <DIR>          .p2 \n 08/15/2021  12:27 AM               200 .packettracer \n 01/09/2021  06:37 PM    <DIR>          .thumbnails \n 09/13/2021  12:16 AM    <DIR>          .VirtualBox \n 12/02/2020  12:47 AM    <DIR>          3D Objects \n 01/12/2021  12:28 PM    <DIR>          ansel \n 08/15/2021  12:28 AM    <DIR>          Cisco Packet Tracer 8.0.1 \n 12/02/2020  12:47 AM    <DIR>          Contacts \n 04/24/2021  09:02 PM    <DIR>          Creative Cloud Files \n 08/22/2021  02:21 AM               297 d4ac4633ebd6440fa397b84f1bc94a3c.7z \n 09/16/2021  07:32 PM    <DIR>          Desktop \n", "\n \n 08/22/2021  02:21 AM    <DIR>          . \n 08/22/2021  02:21 AM    <DIR>          .. \n 08/22/2021  02:20 AM    <DIR>          .android \n 01/10/2021  11:35 PM    <DIR>          .AndroidStudio3.1 \n 09/16/2021  02:51 PM                99 .bash_history \n 08/22/2021  02:20 AM    <DIR>          .BigNox \n 01/10/2021  01:14 AM    <DIR>          .eclipse \n 08/21/2021  11:01 PM               191 .gitconfig \n 08/21/2021  07:58 PM    <DIR>          .matplotlib \n 01/30/2021  12:47 PM    <DIR>          .nbi \n 04/24/2021  09:59 PM    <DIR>          .nvidia-omniverse \n 01/20/2021  05:48 PM    <DIR>          .p2 \n 08/15/2021  12:27 AM               200 .packettracer \n 01/09/2021  06:37 PM    <DIR>          .thumbnails \n 09/13/2021  12:16 AM    <DIR>          .VirtualBox \n 12/02/2020  12:47 AM    <DIR>          3D Objects \n 01/12/2021  12:28 PM    <DIR>          ansel \n 08/15/2021  12:28 AM    <DIR>          Cisco Packet Tracer 8.0.1 \n 12/02/2020  12:47 AM    <DIR>          Contacts \n 04/24/2021  09:02 PM    <DIR>          Creative Cloud Files \n 08/22/2021  02:21 AM               297 d4ac4633ebd6440fa397b84f1bc94a3c.7z \n 09/16/2021  07:32 PM    <DIR>          Desktop \n"]
list2 = ["Encryption Matching...","Targeting...","Land891278731","Matches Detected","Decrypting","Decryption Algorithm Detecting","Process Completing","Decrypting","\n \n 08/22/2021  02:21 AM    <DIR>          . \n 08/22/2021  02:21 AM    <DIR>          .. \n 08/22/2021  02:20 AM    <DIR>          .android \n 01/10/2021  11:35 PM    <DIR>          .AndroidStudio3.1 \n 09/16/2021  02:51 PM                99 .bash_history \n 08/22/2021  02:20 AM    <DIR>          .BigNox \n 01/10/2021  01:14 AM    <DIR>          .eclipse \n 08/21/2021  11:01 PM               191 .gitconfig \n 08/21/2021  07:58 PM    <DIR>          .matplotlib \n 01/30/2021  12:47 PM    <DIR>          .nbi \n 04/24/2021  09:59 PM    <DIR>          .nvidia-omniverse \n 01/20/2021  05:48 PM    <DIR>          .p2 \n 08/15/2021  12:27 AM               200 .packettracer \n 01/09/2021  06:37 PM    <DIR>          .thumbnails \n 09/13/2021  12:16 AM    <DIR>          .VirtualBox \n 12/02/2020  12:47 AM    <DIR>          3D Objects \n 01/12/2021  12:28 PM    <DIR>          ansel \n 08/15/2021  12:28 AM    <DIR>          Cisco Packet Tracer 8.0.1 \n 12/02/2020  12:47 AM    <DIR>          Contacts \n 04/24/2021  09:02 PM    <DIR>          Creative Cloud Files \n 08/22/2021  02:21 AM               297 d4ac4633ebd6440fa397b84f1bc94a3c.7z \n 09/16/2021  07:32 PM    <DIR>          Desktop \n","\n \n 08/22/2021  02:21 AM    <DIR>          . \n 08/22/2021  02:21 AM    <DIR>          .. \n 08/22/2021  02:20 AM    <DIR>          .android \n 01/10/2021  11:35 PM    <DIR>          .AndroidStudio3.1 \n 09/16/2021  02:51 PM                99 .bash_history \n 08/22/2021  02:20 AM    <DIR>          .BigNox \n 01/10/2021  01:14 AM    <DIR>          .eclipse \n 08/21/2021  11:01 PM               191 .gitconfig \n 08/21/2021  07:58 PM    <DIR>          .matplotlib \n 01/30/2021  12:47 PM    <DIR>          .nbi \n 04/24/2021  09:59 PM    <DIR>          .nvidia-omniverse \n 01/20/2021  05:48 PM    <DIR>          .p2 \n 08/15/2021  12:27 AM               200 .packettracer \n 01/09/2021  06:37 PM    <DIR>          .thumbnails \n 09/13/2021  12:16 AM    <DIR>          .VirtualBox \n 12/02/2020  12:47 AM    <DIR>          3D Objects \n 01/12/2021  12:28 PM    <DIR>          ansel \n 08/15/2021  12:28 AM    <DIR>          Cisco Packet Tracer 8.0.1 \n 12/02/2020  12:47 AM    <DIR>          Contacts \n 04/24/2021  09:02 PM    <DIR>          Creative Cloud Files \n 08/22/2021  02:21 AM               297 d4ac4633ebd6440fa397b84f1bc94a3c.7z \n 09/16/2021  07:32 PM    <DIR>          Desktop \n"]
list3 = ["Launching package 12pi21","","","Launching package ns37dhe","Launching package 23","Executing 101","Processes running...","Malware Running...","Backdoors being installed","Settings Changed","Malwears Running...","\n \n 08/22/2021  02:21 AM    <DIR>          . \n 08/22/2021  02:21 AM    <DIR>          .. \n 08/22/2021  02:20 AM    <DIR>          .android \n 01/10/2021  11:35 PM    <DIR>          .AndroidStudio3.1 \n 09/16/2021  02:51 PM                99 .bash_history \n 08/22/2021  02:20 AM    <DIR>          .BigNox \n 01/10/2021  01:14 AM    <DIR>          .eclipse \n 08/21/2021  11:01 PM               191 .gitconfig \n 08/21/2021  07:58 PM    <DIR>          .matplotlib \n 01/30/2021  12:47 PM    <DIR>          .nbi \n 04/24/2021  09:59 PM    <DIR>          .nvidia-omniverse \n 01/20/2021  05:48 PM    <DIR>          .p2 \n 08/15/2021  12:27 AM               200 .packettracer \n 01/09/2021  06:37 PM    <DIR>          .thumbnails \n 09/13/2021  12:16 AM    <DIR>          .VirtualBox \n 12/02/2020  12:47 AM    <DIR>          3D Objects \n 01/12/2021  12:28 PM    <DIR>          ansel \n 08/15/2021  12:28 AM    <DIR>          Cisco Packet Tracer 8.0.1 \n 12/02/2020  12:47 AM    <DIR>          Contacts \n 04/24/2021  09:02 PM    <DIR>          Creative Cloud Files \n 08/22/2021  02:21 AM               297 d4ac4633ebd6440fa397b84f1bc94a3c.7z \n 09/16/2021  07:32 PM    <DIR>          Desktop \n","\n \n 08/22/2021  02:21 AM    <DIR>          . \n 08/22/2021  02:21 AM    <DIR>          .. \n 08/22/2021  02:20 AM    <DIR>          .android \n 01/10/2021  11:35 PM    <DIR>          .AndroidStudio3.1 \n 09/16/2021  02:51 PM                99 .bash_history \n 08/22/2021  02:20 AM    <DIR>          .BigNox \n 01/10/2021  01:14 AM    <DIR>          .eclipse \n 08/21/2021  11:01 PM               191 .gitconfig \n 08/21/2021  07:58 PM    <DIR>          .matplotlib \n 01/30/2021  12:47 PM    <DIR>          .nbi \n 04/24/2021  09:59 PM    <DIR>          .nvidia-omniverse \n 01/20/2021  05:48 PM    <DIR>          .p2 \n 08/15/2021  12:27 AM               200 .packettracer \n 01/09/2021  06:37 PM    <DIR>          .thumbnails \n 09/13/2021  12:16 AM    <DIR>          .VirtualBox \n 12/02/2020  12:47 AM    <DIR>          3D Objects \n 01/12/2021  12:28 PM    <DIR>          ansel \n 08/15/2021  12:28 AM    <DIR>          Cisco Packet Tracer 8.0.1 \n 12/02/2020  12:47 AM    <DIR>          Contacts \n 04/24/2021  09:02 PM    <DIR>          Creative Cloud Files \n 08/22/2021  02:21 AM               297 d4ac4633ebd6440fa397b84f1bc94a3c.7z \n 09/16/2021  07:32 PM    <DIR>          Desktop \n"]
list4 = ["Trying...","Trying","Continuing.","Matching...","","","Retrying.......","\n \n 08/22/2021  02:21 AM    <DIR>          . \n 08/22/2021  02:21 AM    <DIR>          .. \n 08/22/2021  02:20 AM    <DIR>          .android \n 01/10/2021  11:35 PM    <DIR>          .AndroidStudio3.1 \n 09/16/2021  02:51 PM                99 .bash_history \n 08/22/2021  02:20 AM    <DIR>          .BigNox \n 01/10/2021  01:14 AM    <DIR>          .eclipse \n 08/21/2021  11:01 PM               191 .gitconfig \n 08/21/2021  07:58 PM    <DIR>          .matplotlib \n 01/30/2021  12:47 PM    <DIR>          .nbi \n 04/24/2021  09:59 PM    <DIR>          .nvidia-omniverse \n 01/20/2021  05:48 PM    <DIR>          .p2 \n 08/15/2021  12:27 AM               200 .packettracer \n 01/09/2021  06:37 PM    <DIR>          .thumbnails \n 09/13/2021  12:16 AM    <DIR>          .VirtualBox \n 12/02/2020  12:47 AM    <DIR>          3D Objects \n 01/12/2021  12:28 PM    <DIR>          ansel \n 08/15/2021  12:28 AM    <DIR>          Cisco Packet Tracer 8.0.1 \n 12/02/2020  12:47 AM    <DIR>          Contacts \n 04/24/2021  09:02 PM    <DIR>          Creative Cloud Files \n 08/22/2021  02:21 AM               297 d4ac4633ebd6440fa397b84f1bc94a3c.7z \n 09/16/2021  07:32 PM    <DIR>          Desktop \n"]
list1.pop(-1)
list1.pop(-1)
list1.append("\n \n 08/22/2021  02:21 AM    <DIR>          . \n 08/22/2021  02:21 AM    <DIR>          .. \n 08/22/2021  02:20 AM    <DIR>          .android \n 01/10/2021  11:35 PM    <DIR>          .AndroidStudio3.1 \n")
list1.append("08/18/2021  09:49 PM    <DIR>          Searches \n 01/09/2021  07:20 PM                53 useruid.ini \n 09/16/2021  09:31 PM    <DIR>          Videos \n 09/01/2021  12:35 AM    <DIR>          VirtualBox VMs \n 08/22/2021  02:20 AM    <DIR>          vmlogs \n                       9 File(s)          1,002 bytes \n                           33 Dir(s)  120,614,694,912 bytes free \n")
list1.append("\n 04/24/2021  09:59 PM    <DIR>          .nvidia-omniverse \n 01/20/2021  05:48 PM    <DIR>          .p2 \n 08/15/2021  12:27 AM               200 .packettracer \n")
list2.pop(-1)
list2.pop(-1)
list2.append(("08/18/2021  09:49 PM    <DIR>          Searches \n 01/09/2021  07:20 PM                53 useruid.ini \n 09/16/2021  09:31 PM    <DIR>          Videos \n 09/01/2021  12:35 AM    <DIR>          VirtualBox VMs \n 08/22/2021  02:20 AM    <DIR>          vmlogs \n                       9 File(s)          1,002 bytes \n                           33 Dir(s)  120,614,694,912 bytes free \n"))
list2.append("\n 04/24/2021  09:59 PM    <DIR>          .nvidia-omniverse \n 01/20/2021  05:48 PM    <DIR>          .p2 \n 08/15/2021  12:27 AM               200 .packettracer \n")
list3.pop(-1)
list3.append("08/18/2021  09:49 PM    <DIR>          Searches \n 01/09/2021  07:20 PM                53 useruid.ini \n 09/16/2021  09:31 PM    <DIR>          Videos \n 09/01/2021  12:35 AM    <DIR>          VirtualBox VMs \n 08/22/2021  02:20 AM    <DIR>          vmlogs \n                       9 File(s)          1,002 bytes \n                           33 Dir(s)  120,614,694,912 bytes free \n")
list4.pop(-1)
list4.append("08/18/2021  09:49 PM    <DIR>          Searches \n 01/09/2021  07:20 PM                53 useruid.ini \n 09/16/2021  09:31 PM    <DIR>          Videos \n 09/01/2021  12:35 AM    <DIR>          VirtualBox VMs \n 08/22/2021  02:20 AM    <DIR>          vmlogs \n                       9 File(s)          1,002 bytes \n                           33 Dir(s)  120,614,694,912 bytes free \n")
ascii_banner = pyfiglet.figlet_format("Exploit Engineer Toolkit")
print(ascii_banner)

while True:

    val = input("./Sysadmin/Exploiter/.. Enter :")

    if val == "1":
        seed(1)
        for i in range(300):
            nss = randint(0, len(list3))
            print(list3[nss])
            time.sleep(0.06)
        print("Malware Execution Complete... Attack Succesful -+-+-+")
        ascii_banner = pyfiglet.figlet_format("DeDuxxx1 - Malware Executed")
        print(ascii_banner)

    elif val == "2":
        seed(1)
        for i in range(300):
            nss = randint(0, len(list2))
            print(list2[nss])
            time.sleep(0.07)
        print("Decryption Succesfully Complete............... -+-+-+ \n \n")
        ascii_banner = pyfiglet.figlet_format("Kanlan Decrypter - Complete")
        print(ascii_banner)

    elif val == "3":
        seed(1)
        for i in range(300):
            nss = randint(0, len(list1))
            print(list1[nss])
            time.sleep(0.05)
        print("Malware Execution Complete... Attack Succesful -+-+-+")
        ascii_banner = pyfiglet.figlet_format("SHA Matcher - COMPLETED")
        print(ascii_banner)

    else:
        seed(1)
        for i in range(300):
            nss = randint(0, len(list4))
            print(list4[nss])
            time.sleep(0.0455)
        print("Malware Execution Complete... Attack Succesful -+-+-+")
        print("System failed...")
        print("System failed...")
        print("System failed...")
