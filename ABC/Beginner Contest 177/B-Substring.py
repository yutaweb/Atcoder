import numpy as np

S = np.array(list(input()))
T = np.array(list(input()))

count_list = []
ans = 10**19
for i in range(len(S) - len(T) + 1):
    count_list.append(np.count_nonzero(S[i:i+len(T)] != T))

print(min(count_list))
