import re
string = "'I AM NOT YELLING', she said. Though we knew it to not be true."
print(string)

new = re.sub('[A-Z]', '', string)
print(new)

new2 = re.sub('[a-z]', '', string)
print(new2)

# +" " meaing removing the spaces
new3 = re.sub('[.,\'A-Z+" "]', '', string)
print(new3)

newString = string + "6 298 - 345"
print(newString)

onlyNum = re.sub('[^0-9]', '', newString)
print(onlyNum)
