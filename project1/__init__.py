import os
import sys
os_file = input("")
fos_file_w = os_file.open("wb")
ipl_file = input("")

with open("ipl.img", "wb") as f:
    f.write(bufbin)
