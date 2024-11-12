3：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
import math
def find_numbers():
    results = set();#使用集合而非列表或者元组，因为集合元素非重复。
    for i in range(1, 84):
        if 168 % i == 0:
            n1m = i;
            n2m = 168 // i;
            n = (n1m + n2m) / 2;
            m = (n1m - n2m) / 2;
            if n > m and n.is_integer() and m.is_integer():
                results.add(int(m**2 - 100));
    return results;
print(find_numbers());
4：输入某年某月某日，判断这一天是这一年的第几天？
import math
def what_day(year, month, date):
    big = [1,3,5,7,8,10,12];
    small = [4,6,9,11];
    num = date;
    while month > 1:
        month = month - 1;
        if month in big:
            num = num + 31;
        elif month in small:
            num = num + 30;
        else:
            num = num + 28;
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:#闰年
        if month > 2:
            num = num + 1
    return num

year = int(input())
month = int(input())
date = int(input())
numb = what_day(year,month,date)
print(f'这一天是这一年的第{numb}天');

5.输入三个整数x,y,z，请把这三个数由小到大输出。
import math
def max_num(x1, y1, z1):
    if x1 > y1:
       x1, y1 = y1, x1
    if y1 > z1:
        y1, z1 = z1, y1
    if x1 > z1:
        x1, z1 = z1, x1
    return x1, y1, z1

x, y, z = map(int, input().split())
x1, y1, z1 = max_num(x, y, z)
print(x1, y1, z1)

6.斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
import math
def fib(num0):
    if num0 == 0:
        return 0
    elif num0 == 1:
        return 1
    else:
        return fib(num0-1) + fib(num0-2)

a = input('要输出斐波那契数列的第几项？\n')
print(fib(int(a)))


7.将一个列表的数据复制到另一个列表中
import math
#列表复制分为浅拷贝和深拷贝，深拷贝是指针两个
#指针指向同一个内容，浅拷贝就是简单一点只是把内容复制一下

def copy1(list1):##深拷贝
    list2 = list1
    return list2
def copy2(list1):##浅拷贝
    list2 = list1[:]
    return list2


list3 = list(map(int, input().split(",")))
print(list3)
print(copy1(list3))
print(copy2(list3))


8.输出 9*9 乘法口诀表。
import math
def multiplication_list():
    for i in range(1,9):
        print(f'{i}x{i} = {i**2}')

print("输入Yes,输出9*9乘法表")
if input() == 'Yes':
    multiplication_list()
else:
    print('非法输入')

9.暂停一秒输出。
import time#导入time库
def p_time(a):
    time.sleep(a)
curtime1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print('暂停前的时间是'+curtime1)
print('请输入要暂停程序使用的时间？')
p_time(int(input()))
curtime2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print('暂停后的时间是'+curtime2)


10.暂停一秒输出，并格式化当前时间。
import time#导入time库
def timeandstrf():
    time.sleep(1)
    #strftime的意思是string format time
    #strftime(format,t)format里面是一个字符串
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("当前时间：",current_time)

print('下面为当前时间暂停一秒后的时间:\n')
timeandstrf()


11.古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
import math
#简单算一下每个月的兔子对数是1,1,2,3,5,8,13,21
#就是从第三个月开始，每个月都是前两个月相加
def sum_rabbit(month):
    if month == 1 or month == 2:
        return 2
    else:
        return sum_rabbit(month-1) * 2 + sum_rabbit(month-2) * 2

month = int(input('请输入算地几个月的兔子总数'))
print(sum_rabbit(month))

12.判断101-200之间有多少个素数，并输出所有素数。
import math
def is_sushu():
    for i in range(101, 201):
        is_su = 1
        for j in range(2, int(math.sqrt(i))):
            if i % j == 0:
                is_su = 0
                break
        if is_su:
            print(i)

print('下面为101-200之间的所有素数')
is_sushu()


13.打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

import math
def shuixianhua():
    for i in range(100, 1000):
        ge = i % 10
        shi = i // 10 % 10
        bai = i // 100
        if ge**3 + shi**3 + bai**3 == i:
            print(i)

shuixianhua()

14.将一个正整数分解质因数。例如入90,打印出90=2*3*3*5

import math
def yinshifenjie(a):
    items = []
    zhi = 2
    while a > 1:
        while a % zhi == 0:
            items.append(zhi)
            a = a // zhi
        zhi += 1
    return items

a = input('请输入因式分解的整数')
a = int(a)
yinshi = yinshifenjie(a)
print(f'{a}=',end='')
j = 1
for i in yinshi:
    if j != len(yinshi):
        print(f'{i}*',end='')
        j += 1
    else:
        print(f'{i}.',end='')


15.利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
import math
def score_level(score):
    if score >= 90:
        return 'A'
    elif score >=60:
        return 'B'
    else:
        return 'C'

score = input('请输入你的成绩')
score = int(score)
print('你的等级是'+score_level(score))

16.输出指定格式的日期。
import math
from datetime import datetime
time = datetime.now()
formatted_date = time.strftime("%Y-%m-%d %H:%M:%S")
print('当前时间为:'+formatted_date)

17.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

import math
import string
from datetime import datetime
def tongji(s):
    alpha, space = 0, 0
    digit, sym = 0, 0
    for i in s:
        if i.isalpha():
            alpha += 1
        elif i == ' ':
            space += 1
        elif i.isdigit():
            digit += 1
        else:
            sym += 1
    return alpha, space, digit, sym

if __name__ == '__main__':
    s = input()
    a, sp, d, sy = tongji(s)
    print(f'字母,空格,数字,其他字符的个数分别为{a},{sp},{d},{sy}')

18.求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
import math
import string
from datetime import datetime
def duo(a,n):
    sum1 = []
    it = a
    sum1.append(it)
    for i in range(2,n+1):
        it = it * 10
        it += a
        sum1.append(it)
    return sum(sum1)
a, n = map(int, input().split())
print(duo(a, n))

19.一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数
import math
import string
from datetime import datetime
def yinzi(a):
    yinzi = [1]
    for i in range(2,a):
        if a % i == 0:
            yinzi.append(i)
    return yinzi
def is_wanshu(a):
    yin = yinzi(a)
    if sum(yin) == a:
        return 1
    else:
        return 0

if __name__ == '__main__':
    for i in range(2,1001):
        if is_wanshu(i):
            yinzilist = yinzi(i)
            print(i)
            for item in yinzilist:
                print(item,end=' ')
            print()

20.一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
import math
import string
from datetime import datetime
def highm():
    sum = 100
    hight = 100
    for i in range(1,10):
        hight = hight / 2
        sum += hight*2
    hight = hight / 2
    print(f'共经过{sum}米,第10次反弹{hight}米')

if __name__ == '__main__':
    highm()

21.猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
import math
import string
from datetime import datetime
def monkey_tao():
    sum_tao = 1
    for i in range(1,10):
        sum_tao = (sum_tao+1) * 2
    return sum_tao
if __name__ == '__main__':
    a = monkey_tao()
    print(f'第一天共摘了{a}个桃子')

22.两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

import math
import string
from datetime import datetime
import itertools #迭代器和排列组合
def team_two():
    team_A = ['a', 'b', 'c']
    team_B = ['x', 'y', 'z']
    all_B = itertools.permutations(team_B)#返回的对象是一个迭代器
    #迭代器和列表的区别就是迭代器不是即时生成的，类似唯心主义，你不需要
    #时就不存在
    for game in all_B:
        ga, gb, gc = game
        if ga != 'x' and gc != 'x' and gc != 'z':
            print(f'比赛结果为:a -- {ga},b -- {gb},c -- {gc}')



if __name__ == '__main__':
    team_two()

23.打印出如下图案（菱形）
 *
  ***
 *****
*******
 *****
  ***
   *
import math
import string
from datetime import datetime
import itertools #迭代器和排列组合
def print_pattern():
    for i in range(1,4):
        print(' ' * (4-i),end='')
        print('*' * (2*i-1))
    print('*' * 7)
    for i in range(3,0,-1):
        print(' ' * (4-i),end='')
        print('*' * (2*i-1))
if __name__ == '__main__':
    print_pattern()

24.有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

import math
import string
from datetime import datetime
import itertools #迭代器和排列组合
def sequence_sum():
    f1, f2 = 1.0, 2.0
    sum = 0.0
    for i in range(1,21):
        sum += f2/f1
        f1,f2 = f2,f1+f2
    return sum
if __name__ == '__main__':
    a = sequence_sum()
    print(f'前20项之和为{a}')

25.求1+2!+3!+...+20!的和。
import math
import string
from datetime import datetime
import itertools #迭代器和排列组合
def easy_factorial():
    sum = 0
    for i in range(1,21):
        sum += math.factorial(i)
    return sum

def dif_factorial():
    sum = 0
    fac = 1
    for i in range(1,21):
        fac *= i
        sum += fac
    return sum


if __name__ == '__main__':
    print('请输入1or2,1.函数方法，2.循环方法计算1到20的阶乘和')
    a = int(input())
    if a == 1:
        print(easy_factorial())
    elif a == 2:
        print(dif_factorial())
    else:
        print('输入错误，请仅仅输入1或者2')


26.递归方式求5！
import math
import string
from datetime import datetime
import itertools #迭代器和排列组合
def factorial_num(a):
    if a == 1:
        return 1
    else:
        return a * factorial_num(a-1)

if __name__ == '__main__':
    b = factorial_num(5)
    print(b)

27.利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

import math
import string
from datetime import datetime
import itertools #迭代器和排列组合
def reverse_print(s,l):
    if l > 0:
        print(s[l-1],end='')
        reverse_print(s,l-1)

if __name__ == '__main__':
    print('请输入五个字符')
    str1 = input()
    l1 = len(str1)
    reverse_print(str1,l1)

28.有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？

import math
import string
from datetime import datetime
import itertools #迭代器和排列组合
def nianling(n):
    if n == 1:
        return 10
    else:
        return nianling(n-1)+2


if __name__ == '__main__':
    ni = nianling(5)
    print(ni)


29.给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
import math
import string
from datetime import datetime
import itertools #迭代器和排列组合
def integer_wei(n):
    a = n // 10000
    b = n // 1000 % 10
    c = n // 100 % 10
    d = n // 10 % 10
    e = n % 10
    if a != 0:
        print(f'五位数{e}{d}{c}{b}{a}')
    elif b != 0:
        print(f'四位数{d}{c}{b}{a}')
    elif c != 0:
        print(f'三位数{c}{b}{a}')
    elif d != 0:
        print(f'二位数{b}{a}')
    elif e != 0:
        print(f'一位数{a}')

if __name__ == '__main__':
    a = int(input())
    integer_wei(a)

30.一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
import math
import string
from datetime import datetime
import itertools #迭代器和排列组合
def huiwen(n):
    a = n // 10000
    b = n // 1000 % 10
    c = n // 100 % 10
    d = n // 10 % 10
    e = n % 10
    if a == e and b == d:
        print('是回文数')
    else:
        print('不是回文数')

if __name__ == '__main__':
    n = int(input())
    huiwen(n)

31.请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

import math
import string
from datetime import datetime
import itertools #迭代器和排列组合
#monday,tuesday,wednesday,thursday,friday,saturday,sunday
def whichday(s):
    if s[0] == 'm':
        return '周一'
    elif s[0] == 'w':
        return '周三'
    elif s[0] == 'f':
        return '周五'
    elif s[0] == 't':
        if s[1] == 'u':
            return '周二'
        else:
            return '周四'
    elif s[0] == 's':
        if s[1] == 'a':
            return '周六'
        else:
            return '周日'
    else:
        return '输入错误'

if __name__ == '__main__':
    n = input()
    which = whichday(n)
    print(which)
32.按相反的顺序输出列表的值。
import math
import string
from datetime import datetime
import itertools #迭代器和排列组合
#monday,tuesday,wednesday,thursday,friday,saturday,sunday
def reverse_list(s,l):
    for i in range(l-1,-1,-1):
        print(s[i],end=' ')


if __name__ == '__main__':
    str1 = map(str,input().split(' '))
    str1 = list(str1)
    le = len(str1)
    reverse_list(str1,le)

33.
按逗号分隔列表。
import math
import string
from colorama import Fore, Style
from datetime import datetime
import itertools #迭代器和排列组合
def splitdouhao(L):
    s1 = ','.join(map(str, L))
    print(s1)

if __name__ == '__main__':
    L = [1,2,3,4,5,6,7]
    splitdouhao(L)


34.练习函数调用。使用函数，输出三次 RUNOOB 字符串。
import math
import string
from colorama import Fore, Style
from datetime import datetime
import itertools #迭代器和排列组合
def print_str():
    print('RUNBOOB')

if __name__ == '__main__':
    print_str()
    print_str()
    print_str()

35.
文本颜色设置。
import math
import string
from colorama import Fore, Style
from datetime import datetime
import itertools #迭代器和排列组合




def text__color():
    print(Fore.RED + '这是红色')
    print(Fore.GREEN + '这是绿色')
    print(Fore.BLUE + '这是蓝色')

if __name__ == '__main__':
    text__color()

36.求100之内的素数。
import math
import string
from colorama import Fore, Style
from datetime import datetime
import itertools #迭代器和排列组合
def is_prime(a):
    for i in range(2,a):
        if a % i == 0:
            return 0
    return 1
def primein100():
    for j in range(1,101):
        if is_prime(j):
            print(j,end=' ')
if __name__ == '__main__':
    primein100()

37.对10个数进行排序。
import math
import string
from colorama import Fore, Style
from datetime import datetime
import itertools #迭代器和排列组合
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr [j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr
if __name__ == '__main__':
    L = list(map(int, input().split()))
    L_xu = bubble_sort(L)
    print(L_xu)

38.求一个3*3矩阵主对角线元素之和。
import math
import string
from colorama import Fore, Style
from datetime import datetime
import itertools #迭代器和排列组合
def matrix_diagonal(arr,n):
    sum = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                sum += arr[i][j]
    return sum

if __name__ == '__main__':

    L = list(map(int, input('请输入9个数字组成一个3*3的二维数组').split()))
    matrix = [L[i*3:(i+1)*3]for i in range(3)]
    print(matrix_diagonal(matrix,3))


39.有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

import math
import string
from colorama import Fore, Style
from datetime import datetime
import itertools #迭代器和排列组合
def insert_and_sort(arr,a):
    l = len(arr)
    if a >= arr[l-1]:
        arr.append(a)
    else:
        for i in range(l):
            if a > arr[i] and a < arr[i+1]:
                arr.insert(i+1,a)
    return arr

if __name__ == '__main__':
    l = list(map(int,input().split()))
    a = int(input())
    l = insert_and_sort(l,a)
    print(l)



40.将一个数组逆序输出。
import math
import string
from colorama import Fore, Style
from datetime import datetime
import itertools #迭代器和排列组合
def reverse_print(arr):
    arr.reverse()
    print(arr)

if __name__ == '__main__':
    l = list(map(int,input().split()))
    reverse_print(l)


41.模仿静态变量的用法。
import math
import string
from colorama import Fore, Style
from datetime import datetime
import itertools #迭代器和排列组合
class MyClass:
    me = 0#类的属性属于静态变量

    def function():
        MyClass.me += 1
        print('MyClass.me=',MyClass.me)

if __name__ == '__main__':
    MyClass.function()#静态变量
    MyClass.function()
    MyClass.function()


42.学习使用auto定义变量的用法。
import math
import string
from colorama import Fore, Style
from datetime import datetime
import itertools #迭代器和排列组合
def auto():
    num = 1
    print('%d'%num)
    num += 1

if __name__ == '__main__':
    num = 5
    for i in range(5):
        num += 1
        print('外面的num%d'%num)
        auto()


43.模仿静态变量(static)另一案例。（同41）

import math
import string
from colorama import Fore, Style
from datetime import datetime
import itertools #迭代器和排列组合
class MyClass:
    me = 0#类的属性属于静态变量

    def function():
        MyClass.me += 1
        print('MyClass.me=',MyClass.me)

if __name__ == '__main__':
    MyClass.function()#静态变量
    MyClass.function()
    MyClass.function()

44.两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
import math
def matrix_input():
        matrix = []
        print('输入一个矩阵，三行三列中间用空格隔开')
        for i in range(3):
            list1 = input(f'请输入第{i+1}行的数字')
            matrix.append([int(num) for num in list1.split()])
        return matrix
def matrix_add(m1,m2):
    m3 = []
    for i in range(3):
        list2 = []
        for j in range(3):
            list2.append(m1[i][j]+m2[i][j])
        m3.append(list2)
    return m3
def print_matrix(m3):
    for l in m3:
        print(' '.join(map(str, l)))

if __name__ == '__main__':
    m1 = matrix_input()
    m2 = matrix_input()
    m3 = matrix_add(m1,m2)
    print_matrix(m3)

45.统计 1 到 100 之和。
import math
def sum_from1_100():
    n, sum = 1, 0
    while(n <= 100):
        sum += n
        n += 1
    print(sum)

if __name__ == '__main__':
    sum_from1_100()




46.求输入数字的平方，如果平方运算后小于 50 则退出。
import math
from gmpy2 import square
def square_50():
    a = int(input('请输入一个数字\n'))
    if a**2 < 50:
        return 0
    else:
        print(a**2)

if __name__ == '__main__':
    square_50()


47.两个变量值互换。
import math
def exchange(a,b):
    return b, a


if __name__ == '__main__':
  print('请输入两个int值')
  a, b = map(int,input().split())
  a, b =exchange(a,b)
  print(a,b)

48.数字比较。
import math
def compare(a,b):
    if a > b:
        print(f'{a}大于{b}')
    elif a < b:
        print(f'{a}小于{b}')
    else:
        print(f'{a}等于{b}')


if __name__ == '__main__':
    a, b = map(int,input().split())
    compare(a,b)

49.使用lambda来创建匿名函数。
easy = lambda: "我很帅"
print(easy())


50.输出随机数
import random
print(random.randint(1,100))
print(random.uniform(1.0,100.0))


51.学习使用按位与 & 。
a = 12
b = 10

result = a & b #逻辑与
print(result)

52.学习使用按位或 | 。
a = 12
b = 10

result = a | b #逻辑或
print(result)

53.学习使用按位异或 ^ 。
a = 12
b = 10

result = a ^ b #逻辑异或
print(result)

54.取一个整数a从右端开始的4〜7位。
def from4to7(a):
    for i in range(4):
        a = a // 10
    print(a)

if __name__ == '__main__':
    a =int(input("请输入一个数字："))
    from4to7(a)

55.学习使用按位取反~。
a, b = 7, -9
a = ~a
b = ~b
print(a)
print(b)

56.画图，学用circle画圆形。
import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

pen.color("red")
pen.circle(100)

screen.mainloop()



57.画图，学用line画直线。
import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

pen.penup()
pen.goto(100, 200)
pen.pendown()

pen.color("red")
pen.pensize(6)

pen.goto(100, 50)

turtle.done()



58.画图，学用rectangle画方形
import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

pen.color("blue")
pen.pensize(3)

for i in range(4):
    pen.forward(100)
    pen.right(90)

turtle.done()




59.画图，综合例子
过

60.计算字符串长度
str = input('请输入一个字符串')
print(len(str))

61.打印出杨辉三角形（要求打印出10行
def print_triangle():
    a = [[0] * (i + 1) for i in range(10)]

    for i in range(10):
        a[i][0] = 1
        a[i][i] = 1

    for i in range(2, 10):
        for j in range(1, i):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]

    for i in range(10):
        print(" ".join(str(num) for num in a[i]))

if __name__ == '__main__':
    print_triangle()


62.查找字符串
def find_str(s1,s2):
    return s1.find(s2)

if __name__ == '__main__':
    s1 = input('请输入完整字符串')
    s2 = input('请输入匹配字符串')
    a = find_str(s1,s2)
    print(f's2在s1的第{a}个位置')
63.画椭圆
import tkinter as tk



def tuoyuan():
    window = tk.Tk()
    window.title('画椭圆')
    window.geometry('600x800')
    canvas = tk.Canvas(window, width=400, height=300, bg='white')
    canvas.pack()
    canvas.create_oval(50, 50, 350, 250, outline="blue", width=3)
    window.mainloop()

if __name__ == '__main__':
    tuoyuan()

64.利用ellipse 和 rectangle 画图
此题py3.0已改为tk oval 和 rectangle
import tkinter as tk



def hua64():
    window = tk.Tk()
    window.title('画椭圆和矩形')
    window.geometry('800x800')

    canvas = tk.Canvas(window, width = 800, height = 800, bg = 'white')
    canvas.pack()
    canvas.create_rectangle(50, 50, 350, 250, outline='green', width=3, fill='pink')
    canvas.create_oval(50,50,350,250,outline='red',width=3,fill='darkblue')


    window.mainloop()

if __name__ == '__main__':
    hua64()


65.一个最优美的图案
此题我画一个50个点连线
import tkinter as tk
import math

def draw_lines():
    window = tk.Tk()
    window.title('50个点连线')
    window.geometry('600x600')

    canvas = tk.Canvas(window, width=600, height=600, bg='white')
    canvas.pack()
    center_x = 300
    center_y = 300
    radius = 200
    points = []
    for i in range(50):
        angle = i * (360 / 50)
        angle_rad = math.radians(angle)
        x = center_x + radius * math.cos(angle_rad)
        y = center_y + radius * math.sin(angle_rad)
        points.append((x, y))


    for point in points:
        canvas.create_oval(point[0]-3, point[1]-3, point[0]+3, point[1]+3, fill='green')


    for i in range(50):
        for j in range(i + 1, 50):
            canvas.create_line(points[i][0], points[i][1], points[j][0], points[j][1], width=1, fill='green')

    window.mainloop()

if __name__ == '__main__':
    draw_lines()


66.输入3个数a,b,c，按大小顺序输出。


def main_():
    print('请输入三个数，用空格隔开')
    a, b, c = map(int,input().split())
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a
    print(a,b,c)
if __name__ == '__main__':
    main_()

67.输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。


def main_():
    print('请输入数组',end='\n')
    ls = list(map(int, input().split()))
    max, min = 0, len(ls)-1
    for i in range(0, len(ls)):
        if ls[i] > ls[max]:
            max = i
        if ls[i] < ls[min]:
            min = i
    if max != 0:
        ls[0], ls[max] = ls[max], ls[0]
    if min == 0:
        min = max
    if min != len(ls)-1:
        ls[len(ls)-1], ls[min] = ls[min], ls[len(ls)-1]
    print(ls)

if __name__ == '__main__':
    main_()


67.有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数 m<n


def main_():
    print('请输入数组',end='\n')
    ls = list(map(int, input().split()))
    n = len(ls)
    print('请输入m', end='\n')
    m = int(input())

    # 后移m个
    lt = ls[-m:] + ls[:-m]
    print(lt)
if __name__ == '__main__':
    main_()


68.有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
def main_():
    print('请输入数组长度n:', end='\n')
    n = int(input())
    print('请输入要向后移的位置数m:', end='\n')
    m = int(input())
    p = [i + 1 for i in range(n)]

    p = p[-m:] + p[:-m]  # 切片

    print(f"移动后的数组是：{p}")

if __name__ == '__main__':
    main_()


69.有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
此问题也是约瑟夫环问题

def main_():
    n = input('请输入参加人数n')
    n = int(n)

    p = [i + 1 for i in range(n)]
    i = 1
    while(len(p) > 1):
        i = (i + 2)%len(p)
        p.pop(i)
        print(f'淘汰{i}号')

    print(f'剩下的为{p[0]}')

if __name__ == '__main__':
    main_()


70.写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。
def main_():
    s = input('请输入一个字符串')
    print(len(s))

if __name__ == '__main__':
    main_()


71.编写input()和output()函数输入，输出5个学生的数据记录。

def input_71():
    s = {}
    s['学号'] = input('请输入学号: ')
    s['姓名'] = input('请输入姓名: ')
    s['年龄'] = int(input('请输入年龄: '))
    s['性别'] = input('请输入性别: ')
    s['成绩'] = float(input('请输入成绩: '))
    return s


def output_71(s):
    print("\n学生信息记录：")
    print(f"{'学号':<10}{'姓名':<10}{'年龄':<10}{'性别':<10}{'成绩':<10}")
    for student in s:
        print(
            f"{student['学号']:<10}{student['姓名']:<10}{student['年龄']:<10}{student['性别']:<10}{student['成绩']:<10}")


def main():
    s = []
    for i in range(5):
        st = input_71()
        s.append(st)

    output_71(s)


if __name__ == '__main__':
    main()


72.创建一个链表。
此处创建一个单链表
def main():
    print('输入单链表表长n')
    n = int(input())
    p = []
    for i in range(n):
        item = input()
        p.append(item)
    print(p)

if __name__ == '__main__':
    main()



73.反向输出一个链表。

def main():
    print('输入单链表表长n')
    n = int(input())
    p = []
    for i in range(n):
        item = input()
        p.append(item)
    p.reverse()
    print(p)

if __name__ == '__main__':
    main()


74.列表排序及连接。

def main():
    print('请输入A列表')
    A = list(map(int,input().split()))
    print('请输入B列表')
    B = list(map(int, input().split()))

    A.sort()
    print(f'排序后的A为{A}')
    B.sort()
    print(f'排序后的B为{B}')

    print(f'排序后为{A+B}')



if __name__ == '__main__':
    main()


75.放松一下，算一道简单的题目。
此题为计算非递归方法阶乘代码
def main():
    n = print('要计算谁的阶乘？')
    n = int(input())
    sum = 1
    for i in range(n,1,-1):
        sum = sum * i
    print(f'阶乘为{sum}')
if __name__ == '__main__':
    main()


76.编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

def main():
    n = int(input())
    sum = 0
    if n % 2 == 0:
        for i in range(2,n+1,2):
            sum = sum + 1/i
    elif n % 2 != 0:
        for i in range(1,n+1,2):
            sum = sum + 1/i
    print(sum)
if __name__ == '__main__':
    main()


77.循环输出列表
def main():
    s = list(input().split())
    for i in s:
        print(i,end='\n')
if __name__ == '__main__':
    main()


78.找到年龄最大的人，并输出。

题目代码为2.0，下面代码逻辑不变，使用python3.0
def main():
    person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
    max = 'li'
    for key in person.keys():
        if person[max] < person[key]:
            max = key
    print(f'最大的人为{max},年龄为{person[max]}')

if __name__ == '__main__':
    main()


79.字符串排序。和数值排序一个逻辑

def main():
    str1 = input('第一个字符串为')
    str2 = input('第二个字符串为')
    str3 = input('第三个字符串为')
    if str1 > str2:
        str1, str2 = str2, str1
    if str2 > str3:
        str2, str3 = str3, str2
    if str1 > str2:
        str1, str2 = str2, str1

    print(f'排序后的字符串为{str1},{str2},{str3}')


if __name__ == '__main__':
    main()


80.海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
def main():
    t = 0
    while 1:
        t += 1
        count = t
        p = 1
        for i in range(5):
            if (count-1)%5 == 0:
                count = (count-1)//5*4
            else:
                p = 0
                break
        if p:
            print(f"最少有{t}个桃子")
            break


if __name__ == '__main__':
    main()

81.809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。

def main():
    for i in range(10,15):
        if (809*i == 800*i + 9*i) and (9*i > 100):
            break
    print(f'??为{i},结果为{809*i}')

if __name__ == '__main__':
    main()


82.八进制转换为十进制

def main():
    print('输入八进制的数字')
    n = input()
    sum = 0
    for i in range(0,len(n)):
        sum = sum + int(n[i])*8**(len(n)-1-i)
    print(sum)
if __name__ == '__main__':
    main()


83.求0—7所能组成的奇数个数。
def main():
    sum = 0
    for i in range(1,9):
        if i == 1:
            sum += 4
            print(sum)
        if i == 2:
            sum += 4*7
            print(sum)
        if i > 2 and i < 9 :
            sum += 4*8**(i-2)*7
            print(sum)
    print(sum)

if __name__ == '__main__':
    main()

84.连接字符串
def main():
    l = ['wo','shi','shuai','ge']
    print(' '.join(l))

if __name__ == '__main__':
    main()


85.输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。

def main():
    ji = int(input())
    t = 1
    sum = 9
    while t:
        if sum % ji == 0:
            print(sum)
            t = 0
        else:
            sum = sum*10 + 9

if __name__ == '__main__':
    main()


86.两个字符串连接程序。
def main():
    A = input()
    B = input()
    print(A+B)

if __name__ == '__main__':
    main()



87.回答结果（结构体变量传递）。
结构体变量为全局变量是会变化的
if __name__ == '__main__':
    class Student:
        x = 0
        c = 0
    def f(stu):
        stu.x = 20
        stu.c = 'c'
    a = Student()
    a.x = 3
    a.c = 'a'
    f(a)
    print(a.x, a.c)


88.读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。

def main():
    print('每次输入一个，输入7个数字,0-50')
    for i in range(7):
        n = int(input())
        print(n*'*')

if __name__ == '__main__':
    main()


89.某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
def main():
    print('每次输入加密后的数字:')
    num = input()
    num_list = list(num)
    num_list[0], num_list[3] = num_list[3], num_list[0]
    num_list[1], num_list[2] = num_list[2], num_list[1]

    l = []

    for i in num_list:
        i = (int(i)+10-5)%10
        l.append(str(i))

    print('解密后的数字为:', ''.join(l))


if __name__ == '__main__':
    main()

90.列表使用实例。
熟练使用len append等等列表函数即可

91.时间函数举例1
time函数 先import
time.time()为获取当前时间

92.时间函数举例2。
同上
用特定的题目来练习最好

93.时间函数举例3。
同上
用特定的题目来练习最好

94.时间函数举例4,一个猜数游戏，判断一个人反应快慢。
import time
import random

def main__():
    suiji = random.randint(1, 100)
    print("随机了一个1到100之间的数字，请猜它")
    t1 = time.time()
    b = 0
    while 1:
        a = int(input("请输入你猜的"))
        b += 1
        if a < suiji:
            print("太小")
        elif a > suiji:
            print("太大")
        else:
            print("高手，猜对了")
            break
    t2 = time.time()
    dt = t2 - t1
    print(f"{b}次后猜对")
    print(f"反应时间{dt:.2f}")
if __name__ == '__main__':
    main__()

95.字符串日期转换为易读的日期格式
from datetime import datetime

def main__():
    datestr = '2024-11-12 18:53:26'

    date = datetime.strptime(datestr, '%Y-%m-%d %H:%M:%S')
    time = date.strftime('%Y %B %d, %H %M %p')
    print(time)
if __name__ == '__main__':
    main__()

96.计算字符串中子串出现的次数
def main__():
   str1 = input()
   str2 = input()
   print(str1.count(str2))
if __name__ == '__main__':
    main__()


97.从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止
def main__():
   with open('97.txt','w') as file:
       print('直到输入#之前都继续输入')
       while 1:
           s = input()
           if s == '#':
               break
           else:
                file.write(s)
if __name__ == '__main__':
    main__()


98.从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
def main__():
   with open('98.txt','w') as file:
       print('输入字符串')
       s = input()
       sx = s.upper()
       file.write(s)
if __name__ == '__main__':
    main__()

99.有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
def main__():
   with open('A.txt','r') as file:
       A = file.read()
   with open('B.txt','r') as file:
       B = file.read()
   with open('C.txt','w') as file:
        C = list(A+B)
        C.sort()
        s = ''.join(C)
        file.write(s)
if __name__ == '__main__':
    main__()

100.列表转换为字典
字典为映射关系，列表转字典可以使用在链表的数据结构中
这里讲BLG战队队员id和位置进行映射
def main__():
    A = ['bin', 'xun', 'knight', 'elk', 'on']
    B = ['top', 'jug', 'mid', 'xialu', 'bottom']

    dic = dict(zip(B, A))
    print(dic)
if __name__ == '__main__':
    main__()


