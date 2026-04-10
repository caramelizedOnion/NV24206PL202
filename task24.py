class ScoreBoard:
    def __init__(self, score):
        self.__score = score   # private attribute

    def get_score(self):
        return self.__score


s1 = ScoreBoard(0)

print(s1.get_score())