import numpy as np

S = np.array(list(input()))
S = np.append(S, '1')
T = np.array(list(input()))
ans = (S == T).tolist().index(False)

print(ans + 1)
