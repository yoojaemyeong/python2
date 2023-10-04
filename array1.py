##### 배열 원소 개수 구하기 #####
# (문제)입력으로 크기 n인 정수형 배열 A와 정수 k가 주어진다. 배열 A의 원소는 a0,a1,...,an-1이다. 
# 배열 A의 원소 중에서 값이 k인 원소의 개수를 출력하자
# (입력) 첫번째 줄에 정수 n과 k가 공백을 사이에 두고 순서대로 주어진다.
#        두번째 줄에 배열 A의 원소 a0,a1,...,an-1이 공백을 사이에 두고 순서대로 주어진다.
# (출력) 첫번째 줄에 배열 A의 원소중에서 값이 k인 원소의 개수를 출력한다.
def solution(n,A,k):
    answer = 0
    for a in A:
        if a == k:
            answer += 1
    return answer

# 입력을 받고, 정답을 출력한다.
n,k=map(int, input().split())
A = list(map(int,input().split()))
print(solution(n,A,k))
