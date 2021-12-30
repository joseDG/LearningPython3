

import glob
import time
from datetime import datetime

def get_web_content(url):
    """
    Given a URL, return the html CONTENT
    """
    import urllib.request as urllib2

    filedata = urllib2.urlopen(url)
    datatowrite = filedata.read()

    return datatowrite.decode("utf-8")


def get_number(str):
    str = str.replace(',', '')
    lst = list(str)

    for pos in range(len(lst)):
        if not lst[pos].isdigit():
            lst[pos] = ' '

    try:
        return int(''.join(lst))
    except:
        return -1



def extract_number(ret, keyword):
    for i in range(10):
        pos = ret.find(keyword)

        if pos == -1:
            break

        str = ret[pos - 12: pos - 1]
        val = get_number(str)

        if val != -1:
            return val

        ret = ret[pos+5:]

    return -1

def extract_data(url):
    ret = get_web_content(url)

    ratings = extract_number(ret, 'ratings')

    if ratings == -1:
        return -1, -1



    pos = ret.find('ratings')

    if pos == -1:
        return -1, -1

    ret = ret[pos:]

    students = extract_number(ret, 'students')

    return ratings, students

def extract_data111(url):
    ret = get_web_content(url)

    pos = ret.find('Created by')
    cur = pos - 200
    while cur > 0:
        ss = ret[cur : pos]
        if ss.find('ratings') != -1:
            break
        cur -= 100

    cur = max(0, cur - 100)
    ret = ret[cur: pos]

    pos = ret.find('ratings')
    ret = ret[pos + 10:]
    pos = ret.find('ratings')
    ratings_str = ret[pos - 10: pos - 1]
    ratings = get_number(ratings_str)
    ret = ret[pos:]
    pos = ret.find('students')
    students_str = ret[pos - 10: pos - 1]
    students = get_number(students_str)

    return ratings, students


def compute(path):
    sleep_sec = 1
    import time
    now = datetime.now()
    result = now.strftime("%Y-%m-%d %H:%M:%S") + '\t'

    with open(path) as f:
        lines = f.read().splitlines()

    for url in lines:
        try:
            ratings, students = extract_data(url)
            result += '{} {}\t'.format(ratings, students)
        except:
            result += 'NA\t'

        if sleep_sec > 0:
            time.sleep(sleep_sec)


    return result


if __name__ == '__main__':
    langs = ['cpp', 'java', 'python', 'javascript', 'dsalgo', 'mlds']
    inpath = '/home/moustafa/workspaces/git/most-pythons-helper-github/tools/udemy/courses/{}.txt'
    outpath = '/home/moustafa/workspaces/git/most-pythons-helper-github/tools/udemy/outputs/{}.txt'

    while True:
        print('Udemy Tracker')
        for lang in langs:
            ret = compute(inpath.format(lang))

            with open(outpath.format(lang), 'a') as f:
                f.write(ret + '\n')

        print('Sleep')
        time.sleep(20 * 60)

