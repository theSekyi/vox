import                      pandas as pd
from                                           sklearn.datasets import load_iris

data =                                   load_iris()


def load_dataset(data):
    labels = data.target_names
    df = pd.DataFrame(data, columns=labels)
    return df


print(load_dataset(data))
