from script import load_dataset
from sklearn.datasets import load_iris

data = load_iris()

def test_no_columns():
    df = load_dataset(data)
    assert len(df.columns) == 3

def test_columns():
    df = load_dataset(data)
    column_names = list(df.columns)
    assert column_names == ["setosa", "versicolor", "virginica"]