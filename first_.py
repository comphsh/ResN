import torch

print("good")

for i in range(12):
    print(i)

val = torch.randint(1000 , (2,4))
val = val[0][0]
print(val)
if val > 13:
    print("this is larger than 13")
else:
    print("this is smaller than 13")

