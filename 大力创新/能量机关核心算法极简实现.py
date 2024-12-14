calc = ((   # 加法相关算法
    lambda _,b,c,d,f:b[0]*10+c[0]+d[0]==24 and [b,c,f,d,0],
    lambda _,b,c,d,f:b[0]+c[0]+d[0]==24 and [b,f,c,f,d,0],
    lambda a,b,c,d,f:a[0]*10+b[0]+c[0]*10+d[0]==24 and [a,b,f,c,d,0],
    lambda a,b,c,d,f:a[0]*10+b[0]+c[0]+d[0]==24 and [a,b,f,c,f,d,0],
    lambda a,b,c,d,f:a[0]+b[0]+c[0]+d[0]==24 and [a,f,b,f,c,f,d,0]
),(         # 减法相关算法
    lambda _,b,c,d,f:b[0]*10+c[0]-d[0]==24 and [b,c,f,d,0],
    lambda a,b,c,d,f:a[0]*10+b[0]-c[0]*10-d[0]==24 and [a,b,f,c,d,0],
    lambda a,b,c,d,f:a[0]*10+b[0]-c[0]-d[0]==24 and [a,b,f,c,f,d,0]
),(         # 除法相关算法
    lambda _,b,c,d,f:d[0] and (b[0]*10+c[0])/d[0]==24 and [b,c,f,d,0],
    lambda a,b,c,d,f:d[0] and (a[0]*100+b[0]*10+c[0])/d[0]==24 and [a,b,c,f,d,0]
),(         # 乘法相关算法
    lambda _,a,c,d,f:c[0]*d[0]==24 and [c,f,d,0],
    lambda _,b,c,d,f:(b[0]*10+c[0])*d[0]==24 and [b,c,f,d,0],
    lambda _,b,c,d,f:b[0]*c[0]*d[0]==24 and [b,f,c,f,d,0],
    lambda a,b,c,d,f:a[0]*b[0]*c[0]*d[0]==24 and [a,f,b,f,c,f,d,0]
))

from itertools import permutations

data = [5, 
        17, 0.1, 0.2, 0.3, 0.4, 
        16, 0.5, 0.6, 0.7, 0.8, 
        18, 0.9, 1.0, 0.1, 0.2, 
        19, 0.9, 1.0, 0.1, 0.2, 
        50, 0.9, 1.0, 0.1, 0.2
    ] #测试数据

data = [data[i:i+3] for i in range(1, 26, 5)]   #数据裁剪分组
operator = next((temp for temp in data if temp[0] > 40), None)#提取符号数据
data = [[n - 10 if n > 10 else n for n in temp] for temp in data if temp[0] < 40]       #提取数字并转换id

for func in calc[operator[0] % 5]:          #提取对应计算方法(加号id=50,50%5=0 减号51%5=1 除号52%5=2 乘号43%5=3)
    for a, b, c, d in permutations(range(4)):       #枚举数据顺序
        for target in func(data[a], data[b], data[c], data[d], operator) or []:#计算当前数字顺序和算式是否成立
            if not target: exit()               # 完成了全部击打
            print(target)
'''
输出结果:
[7, 0.1, 0.2]   -> 数字七，及其坐标
[50, 0.9, 1.0]  -> 加号，及其坐标
[8, 0.9, 1.0]   -> 数字八，及其坐标
[50, 0.9, 1.0]  -> 加号，及其坐标
[9, 0.9, 1.0]   -> 数字九，及其坐标
'''