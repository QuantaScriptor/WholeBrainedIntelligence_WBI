python
import shap
import lime
import lime.lime_tabular
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Train example model
def train_example_model():
    data = pd.read_csv('path_to_your_data.csv')
    X = data.drop('target', axis=1)
    y = data['target']
    model = RandomForestClassifier()
    model.fit(X, y)
    return model, X, y

# Explain model using SHAP
def explain_model_shap(model, X):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)
    shap.summary_plot(shap_values, X)

# Explain model using LIME
def explain_model_lime(model, X, instance):
    explainer = lime.lime_tabular.LimeTabularExplainer(X.values, feature_names=X.columns, class_names=['class_0', 'class_1'], verbose=True, mode='classification')
    exp = explainer.explain_instance(instance, model.predict_proba, num_features=5)
    exp.show_in_notebook(show_table=True)

if __name__ == "__main__":
    model, X, y = train_example_model()
    explain_model_shap(model, X)
    instance = X.iloc[0]
    explain_model_lime(model, X, instance)
