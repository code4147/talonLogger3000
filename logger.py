import nfc
from nfc.clf import RemoteTarget
import time

# THIS IS THE READER PARAMETER VARIABLE!

rfid_reader = "tty"

# THIS IS THE ID FOR THE ADMIN CARD!

admin_card_id = "AAF5CF23"

# initialize nfc scanner
clf = nfc.ContactlessFrontend()
assert clf.open(rfid_reader) is True 
target = clf.sense(RemoteTarget('106A'), RemoteTarget('106B'), RemoteTarget('212F'))

while True:
    
#print(tag)
    tag = clf.connect(rdwr={'on-connect': lambda tag: False})
    scan_num = str(tag)


    for i in scan_num:
        if i == 'I':
            scan_num = scan_num[scan_num.index(i)+3:]

    if scan_num == admin_card_id:
        break
    print(scan_num)
    time.sleep(0.5) 

clf.close()