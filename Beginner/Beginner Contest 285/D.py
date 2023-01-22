from collections import defaultdict

N = int(input())

ST = [input().split() for _ in range(N)]
S = []
T = []
for i in range(N):
    S.append(ST[i][0])
    T.append(ST[i][1])


# def can_change_username(n, S, T) -> bool:
#     graph = defaultdict(list)
#     for i in range(n):
#         graph[S[i]].append(T[i])
#     visited = set()
#
#     def dfs(node):
#         visited.add(node)
#         for i in graph[node]:
#             if i not in visited:
#                 dfs(i)
#     for i in range(n):
#         if S[i] not in visited:
#             dfs(S[i])
#     return len(visited) == len(S)

# def is_possible_to_change(N, S, T):
#     graph = {}
#     indegree = {}
#
#     for i in range(N):
#         graph[S[i]] = T[i]
#         indegree[T[i]] = 0
#     for i in range(N):
#         if T[i] not in indegree:
#             return False
#         indegree[T[i]] += 1
#     queue = []
#     for i in range(N):
#         if indegree[S[i]] == 0:
#             queue.append(S[i])
#     cnt = 0
#     while queue:
#         node = queue.pop(0)
#         cnt += 1
#         if node in graph:
#             indegree[graph[node]] -= 1
#             if indegree[graph[node]] == 0:
#                 queue.append(graph[node])
#     return cnt == N
#
#
# print(is_possible_to_change(N, S, T))

# ユーザ名の変更を行う順序を格納するリスト
change_order = []

# 現在のユーザ名を格納する辞書
current_users = {}

# 全てのユーザのユーザ名を希望通り変更できるか判定
for i in range(N):
    # 現在のユーザ名が辞書に存在しない場合
    if S[i] not in current_users:
        current_users[S[i]] = T[i]
        change_order.append(i)
    # 現在のユーザ名が辞書に存在し、かつ希望のユーザ名と一致する場合
    elif current_users[S[i]] == T[i]:
        change_order.append(i)
    # 現在のユーザ名が辞書に存在し、かつ希望のユーザ名と一致しない場合
    else:
        print("全てのユーザのユーザ名を希望通り変更できません")
        break
else:
    print("全てのユーザのユーザ名を希望通り変更できます。 変更順序: ", change_order)
