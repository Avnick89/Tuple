#Tuple Itinerary

Itinerary =[("Anthony", "Texas", "Paris"),("Elmer", "Mexico", "Spain")]
Itinerary[0] = ("Anthony from Texas to Paris")
print(Itinerary[0]) 
Itinerary[1] = ("Elmer from Mexico to Spain")
print(Itinerary[1])
    
  
 

#Library System
import bisect
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
bisect.insort(library,("Harry Potter", "J. K Rowling"))
print (library)