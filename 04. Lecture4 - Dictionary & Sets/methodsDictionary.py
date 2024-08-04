dict = {
    "name": "Somnath",
    "subjects": {
        "phy": 87,
        "chem": 97,
        "math": 95
    }   
}

print(dict.keys())  #returns all the keys

print(list(dict.keys()))    #TypeCasting for converting this into list

print(len(dict))    #return the count of keys(Doesn't include nested keys)
print(dict.values())    #returns all the values

print(list(dict.values()))    #TypeCasting for converting this into list

print(dict.items())     #returns all (key, val) pairs as tuples

print(list(dict.items()))

print(dict.get("name"))     #returns the value according to the keys(Doesn't include nested keys)

dict.update({
    "city": "Baharagora",
    "state": "Jharkhand"
})     #inserts the specified items to the dictionary
print(dict)

#print(dict["name2"])    #Error
print(dict.get("name2"))    #NoError -> None