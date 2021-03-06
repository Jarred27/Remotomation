import getConfigs
import socket
import sys

# description here

def uploadFile(fileName,channelNum,instID):
    #load settings
    [TCP_IP,TCP_PORT,BUFFER_SIZE,connectionTimeout,AWG_address]=getConfigs.getConfigs().split(", ")
    TCP_PORT=int(TCP_PORT)
    BUFFER_SIZE=int(BUFFER_SIZE)
    connectionTimeout = int(connectionTimeout)

    if instID=="AWG":
        instID=AWG_address

    #define string to send
    messageString = "file, upload, " + fileName + ", " + channelNum + ", " + instID
    formattedMessage=messageString.encode('UTF8')

    #bind port
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        return "err socketConfigError"

    #connect to server
    errorFlag = s.connect_ex((TCP_IP, TCP_PORT))
    if errorFlag != 0:
        returnString="err hostNotFoundErr#:"+str(errorFlag)
        s.close()
        return returnString

    #send message
    s.send(formattedMessage)
    data = s.recv(BUFFER_SIZE)
    if not data:
        returnString="err noResponse"
    else:
        response = data.decode("utf-8")
        arr = response.split(", ")
        if (arr[0]=="file") & (arr[1]=="uploadResult"):
            if arr[2] == "1":#error flag
                returnString="err "+arr[3]
            else:
                returnString = arr[2]
        else:
            returnString="err unexpectedResponse"

    s.close()
    return returnString

if __name__=="__main__":
    if len(sys.argv) == 4:
        fileName = sys.argv[1]
        channelNum = sys.argv[2]
        instID= sys.argv[3]
        result=uploadFile(fileName,channelNum,instID)
        print(result)
        sys.exit(result.split(" ")[0]=="err")
    else:
        print("err expected 3 argument got "+str(len(sys.argv)-1))
        sys.exit(1)
