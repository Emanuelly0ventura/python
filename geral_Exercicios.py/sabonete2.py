num_inferior = 1
num_superior = 10
print(f"{1:3d}")
print(f"{2:3d}")

for num oin range(3,num_superior + 1,2):
    primo = True
    for i in range(3,int(num**0.5) + 1,2):
        if num % i == 0:
            primo = False
            break
    
if primo:
    print(f"{num:3d}")