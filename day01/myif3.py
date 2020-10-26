import random

mine = input("가위바위보를 입력하세요 : \n");

rnd = random.random()

com = ""

if rnd >= 0.6 :
    com = "가위"
elif rnd >= 0.3:
    com = "바위"
else:
    com = "보"    

print("com : {}".format(com))
print("bae : {}".format(mine))


if com == mine:
    print("비겼습니다")
elif com == "가위" and mine == "바위" or com == "바위" and mine == "보" or com == "보" and mine == "가위": 
    print("이겼습니다")
else :
    print("졌습니다")
