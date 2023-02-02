def my_name():#0
  print("jani")

my_name()#0

def my_name1():#1
  return "jani"

name = my_name1() #1
print(name)

def output(text, amount):#2  #def output(text, amount):
    i = 0                    #print(text * amount) 
    while i < amount:        # output("moro", 10)
       print(text)
       i += 1

output("hello",2)#2

def get_max(a,b,c):
   max = a
   if b > max:
      max = b
   if c > max:
      max = c
   return max   

largest = get_max(1,2,3)
print(largest)