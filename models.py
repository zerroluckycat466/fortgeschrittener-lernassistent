import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


class LearningPathModel:
    def __init__(self, data):
        self.data = data
        self.model = RandomForestClassifier()

    def train_model(self):
        X = self.data.drop('target', axis=1)
        y = self.data['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        self.model.fit(X_train, y_train)

    def predict(self, user_data):
        return self.model.predict(user_data)