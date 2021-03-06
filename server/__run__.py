import main
import socket

configFile = open("config.txt", "r")
configs= configFile.read().split('\n')

#default settings
TCP_IP=str(socket.gethostname())
TCP_PORT="5005"
BUFFER_SIZE="1024"
connectionTimeout="2"
filePath=""

# importing settings from config file
for line in configs:
    [setting,value]=line.split(': ')
    if setting=='TCP_IP':
        TCP_IP=value
        continue
    if setting=='TCP_PORT':
        TCP_PORT=int(value)
        continue
    if setting=='BUFFER_SIZE':
        BUFFER_SIZE=int(value)
        continue
    if setting=='File_Path':
        filePath=value
        continue
    if setting=='Connection_Timout(s)':
        connectionTimeout=int(value)
        continue

# loop forever in TCP server
main.runTCP(TCP_IP,TCP_PORT,BUFFER_SIZE,filePath,connectionTimeout)

# code will never get here
input()