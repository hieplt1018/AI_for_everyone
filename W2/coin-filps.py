import random;
num_tails = 0;
num_heads = 0;
for _ in range (1000):
  coin = random.random();
  if coin < 0.5:
    num_tails += 1;
  else:
    num_heads += 1;

print(num_tails)
print(num_heads)
