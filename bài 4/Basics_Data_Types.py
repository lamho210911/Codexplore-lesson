#Basic Data Types:
'''
Các kiểu dữ liệu cơ bản trong python: bool, None,int,float,str
'''

#Topic #0 bool& none
#bool:true & False
var_bool = True

#[] type(): Dynamically typed
print(type(var_bool))

# Numerrically, they're evaluated as interers with value 1 (True), 0 (False)
a = 4 + True
print(a)

b = False
if b == 0:
    print("B is zero")

# [] None:Phần Tử Không 
var_none = None
print(type(var_none))

#None is often used as a placeholder for optinal or missing value
#It evaluates as False in conditionals
#email_address = None #False
email_address = "codexplore@youtube.com"

if email_address:
    print(f"Email address is {email_address}")
else:
    print(f"Email address is empty or {email_address}")

#Topic 1:Number (int & float)
# [] Numbers: int (Integer = Số nguyên) &float (Floating ponit numbers = Số thực)
print(type(1))#int
print(type(0))
print(type(-10))

print(type(0.0))#float
print(type(2.3))
print(type(4E2)) # Kết quả in ra: <class 'float'> 4*10(^2)
print(4E2, type(4E2)) # Kết quả in ra: 400.0 <class 'float'>

#[] Arithmetic: Các Phép Toán: +-*/ ** / // %
# print(10 + 3)# 13
# print(10 - 3)# 7
# print(10 * 3)# 30
# print(10 ** 3)# 10^3 = 10*10*10 = 1000
# print(10 / 3)# 3.3333333333333335
# print(10 // 3)#3
# print(10 % 3)#1 vì 10 chia 3 = 3 dư 1

# [] Basic Function (Hàm cơ bản)
print(pow(10,3))#10**3 = 1000
print(abs(-6.9))#6.9
print(round(6.69)) #7
round(round(5.468, 2))#5.47 --> round to nth digit
print(bin(512))# '0b100000000' --> binary format
print(hex(512))# '0x200' --> hexadecimal format