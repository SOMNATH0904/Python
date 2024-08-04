student = {
    "name": "Somnath",
    "subjects": {
        "phy": 87,
        "chem": 97,
        "math": 95
    }
}

print(student)
print(student["subjects"]["chem"])      #Nested Dictionary

student["subjects"]["phy"] = 92
print(student)