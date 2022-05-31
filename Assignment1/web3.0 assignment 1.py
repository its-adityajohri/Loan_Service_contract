import hashlib
import time
str1 = input("Enter the string: ")
t = time.time()
x = 0
test = '0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'

while(1):
    strx = str1
    str1 = str1 + str(x)
    hashh = hashlib.sha256()
    hashh.update(str1.encode('utf-8'))
    str2 = hashh.hexdigest()
    str2 = "0x"+str2
    int1 = int(str2, 16)
    int2 = int(test, 16)
    
    if(int1<int2):
        print("The required nonce value is : ",x)
        break
    str1 = strx

    x = x+1
    
t1 = time.time() - t
print("Time taken: ",t1,"sec")
