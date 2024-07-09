
"""
CONFIDENTIALITY NOTICE: This information is the exclusive property of Reece Dixon and is provided under strict confidentiality.
Unauthorized use, reproduction, or distribution is prohibited.
© Reece Dixon - All rights reserved.
"""

import pandas as pd
from aif360.datasets import BinaryLabelDataset
from aif360.algorithms.preprocessing import Reweighing
from fairlearn.metrics import MetricFrame, selection_rate, demographic_parity_difference
from sklearn.linear_model import LogisticRegression

# Load and preprocess data
def load_data():
    data = pd.read_csv('path_to_your_dataset.csv')
    return data

# Bias detection
def detect_bias(data, target, protected_attribute):
    dataset = BinaryLabelDataset(df=data, label_names=[target], protected_attribute_names=[protected_attribute])
    return dataset

# Bias mitigation
def mitigate_bias(dataset):
    reweighing = Reweighing(unprivileged_groups=[{protected_attribute: 0}], privileged_groups=[{protected_attribute: 1}])
    transformed_dataset = reweighing.fit_transform(dataset)
    return transformed_dataset

# Train and evaluate model
def train_and_evaluate(data, target, protected_attribute):
    model = LogisticRegression()
    X = data.drop(columns=[target, protected_attribute])
    y = data[target]
    model.fit(X, y)
    predictions = model.predict(X)

    metric_frame = MetricFrame(metrics={"selection_rate": selection_rate}, y_true=y, y_pred=predictions, sensitive_features=data[protected_attribute])
    print(metric_frame.by_group)
    print(f"Demographic parity difference: {demographic_parity_difference(y, predictions, sensitive_features=data[protected_attribute])}")

if __name__ == "__main__":
    data = load_data()
    protected_attribute = 'gender'  # Change to your dataset's protected attribute
    target = 'outcome'  # Change to your dataset's target variable

    dataset = detect_bias(data, target, protected_attribute)
    mitigated_dataset = mitigate_bias(dataset)
    train_and_evaluate(mitigated_dataset.convert_to_dataframe()[0], target, protected_attribute)
