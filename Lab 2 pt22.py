#Lab 2 p22, Dictionaries
student = {
    "name": "John Doe",
    "ID": 9999999,
    "Course": "CIS30A"
}
print(student)
student["Semester"] = "Fall 2020"
print(student)
student["Course"] = "Python"
print(student)
student.pop("ID")
print(student)
student.popitem()
print(student)
del student
print(student)  # This will raise an error since student has been deleted