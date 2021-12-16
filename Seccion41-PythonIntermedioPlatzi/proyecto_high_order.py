DATA = [
    {
        "name": "Facundo",
        "age": 72,
        "organization": "Platzi",
        "position": "Techical Coah",
        "language": "python",
    },
    {
        "name": "Luisiana",
        "age": 33,
        "organization": "Platzi",
        "position": "UX Designer",
        "language": "javascript",
    },
    {
        "name": "Hector",
        "age": 19,
        "organization": "Platzi",
        "position": "Associate",
        "language": "ruby",
    },
    {
        "name": "Gbriel",
        "age": 52,
        "organization": "Platzi",
        "position": "Data science",
        "language": "python",
    },
    {
        "name": "Jose",
        "age": 29,
        "organization": "Platzi",
        "position": "Devops",
        "language": "python",
    },
    {
        "name": "Adrian",
        "age": 60,
        "organization": "Platzi",
        "position": "Techical Coah",
        "language": "python",
    },
    {
        "name": "Mariana",
        "age": 45,
        "organization": "Platzi",
        "position": "Techical Coah",
        "language": "python",
    },
]


def run():
    all_python_devs = [
        worker["name"] for worker in DATA if worker["language"] == "python"
    ]
    all_Platzi_workers = [
        worker["name"] for worker in DATA if worker["organization"] == "Platzi"
    ]

    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    # perosnas de edad alta
    for worker in old_people:
        print(worker)

    # perosnas que traajn en workd
    for worker in all_Platzi_workers:
        print(f"trabajadores platzi {worker}")

    # personas qeu tabajan como devs
    for worker in all_python_devs:
        print(f"desarrollador en python {worker}")


if __name__ == "__main__":
    run()
