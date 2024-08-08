import torch

print("good")

for i in range(12):
    print(i)


A = torch.tensor([1,2])
B = torch.tensor([5,8])
C = A+B
print(C)