"""
In multilevel inheritance the first class is
inherited to second class, second class is begin
inherited to third class, third to fourth class
"""
class Mother:
    is_badminton = 2

class Daughter(Mother):
    is_badminton = 3
    def play(self):
        print("I play 3 hrs a day")

class GrandDaughter(Daughter):
    is_badminton = 4
    def is_play(self):
        print("I play 4 hrs a day")

one = Mother()
two = Daughter()
three = GrandDaughter()

print(two.play())