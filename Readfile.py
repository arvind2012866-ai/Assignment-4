'''f=open("sample.txt","w")
f.writelines(["Line 1: This is sample text file \n","Line 2:This contains multiple lines"])
f.close()

'''

try:
    with open('sample.txt', 'r') as file:
        data=file.read()
        print(data)
            
except FileNotFoundError:
   print("File not available")
except Exception as e:
     print(e)
    


