from pre_processing import Preprocessing
from model import ModeleRegLog

class Workflow :

    def __init__(self) -> None :
        self.preprocess = Preprocessing()
        self.model = ModeleRegLog()
        self.chemin="/Users/morganjowitt/Desktop/MOSEF/scoring/Projet_scoring/data/hmeq.csv"
        self.var_cible = 'BAD'
        self.method_fillna = 'mean'
        self.pred =['DELINQ','CLAGE','NINQ','DEROG','BAD']
        self.choix_modele = 'random_forest' # soit regression_logistique soit random_forest
        pass

    def processing(self) -> None :
        data = self.preprocess.importation(self.chemin)
        data_selection_predicteurs = self.preprocess.selection_predicteurs(data, self.pred)
        data_sans_ligne_vide = self.preprocess.suppression_ligne_sans_val(data_selection_predicteurs)
        data_sans_na = self.preprocess.imputation_val_manquantes(data_sans_ligne_vide, self.method_fillna)
        return data_sans_na

    def entrainer_et_evaluer(self, data) :
        y_pred, y_test = self.model.entraîner_modele_et_predire(data, self.var_cible, self.choix_modele)
        self.model.metriques(y_pred, y_test)

workflow  = Workflow()
data_process = workflow.processing()
workflow.entrainer_et_evaluer(data_process)
