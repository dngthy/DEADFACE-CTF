buf = open('All_Seeing_Eye.jpg', 'rb').read()

fix = b''
with open('All_Seeing_Eye.jpg', 'wb') as fd:
    for i in range(0, len(buf), 4):
        fd.write(bytes(list(reversed(buf[i:i+4]))))
