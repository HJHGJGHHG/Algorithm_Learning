# Algorithm_Learning
## Python Tricks
1. 多用map少用列表推导式
```
import time
data = ["1"]*10000000

start = time.time()
a = [int(item) for item in data]
print(time.time()-start)  # 2.170196771621704

start = time.time()
b = list(map(int, data))
print(time.time()-start)  # 1.2347049713134766
```

2. 字符与Ascii码转换
```
print(ord('c'))  # 99
print(chr(99))  # 'c'
```