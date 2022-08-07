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

print("The count of words= ", len(chtxt.split()))

toBe = [" am "," is "," are "," was "," were ", " been ", " being "]
countToBe = 0
for i in range (len(toBe)):
    countToBe += chtxt.count(toBe[i])
print("The count of to be verbs= ",countToBe)


uniqueWords=set(chtxt.replace(".","").split())
uniqueWords=set(chtxt.replace(",","").split())
#print(uniqueWords)
print("The count of unique words=" ,len(uniqueWords))

print("the count of 'am' = ", chtxt.count(" am "))
print("the count of 'is' = ", chtxt.count(" is "))
print("the count of 'are' = ", chtxt.count(" are "))
print("the count of 'was' = ", chtxt.count(" was "))
print("the count of 'were' = ", chtxt.count(" were "))
print("the count of 'been' = ", chtxt.count(" been "))
print("the count of 'being' = ", chtxt.count(" being "))