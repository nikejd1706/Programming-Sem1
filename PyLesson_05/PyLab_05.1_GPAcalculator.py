def calcPoints(grde):
    if grde == "a":
        return 4.0
    if grde == "b":
        return 3.0
    if grde == "c":
        return 2.0
    if grde == "d":
        return 1.0
    if grde == "f":
        return 0.0
    
    
    



g1 = input("Please enter your letter grade for math: ")
g2 = input("Please enter your letter grade for science: ")
g3 = input("Please enter your letter grade for english: ")
g4 = input("Please enter your letter grade for history: ")
g5 = input("Please enter your letter grade for foreign language: ")
g6 = input("Please enter your letter grade for elective: ")
g7 = input("Please enter your letter grade for physical education: ")

print("Your GPA is", (calcPoints(g1)+calcPoints(g2)+calcPoints(g3)+calcPoints(g4)+calcPoints(g5)+calcPoints(g6)+calcPoints(g7))/7)
