
import csv
import nfc
from nfc.clf import RemoteTarget


# THIS IS THE READER PARAMETER VARIABLE!

rfid_reader = "tty"


# initialize nfc scanner
clf = nfc.ContactlessFrontend()
assert clf.open(rfid_reader) is True 
target = clf.sense(RemoteTarget('106A'), RemoteTarget('106B'), RemoteTarget('212F'))


tag = clf.connect(rdwr={'on-connect': lambda tag: False})
#print(tag)
scan_num = str(tag)
print(scan_num)

for i in scan_num:
    if i == 'I':
        scan_num = scan_num[scan_num.index(i)+3:]

print(scan_num)

clf.close()