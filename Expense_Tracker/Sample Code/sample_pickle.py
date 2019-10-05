# example use of pickle - taken off stack overflow
# pickled files are used as a mini-database 
# use dictionaries to store my data

import pickle

a = {'hello': 'world'}

with open('filename.pickle', 'wb') as handle:
    pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('filename.pickle', 'rb') as handle:
    b = pickle.load(handle)

print (a == b)