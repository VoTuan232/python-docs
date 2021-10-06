# String Format
age = 36
txt = "My name is John, I am " + age
print(txt)

# String Format 1
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# String Format 2
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# String Format 3
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))