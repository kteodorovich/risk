import random
from tqdm import tqdm

def sim_attack(a, d):
  if a > 3:
    a = 3
  attack = [random.randint(1, 6) for i in range(a)]
  attack.sort(reverse=True)

  defs = [random.randint(1, 6) for i in range(d)]

  return all(attack[i] > defs[i] for i in range(d))


def get_odds(a, d, trials=100000000):
  print('running %i trials' % trials)
  wins = 0
  for i in tqdm(range(trials)):
    if sim_attack(a, d):
      wins += 1

  return wins / trials

a = int(input('attackers: '))
d = int(input('defenders: '))

print('%i attackers vs. %i def' % (a, d))
odds = get_odds(a, d)

print('the attacker has a %.4f%% chance of winning' % (odds * 100))
# print('that is approximately %i/%i' % odds.as_integer_ratio())
    
