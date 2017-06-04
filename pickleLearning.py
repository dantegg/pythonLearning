import pickle


class Bird(object):
    have_feather = True
    reproduction_method = "egg"

summer = Bird()
# pickle_string = pickle.dumps(summer)

# with open("summer.pkl", "wb") as f:
#     f.write(pickle_string)


with open("summer.pkl", "wb") as f:
    pickle.dump(summer, f)

with open("summer.pkl", "rb") as f:
    summer = pickle.load(f)

print(summer.have_feather)