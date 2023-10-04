##### 배열 단일 업데이트 #####
# (문제) 크기가 n인 정수형 배열 A가 주어진다. 배열 A의 원소는 a0,a1,a2,...,an-1이다.
#        입력으로 i,j,k가 주어지면 배열 A의 i번째 원소ai부터 j번째 원소 aj에 k를 곱하는 연산을 수행하자.
#        연산을 수행한 후 배열 A의 모든 원소의 합을 출력하자
# (입력) 첫번째 줄에 n이 주어진다.
#        두번째 줄에 배열 A의 원소 a0,a1,a2,...,an-1이 공백을 사이에 두고 순서대로 주어진다.
#        세번째 줄에 i,j,k가 공백을 사이에 두고 순서대로 주어진다. 
# (출력) 첫번째 줄에 연산을 수행한 후 배열 A의 모든 원소의 합을 출력한다.
def solution(n,A,i,j,k):
    for idx in range(i,j+1):
        A[idx] = A[idx]*k
    return sum(A)

# (입력)
n = map(int, input().split())
A = list(map(int,input().split()))
i,j,k = map(int, input().split())
print(solution(n,A,i,j,k))
