str = input("Ingrese una palabra ")
print(str)
string_reversed=[]
i = len(str)
while i > 0: 
    string_reversed += str[i-1]
    i = i - 1 # decrement index
print("The Reversed String is", string_reversed)