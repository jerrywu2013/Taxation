#訓練
from sklearn import linear_model
reg = linear_model.LinearRegression()
#國文、英文
reg.fit ([[30, 10], [30, 10],[30,100], [20, 20]], [45, 45,45, 20])
#預測
x = input("國文：")
y = input("英文：")
iron_man_color = reg.predict([[int(x),int(y)]])
if iron_man_color < 60:
    print("不及格喔")
elif iron_man_color >= 60:
    print("恭喜及格")
elif iron_man_color >80:
    print("太優秀了")
else:
    print("好像沒這種數字",iron_man_color)