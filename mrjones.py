# this program says hello and asks for my name

print('Hello World!')
print ('What is your name?') #Asks for my name
myName = input() #input funciton waits on the ENTER key (carriage return)
print ('It is good to meet you, ' + myName) #concatination of two strings
print ('The length of your name is: ')
print (len (myName)) #conversion from string value to interger
print ('What is your age?')
myAge = input()
print ('You will be ' + str(int(myAge)+ 1) + ' in one year.')