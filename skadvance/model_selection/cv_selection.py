from functools import partial

import numpy as np


def SingleColumnComplexity(column, larger_more_complex=True):
    """
    Simple model complexity based upon the value of one column.
    """

    def SingleColumnComplexity(data, column, larger_more_complex):
        column = "param_" + column
        if larger_more_complex:
            return data[column]
        return -data[column]

    return partial(
        SingleColumnComplexity, column=column, larger_more_complex=larger_more_complex
    )


def LowComplexitySelector(complexity_fn, strategy=("std", 1), score_name="score"):
    """
    Select the least complex model that has similar performance to the best performer.
    """

    def LowComplexitySelector(cv_results, complexity_fn, strategy, score_name):
        complexities = complexity_fn(cv_results)

        if strategy[0] == "std":
            score_mean_column = "mean_test_" + score_name
            score_std_column = "std_test_" + score_name

            best_score_idx = np.argmax(cv_results[score_mean_column])
            lower_bound = (
                cv_results[score_mean_column]
                - strategy[1] * cv_results[score_std_column]
            )

            candidate_idx = np.flatnonzero(cv_results[score_mean_column] >= lower_bound)
            best_idx = complexities[candidate_idx].argmin()
        return best_idx

    return partial(
        LowComplexitySelector,
        complexity_fn=complexity_fn,
        strategy=strategy,
        score_name=score_name,
    )
