def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "Garcia"}

    super_list = [
        {"firstname": "Jose", "lastname": "Diaz"},
        {"firstname": "Jose", "lastname": "Diaz"},
        {"firstname": "Jose", "lastname": "Diaz"},
        {"firstname": "Jose", "lastname": "Diaz"},
        {"firstname": "Jose", "lastname": "Diaz"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5, 6],
        "integer_nums": [1, 2, 3, 4, 5, 6],
        "floating_nums": [1, 2, 3, 4, 5, 6],
    }

    for key, value in super_dict.items():
        print(key, " - ", value)


if __name__ == "__main__":
    run()
