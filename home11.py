#######################################################
w = "Lorem elit ipsum dolor sit amet consectetur, sit adipisicing" 
w2 = "Lorem elit Exercitationem, dolorum elit"
w3 = "sit adipisicing elit"
w4 = "Lorem elit non pro id"
res = []

s = set(w.split()).intersection( set(w2.split()) )
s2 = set(w3.split()).intersection( set(w4.split()) )
print(s.intersection(s2))

#######################################################
def maxNum(data):
    if type(data) == dict:
        ma = max(data.values())
    return ma

data = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print(maxNum(data))

#######################################################

def createSet(t, t2):
    if type(t) == tuple and type(t2) == tuple:
        return set(t).intersection(set(t2))
    return {}

t = (1, 2, 3, 4, 5, 6)
t2 = (2, 3, 4, 5, 6, 7)
print(createSet(t, t2))

#######################################################


def symbols(s: str):
    if type(s) == str:
        return " ".join([i for i in s if not i.isalnum() and i != " "])
    return 0

s = "Lore!m elit ip.sum dolor sit amet consectetur, sit adipisicing"

print(symbols(s))
#######################################################
d = {"a": 1, "b": 2, "c": 3, "d":4, "e":5}
d2 = {"a": 111, "b": 34, "c": 3, "d":4, "e":87}

print( list( set(d.values() ).intersection(set(d2.values()))  ))
