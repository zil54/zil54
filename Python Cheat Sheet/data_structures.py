#Python Cheat Sheet
#Dictionary

# Creating an empty Dictionary 
DictEuropeanCities = {} 


#Populate DictEuropeanMainCitiesPerCountry

DictEuropeanCities['Serbia']='Belgrade<-->Novi Sad'
DictEuropeanCities['Croatia']='Zagreb<-->Dubrovnik<-->Pula'
DictEuropeanCities['Italy']='Rome<-->Naples<-->Turin<-->Milan'

for i, (j,k) in enumerate(DictEuropeanCities.items()):
	splitter_arr = k.split('<-->')
	capital = splitter_arr[0]
	print (capital)
	print (i)


#Create on empty list
ListContinentsEmpty = []

#Populated
ListContinents = ['Africa','SAmerica','NAmerica','Europe','Asia','Australia']
#append
ListContinents.append('Antarctica')
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
	
print ("\n")	


#functions using args and kwargs as lists and dictionaries, respectively:

def invadeEarth(attackingFleet, *args):
	if len(args) > 0:
		attackingFleetPerContinent = attackingFleet/len(args)
		print ("Attacking fleet per continent: " + str(attackingFleetPerContinent) + "\n")
		for i, arg in enumerate(args):
			j = i + 1
			print ("Continent # " + str(j) + ": " + arg)
	else:
		print ("No continent specific split - just all-out assault against everyone with " + str(attackingFleet))
		

invadeEarth(77, *ListContinents)	
invadeEarth(77)	

def travelEurope(numberOfDays, **kwargs):
	if len(kwargs) > 0:
		citiesPlanned = 0
		print ("Number of Days per City: " + "\n")
		for i, (j,k) in enumerate(kwargs.items()):
			splitter_arr = k.split('<-->')
			citiesPlanned = citiesPlanned + len(splitter_arr)
		print (str(numberOfDays / citiesPlanned)) 
			
		
		

travelEurope(18, **DictEuropeanCities)		
		
	
	

