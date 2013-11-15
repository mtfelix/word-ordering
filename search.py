
words =[]
dependency = []

agenda = []
for word in words:
    if HasPOS(word):
        EnQueue(agenda, word)
    else:
        for w in AssignPOS(word):
            EnQueue(agenda, w)

chart = []
goals = []
while not TimeOut():
    h = DeQueue(agenda)
    if GoalHypothesis(h):
        AddToSet(goals, h)
    else:
        for h_c in chart:
            if NoCollision(h, h_c):
                temp_h = Combine(h, h_c, HeadLeft)
                if temp_h:
                    EnQueue(agenda, temp_h)
                
                temp_h = Combine(h, h_c, HeadRight)
                if temp_h:
                    EnQueue(agenda, temp_h)
                
                temp_h = Combine(h_c, h, HeadLeft)
                if temp_h:
                    EnQueue(agenda, temp_h)
                
                temp_h = Combine(h_c, h, HeadRight)
                if temp_h:
                    EnQueue(agenda, temp_h)
        AddtoBeam(chart, h)
if Empty(goals):
    return Default(chart)
else:
    return BestInset(goals)
