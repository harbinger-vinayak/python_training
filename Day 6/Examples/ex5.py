"""
Operator Overloading with Dinder Function Overriding
"""

class Team(object):

    def __init__(self, teamName, *players):  # with non-keyword arguments
        self.teamName = teamName
        self.players = players

    def __len__(self):
        count = 0
        for i in self.players:
            count += 1
        return count

    def __str__(self):
        return self.teamName

    def __add__(self, other):
        allplayers = str()  # assign '' to var
        for i in self.players:
            allplayers += ' ' + i
        for j in other.players:
            allplayers += ' ' + j
        return allplayers

    def __gt__(self, other):
        var1 = len(self.players)
        var2 = len(other.players)
        if var1 > var2:
            return True


india = Team('India', 'ab', 'xy', 'pq', 'dfd')
australia = Team('Australia', 'sd', 'df', 'dfsd')

print 'Total no of players in India: {}'.format(len(india))
print 'Total no of players in Australia'.format(len(australia))
print 'Name of Team {} and players {}'.format(india, india.players)
print 'All players in India and Australia is:', india + australia
print 'Total players in India is greater than australia', india > australia

