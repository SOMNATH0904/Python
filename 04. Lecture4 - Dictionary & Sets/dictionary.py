dict = {
    "name": "Somnath",
    "cgpa": 9.7,
    "marks": [93, 67, 99]
}

print(dict)
print(dict["name"])
print(dict["cgpa"])
print(dict["marks"])

dict["cgpa"] = 9.73
print(dict["cgpa"])
print(dict)
print(type(dict))