from datetime import timedelta

from feast import Entity, FeatureService, FeatureView, Field, FileSource
from feast.types import Float32, Int64


sample = Entity(name="sample_id", join_keys=["sample_id"])

wine_source = FileSource(
    name="wine_source",
    path="data/wine_features.parquet",
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp",
)

wine_fv = FeatureView(
    name="wine_measurements",
    entities=[sample],
    ttl=timedelta(days=365),
    schema=[
        Field(name="alcohol", dtype=Float32),
        Field(name="malic_acid", dtype=Float32),
        Field(name="ash", dtype=Float32),
        Field(name="target", dtype=Int64),
    ],
    source=wine_source,
    online=True,
)

wine_feature_service = FeatureService(
    name="wine_feature_service",
    features=[wine_fv],
)
