myDict={
    "Pankha":"Fan",
    "Dabba": "Box",
    "Kitab": "Book"
}
print("The words available in dictionary are: ",myDict.keys())
a=input("Enter The hindi word of which u want a meaning\n")
b=a.capitalize()
print("The meaning of your word",b,"is",myDict.get(b))

