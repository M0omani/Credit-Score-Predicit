from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.metrics import accuracy_score, classification_report


class BalancedRandomForestModel:

    def __init__(self, X_train, y_train, X_val, y_val, X_test, y_test):
        # The model to use search on
        self.brf = BalancedRandomForestClassifier(random_state = 42)
        # Training
        self.X_train = X_train
        self.y_train = y_train

        # Validation
        self.X_val = X_val
        self.y_val = y_val

        # Testing
        self.X_test = X_test
        self.y_test = y_test

    # Balanced Random Forest Classifier with default params
    def BRFC_Classic(self):

        """
        Returns:
        self.brf: The classic Balanced Random Forest Classifier model trained on the passed data.

        """

        # Train model
        self.brf.fit(self.X_train, self.y_train)

        # Validation
        pred_val = self.brf.predict(self.X_val)
        # Evaluating validation
        # Accuracy
        accuracy_val = accuracy_score(self.y_val, pred_val)
        # Classification report
        report_val = classification_report(self.y_val, pred_val)

        # Testing
        pred_test = self.brf.predict(self.X_test)
        # Evaluating testing
        # Accuracy
        accuracy_test = accuracy_score(self.y_test, pred_test)
        # Classification report
        report_test = classification_report(self.y_test, pred_test)

        # Printing the results
        print(f"Balanced Random Forest's validation accuracy is {accuracy_val}")
        print("-" * 70)
        print(f"Balanced Random Forest's validation classification report is:\n{report_val}")
        print("=" * 100)
        print(f"Balanced Random Forest's testing accuracy is {accuracy_test}")
        print("-" * 70)
        print(f"Balanced Random Forest's testing classification report is:\n{report_test}")

        # Return the trained Balanced Random Forest model
        return self.brf

    # Balanced Random Forest Classifier + GridSearch for best params
    def BRFC_GridSearchCV(self, params, cv):

        """
        Returns:
        best_brf: The Balanced Random Forest Classifier model trained on the best parameters found by GridSearchCV.
        best_params: The best parameters found by GridSearchCV.

        """
        # GridSearchCV
        grid_search = GridSearchCV(self.brf, params, cv = cv, n_jobs = -1)
        grid_search.fit(self.X_train, self.y_train)

        # Best Parameters
        best_params = grid_search.best_params_

        # Train the model with the best parameters
        best_brf = BalancedRandomForestClassifier(**best_params, random_state = 42)
        best_brf.fit(self.X_train, self.y_train)

        # Validation
        pred_val = best_brf.predict(self.X_val)
        # Evaluating validation
        # Accuracy
        accuracy_val = accuracy_score(self.y_val, pred_val)
        # Classification report
        report_val = classification_report(self.y_val, pred_val)

        # Testing
        pred_test = best_brf.predict(self.X_test)
        # Evaluating testing
        # Accuracy
        accuracy_test = accuracy_score(self.y_test, pred_test)
        # Classification report
        report_test = classification_report(self.y_test, pred_test)

        # Printing the results
        print(f"Balanced Random Forest's validation accuracy (GridSearchCV) is {accuracy_val}")
        print("-" * 70)
        print(f"Balanced Random Forest's validation classification report (GridSearchCV) is:\n{report_val}")
        print("=" * 100)
        print(f"Balanced Random Forest's testing accuracy (GridSearchCV) is {accuracy_test}")
        print("-" * 70)
        print(f"Balanced Random Forest's testing classification report (GridSearchCV) is:\n{report_test}")

        # Return the trained Balanced Random Forest model and the best parameters
        return best_brf, best_params

    # Balanced Random Forest Classifier + RandomizedSearchCV for best params
    def BRFC_RandomizedSearchCV(self, params, cv):

        """
        Returns:
        best_brf: The Balanced Random Forest Classifier model trained on the best parameters found by RandomizedSearchCV.
        best_params: The best parameters found by RandomizedSearchCV.

        """
        # RandomizedSearchCV
        random_search = RandomizedSearchCV(self.brf, params, cv = cv, n_jobs = -1)
        random_search.fit(self.X_train, self.y_train)

        # Best Parameters
        best_params = random_search.best_params_

        # Train the model with the best parameters
        best_brf = BalancedRandomForestClassifier(**best_params, random_state = 42)
        best_brf.fit(self.X_train, self.y_train)

        # Validation
        pred_val = best_brf.predict(self.X_val)
        # Evaluating validation
        # Accuracy
        accuracy_val = accuracy_score(self.y_val, pred_val)
        # Classification report
        report_val = classification_report(self.y_val, pred_val)

        # Testing
        pred_test = best_brf.predict(self.X_test)
        # Evaluating testing
        # Accuracy
        accuracy_test = accuracy_score(self.y_test, pred_test)
        # Classification report
        report_test = classification_report(self.y_test, pred_test)

        # Printing the results
        print(f"Balanced Random Forest's validation accuracy (RandomizedSearchCV) is {accuracy_val}")
        print("-" * 70)
        print(f"Balanced Random Forest's validation classification report (RandomizedSearchCV) is:\n{report_val}")
        print("=" * 100)
        print(f"Balanced Random Forest's testing accuracy (RandomizedSearchCV) is {accuracy_test}")
        print("-" * 70)
        print(f"Balanced Random Forest's testing classification report (RandomizedSearchCV) is:\n{report_test}")

        # Return the trained Balanced Random Forest model and the best parameters
        return best_brf, best_params
