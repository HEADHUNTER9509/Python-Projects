import random
when = ['A few years ago', 'In the scorching summers of 2077', 'In the distant Future','On 27 August 2077']
who = [ 'an emperor', 'a scavenger droid', 'a trooper','a person']
name = ['Gaz','KAY/O', 'Simon', 'Cypher']
residence = ['C-1911 Earth', 'USA', 'Los Santos', 'Night City']
went = ['World War III', 'R-90 Predator Spaceship','Formula 1 Track', 'Corpo Battle stations']
happened = ['And fought against Russia and won.','And explored it to find alien weaponry.', 'And witnessed a massive victory of T1871.', 'And faught the Demons from hell.']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) +
 ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))