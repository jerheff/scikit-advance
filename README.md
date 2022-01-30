# scikit-advance

A place to publish components that advance your use of scikit-learn. For instance, more
robust model selection logic during cross validation.

This is an alpha stage project.

# Example

Select a low complexity model during cross validation:

```python
from scipy.stats import uniform
from sklearn.model_selection import RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier

from ska.model_selection import SingleColumnComplexity, LowComplexitySelector

# prep your data ...

# do CV...
complexity = SingleColumnComplexity("min_samples_split", larger_more_complex=False)
selector = LowComplexitySelector(complexity)

gs = RandomizedSearchCV(
    DecisionTreeClassifier(),
    param_grid={'min_samples_split': uniform(0, 1)},
    scoring="roc_auc",
    refit=selector,
)

gs.fit(X, y)
```
