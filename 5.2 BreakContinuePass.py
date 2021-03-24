for i in range(10):
    pass # Pass is used to handle errors while empty function or if else condition

for i in range(10):
    if i == 7:
        continue # continue will skip the next thing in loop and go for next increment in loop
        # Here it will not print 7 and go for 8th iteration in loop
    print(i)

for i in range(10):
    if i == 7:
        break # break will exit from loop
        # Here it will print loop till six and after six when condition == 7 it will break loop
    print(i)