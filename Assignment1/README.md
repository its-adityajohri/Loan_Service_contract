In the program i take a string input from the user and add nonce value ahead of it and keep it as string. 
Then using hashlib library I create hex string storing hexadecimal value 
the target value is stored in test variable as string
both the hex strings are then converted to base 10 integers for comaparision and the infinite loop breaks when required nonce value is found
test case example - input string - "iitk"
found nonce value - 1217060
time taken - 3.970526695251465 sec
