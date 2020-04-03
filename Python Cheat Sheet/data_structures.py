#Python Cheat Sheet
#Dictionary

# Creating an empty Dictionary 
DictEuropeanCapitals = {} 


#Populate DictEuropeanMainCitiesPerCountry

DictEuropeanCapitals['Serbia']='Belgrade<-->Novi_Sad'
DictEuropeanCapitals['Croatia']='Zagreb<-->Dubrovnik<-->Pula'
DictEuropeanCapitals['Italy']='Rome<-->Naples<-->Turin<-->Milan'

for i, (j,k) in enumerate(DictEuropeanCapitals.items()):
	splitter_arr = k.split('<-->')
	capital = splitter_arr[0]
	print (capital)
	print (i)


#Create on empty list
ListContinentsEmpty = []

#Populated
ListContinents = ['Africa','SAmerica','NAmerica','Antarctica','Europe','Asia','Australia']
#append
ListContinents.append('Atlantida')
print ("individual continent")
print (ListContinents[3])

print ("version 1 --> range")
for x in range(len(ListContinents)): 
    print (ListContinents[x])

print ("version 2 --> simple for loop")
for continent in ListContinents:
	print (continent)
	
print ("version 3 --> enumerate")	
for i, continent in enumerate(ListContinents):
	print (ListContinents[i])