class player:
    teamName ='Liverpool'
    
    def __init__(self, name):
        self.name = name
        self.formerTeam = []
        
p1 = player('Ismael')
p1.formerTeam.append('Manchester united')
p2= player('Messi')
p2.formerTeam.append('Barcelona')

print('the player is :', p1.name)
print("previous team was: ", p1.formerTeam)
print("currently playing in :", p1.teamName)
print()
print("2nd player is :", p2.name)
print("prevous team was: ", p2.formerTeam)
print("currently playing in :", p2.teamName)
