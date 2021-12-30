
if __name__ == '__main__':

    lst = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    dict = {}
    for idx, value in enumerate(lst):
        dict.setdefault(value, [])
        dict[value].append(idx)

    for q in queries:
        ans = dict.get(q, -1)
        print(f'Query {q} answer {ans}')
