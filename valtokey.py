#Question-1
port1={21:'FTP',22:'SSH',23:'telnet',80:'http'}
port2={}
for i,j in port1.items():
    port2[j]=i
print(port2)
