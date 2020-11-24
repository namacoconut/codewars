# 1:Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.
#by rearrange the code
# Can you help her?

def greet(name):
  if name == "Johnny":
    return "Hello, my love!"
  return "Hello, {name}!".format(name=name)      

print (greet('Johnny'))

def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True
    