string = raw_input("Enter word: ")

dict1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# we can leverage ascii --> get value and subtract 65 (A = 65, thus - 65 = 0)
#use ord



encryptString=[] # string to be added to, what will be returned and printed out

#boolean to see if letter capital or not (to be used later)
#to encode, make entire string uppercase
isCapital=-1; #for now, no letters
curIndex=0
for x in string:
	#where x is each letter
	
	#if (isCapital == -1):
		#means first pass of algo
	if(x.isupper()): #check if uppercase, preserves letter cas
		isCapital=1
	else:
		isCapital=0
	#if x in dictionary.values():
	temp=string.upper()
	#print(temp) STRING IS NOW IN UPPERCASE
	temp2 = temp[curIndex] #grab temp uppercase letter
	#print(temp2)
	if (temp2 in dict1):
		#oldPosition = dictionary[temp2] #get new value
		oldPosition = (ord(temp2)-65) #should be ascii value original 
		#print(oldPosition) this is working
		newPosition=(oldPosition-3)%26
		if isCapital==1:
			hold=dict1[newPosition] #grab letter
			hold=hold.upper()
			encryptString.append(hold)
		else:
			hold=dict1[newPosition]
			hold=hold.lower()
			encryptString.append(hold)
	else:
		encryptString.append(x)

	curIndex=curIndex+1
	
#convert list to string
listToString=''.join(map(str,encryptString))
print(listToString)

