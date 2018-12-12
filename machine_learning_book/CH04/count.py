#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
#!/usr/bin/python
#-*- coding:utf-8 -*-
#there is no ++ operator in python
import string
def main():
	s = input('input a string')
	letter = 0
	space = 0
	digit = 0
	other = 0
	for c in s:
		if c.isalpha():letter += 1
		elif c.isspace():space += 1
		elif c.isdigit():digit += 1
		else :other += 1
	print('There are %d letters,%d spaces,%d digits,%d other characters in your string'%(letter,space,digit,other)) 

if __name__ == '__main__'
	main()

#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字
#!/usr/bin/python
#-*- coding:utf-8 -*-
def main():
	basis = int(input('input the basis number:'))
	n = int(input('input the longest length of the number:'))
	b = basis
	sum = 0
	for i in range(0,n):
		if i == n-1:
			print("%d" %(basis))
		else :
			print("%d +"%(basis))
		sum += basis
		basis = basis*10 + b
	print('= %d'%(sum))
if __name__ == '__main__':
	main()

#一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程
# 找出1000以内的所有完数。
from math import sqrt
n = int(input('input a number:'))
sum = n-1
k = int(sqrt(n))
for i in range(1,k+1):
	if n%i == 0:
		sum += n/i
		sum += i
if sum == n:
	print('Yes')
else:
	print('no')


