###txt is the paragraph we want to check###
## txt is copined form a colleague python file##
txt = """
City life is full of fun. There are parks and picnic spots to visit. We have cinema halls to see movies.
We have electricity which runs our factories, light and cools our home and helps us in seeing T.V.
There are all type of amenities like water, health check up and transport.
Sometimes circus shows and magic shows entertain the city people.
"""

###chtxt is created to make paragraph in lower case to be ready to check###
chtxt = txt.lower()

print("Count of words= ", len(chtxt.split()))

toBe = [" am "," is "," are "," was "," were "]

countToBe = 0
for i in range (1,len(toBe)):
    countToBe += chtxt.count(toBe[i])

print(countToBe)