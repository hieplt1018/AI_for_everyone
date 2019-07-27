import random

dice_1 = 0;
dice_2 = 0;
dice_3 = 0;
dice_4 = 0;
dice_5 = 0;
dice_6 = 0;

for _ in range(10000):
  roll_the_dice = random.randint(1,6);
  if roll_the_dice == 1:
    dice_1 += 1;
  elif roll_the_dice == 2:
    dice_2 += 1;
  elif roll_the_dice == 3:
    dice_3 += 1;
  elif roll_the_dice == 4:
    dice_4 += 1;
  elif roll_the_dice == 5:
    dice_5 += 1;
  else:
    dice_6 += 1;

print(dice_1);
print(dice_2);
print(dice_3);
print(dice_4);
print(dice_5);
print(dice_6);
