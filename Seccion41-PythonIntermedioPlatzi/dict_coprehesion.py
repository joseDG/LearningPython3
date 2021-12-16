def run():

    my_dict = {i: i ** 3 for i in range(1, 101) if 1 % 3 != 0}
    print(my_dict)


if __name__ == "__main__":
    run()
