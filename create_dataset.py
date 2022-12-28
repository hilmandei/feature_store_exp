# Importing dependencies
import pandas as pd
from feast import FeatureStore
from feast.infra.offline_stores.file_source import SavedDatasetFileStorage

# Getting our FeatureStore
store = FeatureStore(repo_path="breast_cancer/feature_repo/")

# Reading our targets as an entity DataFrame
entity_df = pd.read_parquet(path="breast_cancer/feature_repo/data/target_df.parquet")

# Getting the indicated historical features
# and joining them with our entity DataFrame
training_data = store.get_historical_features(
    entity_df=entity_df,
    features=[
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
)

# Storing the dataset as a local file
dataset = store.create_saved_dataset(
    from_=training_data,
    name="breast_cancer_dataset",
    storage=SavedDatasetFileStorage("breast_cancer/feature_repo/data/breast_cancer_dataset.parquet")
)