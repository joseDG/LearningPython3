

import pickle
# Pickle serializes objects in a file.
# Serialization is the process of converting an object into a stream of bytes

data = (2021, '4444', ((7, 'wow'), [4, 5]))
lst = [1, 251221, 30000]    # > 256

with open("data.pickle", "wb") as pickle_file:
    pickle.dump(data, pickle_file)
    pickle.dump(lst, pickle_file)
