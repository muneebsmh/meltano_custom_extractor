{{
    config(
        target_schema=env_var('target_schema')
    )
}}
WITH
source AS (
    SELECT
        id,
        version,
        launch,
        longitude,
        latitude,
        height_km,
        velocity_kms,
        "spaceTrack",
        CURRENT_TIMESTAMP AS transformation_updated_at
    FROM {{ source('pg_source', 'starlink') }}
)
SELECT * FROM source
