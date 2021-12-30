


def init():
    class CustomersDataBase:
        def load_database(self):
            nonlocal users_ids
            users_ids += [3, 4]

        def add_id(self, id):
            if id not in users_ids:
                print(f'Adding {id}')
                # doesn't need nonlocal
                users_ids.append(id)
                print(users_ids)
            else:
                print(f'{id} is already there')

    users_ids = [1, 2]
    db = CustomersDataBase()
    db.load_database()

    return db.add_id


def go1(adder):
    adder(4)
    adder(5)

def go2(adder):
    adder(6)

if __name__ == '__main__':
    id_adder = init()
    go1(id_adder)
    go2(id_adder)
"""
4 is already there
Adding 5
[1, 2, 3, 4, 5]
Adding 6
[1, 2, 3, 4, 5, 6]
"""