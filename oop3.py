from random import randrange
def f():
    class Soldier:
        def __init__(self,num,team):
            self.num = num
            self.team = team
        def go_behind_heroe(self,heroe):
            print('Go to heroe %s '% heroe)
    class Heroe(Soldier):
        level = 0
        def asc_level(self):
            self.level += 1

    heroe1 = Heroe(1,'red')
    heroe2 = Heroe(2,'blue')

    teams = [heroe1.team,heroe2.team]

    heroes = [heroe1,heroe2]

    soldiers = []

    red_team = []
    blue_team = []

    print(heroe1.num,heroe1.team)
    print(heroe2.num,heroe2.team)

    print(teams)

    i = 3
    while True:
        num = randrange(2)
        color = teams[num]
        soldier = Soldier(i,teams[num])
        if color == 'red':
            red_team.append(soldier)
        else:
            blue_team.append(soldier)
        i += 1
        if i == 7: break

    print(len(red_team))
    print(len(blue_team))

    if heroe1.team == 'red':
        if len(red_team) > len(blue_team):
            heroe1.asc_level()
    elif heroe1.team == 'blue':
        if len(red_team) < len(blue_team):
            heroe1.asc_level()

    if heroe2.team == 'red':
        if len(red_team) > len(blue_team):
            heroe2.asc_level()
    elif heroe2.team == 'blue':
        if len(red_team) < len(blue_team):
            heroe2.asc_level()

    print(heroe1.level)
    print(heroe2.level)

    
    

    

    
        

    
