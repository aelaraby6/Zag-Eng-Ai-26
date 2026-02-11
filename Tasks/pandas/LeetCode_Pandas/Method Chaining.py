import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    heavy_animals = animals[animals['weight'] > 100]
    return heavy_animals.sort_values(by='weight', ascending=False)[['name']]