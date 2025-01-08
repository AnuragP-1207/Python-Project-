def vowel(c):
   return (c.lower() in['a','e','i','o','u'])
   
c=input("Enter a character: ")
if vowel(c):
   print("vowel")
else:
   print("consonant")
