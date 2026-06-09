#Part 9, using replace()
text = "No pain, no gain!?!"
if "!" in text:
    text = text.replace("!", ".")
if "?" in text:
    text = text.replace("?", "|")
if "," in text:
    text = text.replace(",", ";")
print(text)
