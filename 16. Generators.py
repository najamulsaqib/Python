def top10():

    for i in range(11):
        sq = i*i
        yield sq # using yield statement ve can create generators
        print(":)") #Unlike return here we can use statements after yield



val = top10()

for i in val:
    print(i)
    