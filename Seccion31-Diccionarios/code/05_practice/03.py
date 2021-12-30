
if __name__ == '__main__':

    lst = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    dict = {}
    for idx, value in enumerate(lst):
        dict[value] = idx

    for q in queries:
        ans = dict.get(q, -1)
        print(f'Query {q} answer {ans}')

"""
-1000 500 -1000 70 2 2 70 3 20 20
2 3 20 70 500 -1000  999
"""