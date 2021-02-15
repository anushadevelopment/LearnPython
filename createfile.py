import os
file = open("/users/anusha/documents/anusha_sp/pythonstudy/testfile.txt","w")
file.write("Akshu is cute")
file.close()
file1 = open("/users/anusha/documents/anusha_sp/pythonstudy/testfile.txt","a")
file1.write("\nand chella kutty is cute :)")
file1.close()