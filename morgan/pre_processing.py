import pandas as pd

class Preprocessing :

    def __init__(self) -> None:
        pass
    
    def importation(self, chemin : str) -> pd.DataFrame :
        data = pd.read_csv(chemin)
        return data
    
    def selection_predicteurs(self, data : pd.DataFrame, Pred : list) -> pd.DataFrame :
        return data[Pred]
    
    def suppression_ligne_sans_val(self, data = pd.DataFrame) -> pd.DataFrame :
        missing_by_row = data.isnull().sum(axis=1)
        for i in range(len(missing_by_row)):
            if missing_by_row[i]>=3  :
                data=data.drop(i)
        return data

    def imputation_val_manquantes(self, data : pd.DataFrame, method : 'str') -> pd.DataFrame :
        if  method == 'mean' :
            for column in data.columns :
                data[column].fillna(data[column].mean(), inplace=True)
        elif method == 'median' :
            for column in data.columns :
                data[column].fillna(data[column].median(), inplace=True)
        else :
            print('méthode non existante')
        return data
