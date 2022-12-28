# Importing dependencies
from feast import FeatureStore
import pandas as pd
from joblib import load

# Getting our FeatureStore
store = FeatureStore(repo_path="breast_cancer/feature_repo/")

# Defining our features names
feast_features = [
        "df1_Field_view:mean radius",
        "df1_Field_view:mean texture",
        "df1_Field_view:mean perimeter",
        "df1_Field_view:mean area",
        "df1_Field_view:mean smoothness",
        "df2_Field_view:mean compactness",
        "df2_Field_view:mean concavity",
        "df2_Field_view:mean concave points",
        "df2_Field_view:mean symmetry",
        "df2_Field_view:mean fractal dimension",
        "df3_Field_view:radius error",
        "df3_Field_view:texture error",
        "df3_Field_view:perimeter error",
        "df3_Field_view:area error",
        "df3_Field_view:smoothness error",
        "df3_Field_view:compactness error",
        "df3_Field_view:concavity error",
        "df4_Field_view:concave points error",
        "df4_Field_view:symmetry error",
        "df4_Field_view:fractal dimension error",
        "df4_Field_view:worst radius",
        "df4_Field_view:worst texture",
        "df4_Field_view:worst perimeter",
        "df4_Field_view:worst area",
        "df4_Field_view:worst smoothness",
        "df4_Field_view:worst compactness",
        "df4_Field_view:worst concavity",
        "df4_Field_view:worst concave points",
        "df4_Field_view:worst symmetry",
        "df4_Field_view:worst fractal dimension"
    ]

# Getting the latest features
features = store.get_online_features(
    features=feast_features,    
    entity_rows=[{"patient_id": 568}, {"patient_id": 567}]
).to_df()

# Converting the features to a DataFrame
features_df = features
print(features_df)

# Loading our model and doing inference
reg = load("model.joblib")
predictions = reg.predict(features_df[sorted(features_df.drop("patient_id", axis=1))])
print(predictions)