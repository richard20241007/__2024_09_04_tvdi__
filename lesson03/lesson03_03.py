import tools

print(tools.SUN)

p1 =tools.Person(name = "Ken", age=20)
print(p1)


#輸入時出現板手就表示 property
#只有method 要記得加上 括號

s1 = tools.Student('Ken',20,98,97,99)

print(f'Chinese: {s1.chinese}\nEnglish: {s1.english}\nMath: {s1.math}\nTotal: {s1.total}\nAvg: {s1.average()}')