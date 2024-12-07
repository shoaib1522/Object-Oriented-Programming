import pickle

# Deserialize the data
with open('data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)
    loaded_data2 = pickle.load(file)
    loaded_data3 = pickle.load(file)
    loaded_data4 = pickle.load(file)

print(loaded_data)
print(loaded_data2)
print(loaded_data3)
print(loaded_data4)