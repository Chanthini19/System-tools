msg=input("Enter Your Message:")
output="Hello " + msg
print(output)
with open('checkoutput.txt','w') as f:
    f.write(output)
    f.close()