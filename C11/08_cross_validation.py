import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.read_csv("visualization_sales.csv").dropna(subset=["profit"]).copy()
df["high_profit"] = (df["profit"] >= df["profit"].median()).astype(int)

numeric = ["quantity", "unit_price", "discount_rate", "ad_spend", "satisfaction_score"]
categorical = ["region", "category", "channel", "customer_segment"]
X = df[numeric + categorical]
y = df["high_profit"]

preprocessor = ColumnTransformer(
    [
        (
            "num",
            Pipeline(
                [
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler()),
                ]
            ),
            numeric,
        ),
        (
            "cat",
            Pipeline(
                [
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("encoder", OneHotEncoder(handle_unknown="ignore")),
                ]
            ),
            categorical,
        ),
    ]
)

models = {
    "baseline": DummyClassifier(strategy="prior"),
    "logistic": LogisticRegression(max_iter=2_000, class_weight="balanced"),
}

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
for name, estimator in models.items():
    pipeline = Pipeline(
        [("preprocess", preprocessor), ("model", estimator)]
    )
    scores = cross_validate(
        pipeline,
        X,
        y,
        cv=cv,
        scoring=["accuracy", "f1", "roc_auc"],
        n_jobs=-1,
    )
    print(
        name,
        "accuracy=", round(scores["test_accuracy"].mean(), 3),
        "f1=", round(scores["test_f1"].mean(), 3),
        "roc_auc=", round(scores["test_roc_auc"].mean(), 3),
    )