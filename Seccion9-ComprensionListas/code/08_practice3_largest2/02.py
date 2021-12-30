
def top2_argmax_v2(lst):
    # Given a list: return the indices of the first and second maximum
    if len(lst) < 2:
        return None, None

    # Use the first 2 positions for the top 2 max
    max1_pos, max2_pos = 0, 1
    if lst[max1_pos] < lst[max2_pos]:
        max1_pos, max2_pos = 1, 0

    # Iterate and update the indices based on current element if bigger
    for cur_pos in range(2, len(lst)):
        if lst[max1_pos] < lst[cur_pos]:
            max1_pos, max2_pos = cur_pos, max1_pos
        elif lst[max2_pos] < lst[cur_pos]:
            max2_pos = cur_pos

    return max1_pos, max2_pos


def main():
    lst = list(map(int, input().split()))

    max1_pos, max2_pos = top2_argmax_v2(lst)

    if max1_pos is not None:
        print('idx1', max1_pos, 'value', lst[max1_pos])
        print('idx2', max2_pos, 'value', lst[max2_pos])



main()


