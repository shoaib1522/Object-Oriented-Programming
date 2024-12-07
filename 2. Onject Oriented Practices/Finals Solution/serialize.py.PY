import pickle

data = {'name': 'John', 'age': 30, 'city': 'New York'}
data2=  {'name': 'Shoaib', 'age': 90, 'city': 'Lahore'}
data3=[1,2,556]
a=125

# Serialize the data
with open('data.pickle', 'wb') as file:
    pickle.dumps(data, file)
    pickle.dump(data2, file)
    pickle.dump(data3, file)
    pickle.dump(a,file)


