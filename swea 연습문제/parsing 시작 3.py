text = "B[45]AB[9994]"
a = text.find("[")
b = text.find("]")
c = text.find("[", a+1)
d = text.find("]", b+1)
print(int(text[a+1:b]) + int(text[c+1:d]))