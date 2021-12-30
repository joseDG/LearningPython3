from datetime import datetime


def get_numbers(string):
    items = string.split(' ')
    return int(items[0]), int(items[1])


def compute_increment(lst):
    for row in range(1, len(lst)):
        cur_lst = lst[row].split('\t')
        cur_line = cur_lst[0]
        for col in range(1, len(cur_lst)):
            prev_lst = lst[row - 1].split('\t')
            prev_rating, prev_reg = get_numbers(prev_lst[col])
            cur_rating, cur_reg = get_numbers(cur_lst[col])

            dif = max(0, cur_reg - prev_reg)
            cur_line += '\t{} {} +{}'.format(cur_rating, cur_reg, dif)

        lst[row] = cur_line
    return lst


def compress(path):
    with open(path) as f:
        lines = f.read().splitlines()

    # iterate on the file to filter it
    # skip all invalid lines
    lines = [line for line in lines if 'NA' not in line]

    # For valid lines; per day, keep only the last day
    result = []
    for idx, line in enumerate(lines):
        day = line.split('\t')[0].split(' ')[0]

        if idx == len(lines) - 1:   # last line in the file: add it
            result.append(line)
        else:                       # extract day of the next entry
            next = lines[idx+1].split('\t')[0].split(' ')[0]
            if day != next:         # different day: so I am last
                result.append(line)

    # given a filtered file, compute the differences!
    return compute_increment(result)


if __name__ == '__main__':
    input_path = 'courses.txt'

    now = datetime.now()
    cur_date = now.strftime("%Y-%m-%d %H:%M:%S")
    output_path = f'courses-output-{cur_date}.txt'

    lst = compress(input_path)

    with open(output_path, 'w+') as f:
        for line in lst:
            f.write(line + '\n')

