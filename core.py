import random

#player stats
agility = 3
hp = 50
strength = 3
intellect = 3
sideBonus = random.randint(1, 3)
level = 1
nextLevel = 30
enemy = 30

import prologue

print('What is your side? 1 - bio-robots, 2 - humans')
answer1 = int(input())
if answer1 == 1:
    strength += 3
    intellect -= 3
    side = str('bio-robot')
    attack = random.randint(2, 6) + 1
else:
    strength -= 3
    intellect += 3
    side = str('human')
    attack = random.randint(1, 5) + sideBonus

print('You start in the grey area where a conflict has recently arisen')
print(f'You stay against {side} who ready to fight. Your choice: ')


print('1 - attack, 2 - dodge, 3 - block(bio-robot)/magic(human)')
while enemy >0:
  fightChoice = int(input())
#mechanics
  dodge = random.randint(1, 2)
  block = int(attack * 0.5)
  magicBonus = random
  magic = int(attack * random.uniform(0.3,0.6))
  npcRandom = random.randint(1,3)
  npcChoise1 = 0
  npcChoise2 = 0
  if npcRandom ==1:
        npcChoise1 = attack
  elif npcRandom ==2:
        npcChoise1 = dodge
  else:
        npcChoise1 = block
        npcChoise2 = magic
#player's choice
  if fightChoice == 1:
      enemy -= attack
  elif fightChoice ==2:
      if dodge == 1:
          enemy -= 0
      else:
          enemy -= attack
  if fightChoice ==3 and side == str('bio-robot'):
      enemy -= block
  if fightChoice ==3 and side == str('human'):
      enemy -= magic
  print('enemy hp: '+ str(enemy))
#npc's choise
  if enemy !=0:
    if side == str('bio-robot'):
      hp -= npcChoise2
    else:
      hp -= npcChoise1

    print('opponent\'s move. Your hp: ' + str(hp))
  else:
     nextLevel -= 5
if nextLevel == 0:
  level += 1
print('You just level up! you received 2 stat points. Make your choise:')
statChoise = int(input("agility - 1, hp - 2,strength/intellect - 3 "))
if statChoise == 1 :
  agility +=1
elif statChoise == 2:
  hp += 5
else:
  if side == str('bio-robot'):
    strength += 1
  else:
    intellect += 1