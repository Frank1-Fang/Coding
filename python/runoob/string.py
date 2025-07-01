# use '' or "" to create a string variable
var1 = 'Hello World!'
var2 = "Runoob"

print ("var1[0]: ", var1[0]) # output: var1[0]:  H
print ("var2[1:5]: ", var2[1:5]) # output: var2[1:5]:  unoo
                                 # [1:5]: 打印第2位到第5位的字符，遵循左闭右开的原则（这里不打印第六位）

# Update a string
var1 = 'Hello World!'

print ("已更新字符串 : ", var1[:6] + 'Runoob!') # 将var1中的Hello 与Runoob拼接在一起


