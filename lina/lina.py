#import des bibliothèques
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2_contingency
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

#Comprendre et Visualiser les Données
df= pd.read_csv('C:\\Users\\benze\\OneDrive\\Bureau\\M2 MOSEF 2024-2025\\Scoring\\Projet_scoring-1\\Projet_scoring\\data\\hmeq.csv')
df_describe=df.describe(include='all')

#Analyse et Gestion des Valeurs Manquantes
print(df.isnull().sum())

plt.figure(figsize=(12, 8))  
sns.heatmap(df.isnull(), cbar=False, cmap='coolwarm', yticklabels=False, 
            cbar_kws={'label': 'Valeurs Manquantes'})
plt.title('Carte des valeurs manquantes dans le DataFrame', fontsize=18)


def tschuprow_coefficient(df, col1, col2):
    contingency_table = pd.crosstab(df[col1], df[col2])
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    n = contingency_table.sum().sum()
    r, c = contingency_table.shape
    tschuprow = np.sqrt(chi2 / n) / np.sqrt(min(r - 1, c - 1))

    return tschuprow
coeff_tschuprow = tschuprow_coefficient(df, 'REASON', 'JOB')
print(f"Le coefficient de Tschuprow entre REASON et JOB est : {coeff_tschuprow}")

df_value_cleaned = df['LOAN'].dropna()
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
sns.distplot(df['LOAN'], kde=True, ax=ax[0])
ax[0].set_title('Distribution de LOAN')
sns.boxplot(x=df['LOAN'], ax=ax[1])
ax[1].set_title('Boxplot de LOAN')

df_value_cleaned = df['MORTDUE'].dropna()
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
sns.distplot(df_value_cleaned, kde=True, ax=ax[0])
ax[0].set_title('Distribution de MORTDUE')
sns.boxplot(x=df_value_cleaned, ax=ax[1])
ax[1].set_title('Boxplot de MORTDUE')




df_value_cleaned = df['YOJ'].dropna()
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
sns.distplot(df_value_cleaned, kde=True, ax=ax[0])
ax[0].set_title('Distribution de YOJ')
sns.boxplot(x=df_value_cleaned, ax=ax[1])
ax[1].set_title('Boxplot de YOJ')


df_value_cleaned = df['DEROG'].dropna()
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
sns.distplot(df_value_cleaned, kde=True, ax=ax[0])
ax[0].set_title('Distribution de DEROG')
sns.boxplot(x=df_value_cleaned, ax=ax[1])
ax[1].set_title('Boxplot de DEROG')


df_value_cleaned = df['DELINQ'].dropna()
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
sns.distplot(df_value_cleaned, kde=True, ax=ax[0])
ax[0].set_title('Distribution de DELINQ')
sns.boxplot(x=df_value_cleaned, ax=ax[1])
ax[1].set_title('Boxplot de DELINQ')




df_value_cleaned = df['CLAGE'].dropna()
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
sns.distplot(df_value_cleaned, kde=True, ax=ax[0])
ax[0].set_title('Distribution de CLAGE')
sns.boxplot(x=df_value_cleaned, ax=ax[1])
ax[1].set_title('Boxplot de CLAGE')




df_value_cleaned = df['NINQ'].dropna()
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
sns.distplot(df_value_cleaned, kde=True, ax=ax[0])
ax[0].set_title('Distribution de NINQ')
sns.boxplot(x=df_value_cleaned, ax=ax[1])
ax[1].set_title('Boxplot de NINQ')


df_value_cleaned = df['CLNO'].dropna()
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
sns.distplot(df_value_cleaned, kde=True, ax=ax[0])
ax[0].set_title('Distribution de CLNO')
sns.boxplot(x=df_value_cleaned, ax=ax[1])
ax[1].set_title('Boxplot de CLNO')




df_value_cleaned = df['DEBTINC'].dropna()
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
sns.distplot(df_value_cleaned, kde=True, ax=ax[0])
ax[0].set_title('Distribution de DEBTINC')
sns.boxplot(x=df_value_cleaned, ax=ax[1])
ax[1].set_title('Boxplot de DEBTINC')

df_cleaned = df[df.isnull().sum(axis=1) < 6]

plt.figure(figsize=(12, 8))  
sns.heatmap(df_cleaned .isnull(), cbar=False, cmap='coolwarm', yticklabels=False, 
            cbar_kws={'label': 'Valeurs Manquantes'})
plt.title('Carte des valeurs manquantes dans le DataFrame', fontsize=18)


df_cleaned['MORTDUE'].fillna(df_cleaned['MORTDUE'].median(), inplace=True)
df_cleaned['DEBTINC'].fillna(df_cleaned['DEBTINC'].median(), inplace=True)
df_cleaned['CLAGE'].fillna(df_cleaned['CLAGE'].median(), inplace=True)
df_cleaned['NINQ'].fillna(df_cleaned['NINQ'].median(), inplace=True)
df_cleaned['DEROG'].fillna(0, inplace=True)  
df_cleaned['DELINQ'].fillna(0, inplace=True)  
df_cleaned['CLNO'].fillna(df_cleaned['CLNO'].median(), inplace=True)  
df_cleaned['YOJ'].fillna(df_cleaned['YOJ'].median(), inplace=True)  
df_cleaned.drop(columns=['VALUE'], inplace=True) 

df_encoded = pd.get_dummies(df_cleaned, columns=['REASON', 'JOB'])

correlation_matrix = df_encoded.corr()
plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

numeric_cols = ['LOAN', 'MORTDUE', 'YOJ', 'DEROG', 'DELINQ', 'CLAGE', 'NINQ', 'CLNO', 'DEBTINC']
df_encoded[numeric_cols].hist(bins=30, figsize=(15, 10), layout=(3, 4), color='skyblue', edgecolor='black')
plt.suptitle('Histograms of Numerical Variables', fontsize=16)


# Dictionnaire des colonnes à discrétiser avec 'qcut' et 'cut', et leurs labels
qcut_columns = {
    'CLAGE': ['low', 'medium', 'high', 'very_high'],
    'CLNO': ['low', 'medium', 'high', 'very_high'],
    'LOAN': ['low', 'medium', 'high', 'very_high'],
    'MORTDUE': ['low', 'medium', 'high', 'very_high']
}

cut_columns = {
    'DEBTINC': {
        'bins': [0, 20, 40, 204], 
        'labels': ['low', 'medium', 'high']
    },
    'DELINQ': {
        'bins': [-1, 0, 2, 15], 
        'labels': ['no_incident', 'few_incidents', 'many_incidents']
    },
    'DEROG': {
        'bins': [-1, 0, 1, 10], 
        'labels': ['no_incident', 'few_incidents', 'many_incidents']
    },
    'YOJ': {
        'bins': [-1, 5, 10, 42], 
        'labels': ['<5 years', '5-10 years', '>10 years']
    },
    'NINQ': {
        'bins': [-1, 0, 2, 18], 
        'labels': ['no_inquiry', 'few_inquiries', 'many_inquiries']
    }
}

label_mapping = {
    'low': 1, 'medium': 2, 'high': 3, 'very_high': 4,
    'no_inquiry': 1, 'few_inquiries': 2, 'many_inquiries': 3,
    'no_incident': 1, 'few_incidents': 2, 'many_incidents': 3,
    '<5 years': 1, '5-10 years': 2, '>10 years': 3
}

for col, labels in qcut_columns.items():
    df_encoded[f'{col}_discretized'] = pd.qcut(df_encoded[col], q=4, labels=labels)

for col, info in cut_columns.items():
    df_encoded[f'{col}_discretized'] = pd.cut(df_encoded[col], bins=info['bins'], labels=info['labels'])

discretized_columns = [f'{col}_discretized' for col in qcut_columns.keys()] + [f'{col}_discretized' for col in cut_columns.keys()]
for col in discretized_columns:
    df_encoded[col] = df_encoded[col].map(label_mapping)

print(df_encoded[discretized_columns].head())

df_copy = df_encoded.copy()

df_copy = df_copy.drop(columns=[
    'CLAGE', 'CLNO', 'DEBTINC', 'DELINQ', 'DEROG', 'LOAN', 'MORTDUE', 'NINQ', 'YOJ'
])

correlation_matrix = df_copy.corr()
plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

variables_to_drop = [
    'CLNO_discretized',     # Faible corrélation avec BAD
    'DEBTINC_discretized',  # Faible corrélation avec BAD
    'MORTDUE_discretized',  # Faible corrélation avec BAD
    'LOAN_discretized',     # Faible corrélation avec BAD
    'REASON_HomeImp',       # Multicolinéarité avec REASON_DebtCon
    'JOB_ProfExe'           # Multicolinéarité avec JOB_Other
]
df_copy = df_copy.drop(columns=variables_to_drop)

correlation_matrix = df_copy.corr()
plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')


X = df_copy.drop(columns=['BAD'])  
y = df_copy['BAD']  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)
sfs = SequentialFeatureSelector(model, direction='forward')  
sfs.fit(X_train, y_train)
selected_features = X.columns[sfs.get_support()]
print(f'Variables sélectionnées : {selected_features}')
model.fit(X_train[selected_features], y_train)
y_pred = model.predict(X_test[selected_features])
print("Accuracy :", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))



