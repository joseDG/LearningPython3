
def argmax(lst):
    # Given a list: return the idx of the maximum value
    # Return None for an empty list
    if len(lst) == 0:
        return None
    return lst.index(max(lst))


def top2_argmax_v1(lst):
    # Given a list: return the indices of the first and second maximum
    if len(lst) < 2:
        return None, None

    # get top max position and value
    max1_pos = argmax(lst)
    max1_val = lst[max1_pos]

    # replace it with a very small value
    mn_value = min(lst)
    lst[max1_pos] = mn_value - 1

    max2_pos = argmax(lst)

    # undo the change to the list
    lst[max1_pos] = max1_val

    return max1_pos, max2_pos

def main():
    lst = list(map(int, input().split()))

    max1_pos, max2_pos = top2_argmax_v1(lst)

    if max1_pos is not None:
        print('idx1', max1_pos, 'value', lst[max1_pos])
        print('idx2', max2_pos, 'value', lst[max2_pos])



main()


