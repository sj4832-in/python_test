'''
 풍덕고 1학년 학생 n명이 급식을 먹기 위해 한 줄로 줄을 섰다.
 줄을 설 수 있는 경우의 수를 다음 조건에 유의하여 작성해보자.
'''


# 각 과목의 점수를 키보드로 입력받는다.
num = int(input("1학년 학생이 몇명인가요?"))

# n번만큼 반복하면서 곱한다.
sum = 1
for i in range(0, num):
    sum *= (num-i)

print("경우의 수:", sum)
