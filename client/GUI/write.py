import getConfigs
import socket
import sys

# takes 2 input arguments, the first being the instrument address and the second the being the message to send,

def write(instID,message):
    #load settings
    [TCP_IP,TCP_PORT,BUFFER_SIZE,connectionTimeout]=getConfigs.getConfigs().split(", ")
    TCP_PORT=int(TCP_PORT)
    BUFFER_SIZE=int(BUFFER_SIZE)
    connectionTimeout = int(connectionTimeout)

    #define string to send
    messageString = "visa, write, "+instID+", "+message
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
        if len(arr)<=3:
            if arr[2] == "1":
                returnString = "err invalidResponse"
            else:
                returnString=""
        else:
            if arr[0] == "visa" & arr[1] == "writeResult":
                if arr[2] == "1":  # error flag
                    returnString = "err " + arr[3]
                else:
                    returnString = arr[2]
            else:
                returnString = "err unexpectedResponse"

    s.close()
    return returnString

if __name__=="__main__":
    if len(sys.argv) >= 3:
        instID = sys.argv[1]

        # recombine all text after inital arguments into one string
        max=len(sys.argv)
        i=2
        message = ""
        while 1:
            message += sys.argv[i]
            i += 1
            if i >= max:
                break
            message += " "
        result = write(instID,message)
        print(result)
        sys.exit(result.split(" ")[0]=="err")
    else:
        print("err expected 2 arguments got "+str(len(sys.argv)-1))
        sys.exit(1)
