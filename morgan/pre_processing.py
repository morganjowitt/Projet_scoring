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
    
    def entraîner_modele_et_predire_reg_log(self, data : pd.DataFrame, var_cible : str) -> None :

        X = data.drop(columns=[var_cible])
        y = data[var_cible]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        logistic_model = LogisticRegression(max_iter=1000)
        logistic_model.fit(X_train, y_train)
        y_pred = logistic_model.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        conf_matrix = confusion_matrix(y_test, y_pred)
        class_report = classification_report(y_test, y_pred)
        print(f"Accuracy: {accuracy}")
        print("Confusion Matrix:")
        print(conf_matrix)
        print("Classification Report:")
        print(class_report)

