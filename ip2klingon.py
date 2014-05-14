#!/usr/bin/env python3
import sys
import os

ones = ["pagh", "wa’", "cha’", "wej", "loS", "vagh", "jav", "Soch", "chrogh", "Hut"]
ten = "maH"
hundred = "vatlh" 

def number2klingon(numberS):
    number = int(numberS)
    if number > 255:
        raise RuntimeError("Not a valid IPv4 address")
    if number < 10:
        return ones[number]
    elif number < 100:
        t = int(number / 10)
        if number % 10 != 0:
            return ones[t] + ten + " " + number2klingon(number % 10)
        else:
            return ones[t] + ten
    else:
        h = int(number / 100)
        if number % 100 != 0:
            return ones[h] + hundred + " " + number2klingon(number % 100)
        else:
            return ones[h] + hundred

        
try:
    if len(sys.argv) != 3:
        raise RuntimeError("The only honorable amount of arguments is 2!")
    ip = sys.argv[1]
    out = sys.argv[2]
    klingonip = " . ".join([number2klingon(n) for n in ip.split(".")])
    imagemap = ["%s.png" % c if c != '.' else "_.png" for c in ip]
    os.system("montage -geometry 128x128-5+0 -tile x1 %s %s" % (" ".join(imagemap), out))
    os.system("convert -font Inconsolata -pointsize 32 %s label:\"%s\" -gravity Center -append %s" % (out,klingonip, out))
except Exception as e:
    print("{0}".format(e))

