from logger import logger 

@logger 
def add(a,b):
    return a+b 

print(add(10,20))


# ✅ Every time you call a function → it logs automatically.
# ✅ This is used in real applications.


