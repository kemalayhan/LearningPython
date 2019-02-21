#Programme which filter out string values
list = ["123", "asd12", "22", "asda"]

for i in list:
    try:
        i = int(i)
        print(i)
    except:
        pass

#This programme reverse word you enter
def reverse(word):
    if (type(word) != str):
        raise ValueError("Please enter string value")
    else:
        return word[::-1]
print(reverse("ab"))


#If number you enter is even this function will return True.
def is_even(numb):
    if(numb % 2 == 0):
        return numb
    else:
        raise ValueError("You entered odd number")

list1 = [2,3,4,5,6]

for i in list1:
    try:
        print(is_even(i))
    except:
        pass


