#part 10, using len()
text = "PythonPython"
text1 = text[:len(text)//2 + len(text)%2]
text2 = text[len(text)//2 + len(text)%2:]
print(text1)
print(text2)