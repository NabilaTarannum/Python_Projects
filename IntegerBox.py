import easygui

Res1 = easygui.enterbox(msg="Your name?")
Res2 = easygui.integerbox(msg="Enter price", upperbound=999)
print(Res1, type(Res1), Res2, type(Res2))
