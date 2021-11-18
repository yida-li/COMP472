
# Python code to demonstrate
# to convert dictionary into string
# using json.dumps()
  
import json
  
# initialising dictionary
test1 = { "testname" : "akshat",
          "test2name" : "manjeet",
          "test3name" : "nikhil"}
  
# print original dictionary
print (type(test1))
print ("initial dictionary = ", test1)
  
# convert dictionary into string
# using json.dumps()
result = json.dumps(test1)

 
# printing result as string
print ("\n", type(result))
print ("final string = ", result)



d = {"efefefef": ["127.0.0.1", "8889"], "yida": ["127.0.0.1", "8889"], " fife": ["127.0.0.1", "8889"], " fucktards": ["127.0.0.1", "6969"], "mk": ["127.0.0.1", "8889"], "registration": ["127.0.0.1", "8889"], "expertsmyass": ["127.0.0.1", "1233"], "emte": ["127.0.0.1", "8889"], "john": ["127.0.0.1", "8889"], " seeeee": ["127.0.0.1", "1233"]}

for key, values in d.items():
    
        print(values[1])