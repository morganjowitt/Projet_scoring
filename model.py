    
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

class ModeleRegLog :

    def __init__(self) -> None:
        pass

    def entraîner_modele_et_predire(self, data : pd.DataFrame, var_cible : str, choix_modele : str) -> None :

        X = data.drop(columns=[var_cible])
        y = data[var_cible]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        if choix_modele == 'regression_logistique' :
            modele = LogisticRegression(max_iter=1000)
        elif choix_modele == 'random_forest' : 
            modele = RandomForestClassifier(n_estimators=25)
        else : print("modele non valide")

        modele.fit(X_train, y_train)
        y_pred = modele.predict(X_test)
        return y_pred, y_test

    def metriques (self, y_pred, y_test ) :
        accuracy = accuracy_score(y_test, y_pred)
        conf_matrix = confusion_matrix(y_test, y_pred)
        class_report = classification_report(y_test, y_pred)
        print(f"Accuracy: {accuracy}")
        print("Confusion Matrix:")
        print(conf_matrix)
        print("Classification Report:")
        print(class_report)
