t=raw_input("")
b=['a','e','i','o','u','A','E','I','O','U']
if (t>='a' and t<='z' or t>='A' and t<='Z'):
   if(t in b):
            print("vowel")
   else:
       print("consonant")
else:
     print("invalid")
