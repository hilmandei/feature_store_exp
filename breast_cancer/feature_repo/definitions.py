# Importing dependencies
from datetime import timedelta
from feast import Entity, FileSource, Field, FeatureView
from feast.types import Float64, Int64, ValueType

abs_path = "/Users/hilman/Documents/file_python/DS_Project/feast_feature_store/" \
           "feast_tutorial/breast_cancer/feature_repo/data/"

# Declaring an entity for the dataset
patient = Entity(
    name="patient_id", 
    value_type=ValueType.INT64,
    description="The ID of the patient",
    join_keys=['patient_id'])

# Declaring the source of the first set of Fields
f_source1 = FileSource(
    path=abs_path+"data_df1.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the first set of Fields
df1_fv = FeatureView(
    name="df1_Field_view",
    ttl=timedelta(days=1),
    entities=[patient],
    schema=[
        Field(name="mean radius", dtype=Float64),
        Field(name="mean texture", dtype=Float64),
        Field(name="mean perimeter", dtype=Float64),
        Field(name="mean area", dtype=Float64),
        Field(name="mean smoothness", dtype=Float64)
        ],    
    source=f_source1
)

# Declaring the source of the second set of Fields
f_source2 = FileSource(
    path=abs_path + "data_df2.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the second set of Fields
df2_fv = FeatureView(
    name="df2_Field_view",
    ttl=timedelta(days=1),
    entities=[patient],
    schema=[
        Field(name="mean compactness", dtype=Float64),
        Field(name="mean concavity", dtype=Float64),
        Field(name="mean concave points", dtype=Float64),
        Field(name="mean symmetry", dtype=Float64),
        Field(name="mean fractal dimension", dtype=Float64)
        ],    
    source=f_source2
)

# Declaring the source of the third set of Fields
f_source3 = FileSource(
    path=abs_path + "data_df3.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the third set of Fields
df3_fv = FeatureView(
    name="df3_Field_view",
    ttl=timedelta(days=1),
    entities=[patient],
    schema=[
        Field(name="radius error", dtype=Float64),
        Field(name="texture error", dtype=Float64),
        Field(name="perimeter error", dtype=Float64),
        Field(name="area error", dtype=Float64),
        Field(name="smoothness error", dtype=Float64),
        Field(name="compactness error", dtype=Float64),
        Field(name="concavity error", dtype=Float64)
        ],    
    source=f_source3
)

# Declaring the source of the fourth set of Fields
f_source4 = FileSource(
    path=abs_path + "data_df4.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the fourth set of Fields
df4_fv = FeatureView(
    name="df4_Field_view",
    ttl=timedelta(days=1),
    entities=[patient],
    schema=[
        Field(name="concave points error", dtype=Float64),
        Field(name="symmetry error", dtype=Float64),
        Field(name="fractal dimension error", dtype=Float64),
        Field(name="worst radius", dtype=Float64),
        Field(name="worst texture", dtype=Float64),
        Field(name="worst perimeter", dtype=Float64),
        Field(name="worst area", dtype=Float64),
        Field(name="worst smoothness", dtype=Float64),
        Field(name="worst compactness", dtype=Float64),
        Field(name="worst concavity", dtype=Float64),
        Field(name="worst concave points", dtype=Float64),
        Field(name="worst symmetry", dtype=Float64),
        Field(name="worst fractal dimension", dtype=Float64),        
        ],    
    source=f_source4
)

# Declaring the source of the targets
target_source = FileSource(
    path=abs_path+"target_df.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the targets
target_fv = FeatureView(
    name="target_Field_view",
    entities=[patient],
    ttl=timedelta(days=1),
    schema=[Field(name="target", dtype=Int64)],
    source=target_source
)
