"""
regex = “((http|https)://)(www.)?” 
+ “[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]” 
+ “{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)”

The URL must start with either http or https and
then followed by :// and
then it must contain www. and
then followed by subdomain of length (2, 256) and
last part contains top level domain like .com, .org etc.

Match the given URL with the regular expression.
Return true if the URL matches with the given regular expression, else return false.
Below is the implementation of the above approach
"""

import re

def isValidURL(str):
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    p = re.compile(regex)

    if (str == None): return False
    if (re.search(p, str)): return True
    else: return False

url = "https://www.geeksforgeeks.org"

if (isValidURL(url) == True): print("Yes")
else: print("No")