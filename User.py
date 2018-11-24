import CryptoLib
import ast
#Arrays de traduccion
array={"a":"31","b":"32","c":"33","d":"34","e":"35","f":"36","g":"37","h":"38","i":"39","j":"10","k":"11","l":"12","m":"13","n":"14","o":"15","p":"16","q":"17","r":"18","s":"19","t":"20","u":"21","v":"22","w":"23","x":"24","y":"25","z":"26"," ":"27",".":"28"}
array1 = {v: k for k, v in array.items()}
encrypt=CryptoLib.encrypt()
while(True):
    #Menu
    input1=str(input("\nMenu \n=================================================== \n1.-Encode \n2.-Decode \n3.-Keys(Recommended after introducing other keys) \n4.-Exit \n=================================================== \nCommand: "))
    if(input1.lower()=="encode"):
        #Get Message and Translate into Array
        msg=str(input("Message to Encrypt: "))
        msgtr=int(CryptoLib.encode(msg.lower(),array))

        #Encode Messagge(MATHS!)
        input2=str(input("Random or Given"))
            # Codificarlo con valores Aleatorios o Dados(Usuario)
        if(input2.lower()=="given"):
            encrypt[3]=int(input("Clave Publica(ee): "))
            encrypt[2]=int(input("Modulo (n): "))
        msg_encriptado=pow(msgtr,encrypt[3],encrypt[2])
        print(msg_encriptado)


        #Save Keys and Message
        f = open("RSA.txt","w")
        f.write("Publica: "+str(encrypt[3])+"\n\nModulo: "+str(encrypt[2])+"\n\nPrimes: \n      P= " +str(encrypt[0])+"\n      Q= " +str(encrypt[1])+"\n\nPRIVADA: "+str(encrypt[4])+"\n\nMensaje: "+str(msg)+"          Mensaje Traducido: "+ str(msgtr) +"        Mesansaje Encryptado: "+ str(msg_encriptado))
        f.close()


        #Prints Keys and Message
        print("Publica: "+str(encrypt[3])+"\n\nModulo: "+str(encrypt[2])+"\n\nPrimes: \n      P= " +str(encrypt[0])+"\n      Q= " +str(encrypt[1])+"\n\nPRIVADA: "+str(encrypt[4])+"\n\nMensaje: "+str(msg)+"          Mensaje Traducido: "+ str(msgtr) +"        Mesansaje Encryptado: "+ str(msg_encriptado))
    elif(input1.lower()=="decode"):
        input3=str(input("Uncode \n===================================================\n1.-Normal \n2.-Debug \n=================================================== \nCommand: "))
        input2=int(input("Message to Decode: "))
        if(input3.lower()=="normal"):
            encrypt[4]=int(input("Clave Privada: "))
            encrypt[2]=int(input("Modulo: "))
        print("The Coded Message: "+str(input2)+"\n\nDecoded: "+CryptoLib.dencrypt(input2,encrypt[4],encrypt[2],array1))
    elif(input1=="keys"):
        encrypt=CryptoLib.encrypt()
    elif(input1.lower()=="exit"):
        break
