# # 문제 1
#
# x = int(input())
# y = int(input())
# result = 1
#
# for i in range (y):
#     result = result * x
#     if i < y-1:
#         print(x,"* ",end='')
#     else:
#         print(x,"= ", end='')
#
# print(result,end='')
#
# # 문제 2
# password = "hipython"   #임의의 암호 지정
# i = 0
# while (i < 3):
#     login = input("비밀번호 : ")  # 입력받기
#     if password == login:
#         print("로그인 되었습니다!")
#         break
#     else:
#         print("비밀번호를 다시 입력하세요")
#     i += 1
#
# if (i >= 3):
#     print("로그인 실패! 횟수초과!")
#
#
# # 문제 3
# def toUpper(string):
#     return string.upper()
#
# def reverseList(mylist):
#     return list(reversed(mylist))
#
# arr = [10,3.5,"python",100]
# arr[2] = toUpper(arr[2])
# print(arr)
#
# arr[1] = [1.0,2.1,3.1]
# print(arr)
#
# arr[1] = reverseList(arr[1])
# print(arr)
#
# arr[1][0] = 3.5
# print(arr)
#
# del(arr[2:])
# arr.append(50)
# print(arr)
#
# for i in range (60, 90, 10):
#     arr.append(i)
# print(arr)
#
# print("마지막원소 추출 : ",arr.pop())
# print(arr)
#
# print("index1 요소 pop 추출 : ",arr.pop(1))
# print(arr)
#
# # 문제 4
# arr = []
#
# i = int(input("정수 입력 : "))
# while (i != 0):
#     arr.append(i)
#     i = int(input("정수 입력 :"))
# print(arr)
# print()
# print("역순 :",end='')
# print()
#
# for i in list(reversed(arr)):
#     print(i,end=' ')
# print()
#
# add = int(input("삽입 정수 : "))
# idx = int(input("삽입할 인덱스 : "))
# if idx not in range(0,len(arr)):
#     print("index의 범위에 맞지 않습니다!!!")
# else:
#     arr.insert(idx, add)
#
# print(arr)
# print()
#
# delidx = int(input("삭제할 정수 : "))
# try:
#     arr.remove(delidx)
#
# except:
#     print(delidx,"는 존재하지 않습니다!")
# print(arr)
# print("역순 :",list(reversed(arr)))
# print("정렬 :",list(sorted(arr)))
#
# # 문제 5
# Bloods = []
# for i in range (10):
#     Bloods.append(input("헌열할 혈액형 (a, b, ab, o) : "))
# print("저장된 혈액형 : ",Bloods)
# print("A 혈액형 수 :",Bloods.count('a'))
# print("B 혈액형 수 :",Bloods.count('b'))
# print("AB 혈액형 수 :",Bloods.count('ab'))
# print("O 혈액형 수 :",Bloods.count('o'))
#
# # 문제 6
# arr = [['A',80,80,80],['A',90,90,90],['B',60,70,80],
#        ['A',71,78,77],['B',70,80,73],['B',90,87,92]]
#
# listA = []
# listB = []
#
# print("원본 데이터")
# for i in arr:
#     print(i)
#     if (i[0] == 'A'):
#         listA.append(round(sum(i[1:])/3, 1))
#
#     else:
#         listB.append(round(sum(i[1:])/3, 1))
#
# print()
# print("listA, listB 출력")
# print("A :",listA,"\nB :",listB)
#
# print()
# print("리스트 역순 출력")
# print("A 역순 :",list(reversed(listA)),"\nB 역순 :",list(reversed(listB)))
#
# print()
# print("최대값, 최소값, 합계")
# print("listA 최대값 :",max(listA),"최소값 :",min(listA),"합계 :",sum(listA))
# print("listA 최대값 :",max(listB),"최소값 :",min(listB),"합계 :",sum(listB))
#
# # 문제 7
# quiz = (["3+2",5,3], ["5/2",2.5, 5], ["10 - 2", 8, 3],
#         ["2의 3승",8, 4], ["5-2*2",1,5])
# score = [0,0,0] #정답, 오답, 점수 순서임
#
# for i in quiz:
#     answer = int(input(i[0]+' : '))
#     if i[1] == answer:
#         score[2] += i[2]
#         score[0] += 1
#     else:
#         score[1] += 1
#
# print("정답 수 :",score[0])
# print("오답 수 :",score[1])
# print("점 수 :",score[2])
#
# # 문제 8
#
# dogtype = []
# for i in range (3):
#     info = {'name' : input('강아지 이름 :'), 'age' : int(input('강아지 나이 : ')), 'kind' : input('강아지 종류 : ')}
#     dogtype.append(info)
#
# print("리스트 내용")
# for idx, form in enumerate(dogtype):
#     print(idx,"번째 :", form)
#
# print("나이가 3살 이상인 강아지")
# for age in dogtype:
#     if (age['age'] >= 3):
#         print(age)
#
# # 문제 9
# def computing(param1, param2):
#     if param1 < param2:
#         temp = param1
#         param1 = param2
#         param2 = temp
#
#     return {'plus' : param1 + param2, 'minus' : param1 - param2, 'multi' : param1 * param2, 'div': int(param1 / param2)}
#
# first = int(input("0이 아닌 정수 입력 :"))
# last = int(input("0이 아닌 정수 입력 :"))
# returns = computing (first, last)
# for i in returns.keys():
#     print(i,' = ',returns[i], end=' ')

# # 문제 10
# def find_max(*values):
#     print("max",values," = ",end='')
#     max = 0
#     for value in values:
#         if value > max:
#             max = value
#     return max
#
# ar = []
# result = []
#
# for i in range(5):
#     ar.append(int(input("정수 입력 : ")))
#
# print("max() = 0")
# print("max(",ar[0],") = ",ar[0])
# ar2 = []
# ar2.append(ar[0])
#
# for j in range (1, 5):
#     ar2.append(ar[j])
#     print(find_max(*ar2))

#second 1번

amount = int(input("투자 액수를 입력하세요 :"))
while (amount < 100 or amount > 10000):
    print("#다시 입력해주세요")  # 이부분은 지워도 됩니다
    amount = int(input("투자 액수를 입력하세요 :"))

date = int(input("투자한 날짜 수를 입력하세요 :"))
while (date < 1 or date > 10):
    print("#다시 입력해주세요")  # 이부분은 지워도 됩니다
    date = int(input("투자한 날짜 수를 입력하세요 :"))

remains = amount
va = []
i = 0
while (i < date):

    us_input = (int(input(str(i+1)+"일차 변동 데이터를 입력하세요 :")))/ 100
    if us_input < -100 or us_input > 100:
        print("#다시 입력해주세요") # 이부분은 지워도 됩니다
        continue
    remains = remains + remains * (us_input)
    i = i + 1
result = int(remains - amount)

print(result)
print("이득입니다" if result > 0 else "손해입니다" if result < 0 else "본전입니다")
