import pandas as pd

columns = ["a","b","c","d","e","f"]
informacoes = [[1,2,3,4,5,6]]
a = pd.DataFrame(informacoes, columns = columns)
iterator = list(a["b"])
print(iterator)
