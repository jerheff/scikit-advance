import pytest
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier


from skadvance.model_selection import (
    LowComplexitySelector,
    SingleColumnComplexity,
)

from skadvance.distributions import uniform


def test_lowcomplexityselector():

    X, y = make_classification(n_samples=1000, random_state=42)

    hps = {"min_samples_split": uniform(0, 1)}
    complexity_hp = "min_samples_split"

    selected_hp_values = []
    for complexity_direction in [True, False]:
        complexity = SingleColumnComplexity(
            complexity_hp, larger_more_complex=complexity_direction
        )
        print(f"Complexity fn: {complexity}")
        selector = LowComplexitySelector(complexity)

        gs = RandomizedSearchCV(
            DecisionTreeClassifier(random_state=42),
            param_distributions=hps,
            n_iter=10,
            scoring="roc_auc",
            refit=selector,
            random_state=42,
        )

        gs.fit(X, y)
        print(f"Best test score: {np.max(gs.cv_results_['mean_test_score'])}")
        print(
            f"Selected score: {gs.cv_results_['mean_test_score'][gs.best_index_]}, index: {gs.best_index_}, params: {gs.best_params_}"
        )
        selected_hp_values.append(gs.best_params_[complexity_hp])
    assert selected_hp_values[0] < selected_hp_values[1]
