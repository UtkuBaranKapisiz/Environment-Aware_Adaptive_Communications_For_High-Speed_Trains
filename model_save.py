import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier


"""
Models:
  5. Decision Tree
  6. Random Forest
  7. Gradient Boosting
  8. Neural Network
"""


# import csv
df = pd.read_csv(r"<your_dir>\Model\datasetCombined.csv") # Replace with your dir
df.columns = ["Cografya_zorlugu", "Tunel_sayisi", "Hava_kosulu_zorlugu", "Iletim_noktasi_uzaklik", "DurumLOS", "Bolge_tren_hizi", "Hedef_degisken"]
df.head()

# Data Seperation

X = df.drop(["Hedef_degisken"], axis=1)

y = df["Hedef_degisken"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
X_train.shape, X_test.shape


# Model Training

## Decision Tree

model5 = DecisionTreeClassifier(random_state=42)
model5.fit(X_train, y_train)

## Random Forest

model6 = RandomForestClassifier(n_estimators=100, random_state=42)
model6.fit(X_train, y_train)


# Gradient Boosting

model7 = GradientBoostingClassifier(n_estimators=100, random_state=42)
model7.fit(X_train, y_train)


## Neural Network

model8 = MLPClassifier(hidden_layer_sizes=(32,), activation='relu', solver='adam', random_state=42, max_iter=1000)

model8.fit(X_train, y_train)

# Saving Models

joblib.dump(model5, 'decision_tree.joblib')
joblib.dump(model6, 'random_forest.joblib')
joblib.dump(model7, 'gradient_boosting.joblib')
joblib.dump(model8, 'neural_network.joblib')