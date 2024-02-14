{{
    config(
        target_schema=env_var('target_schema')
    )
}}
WITH
source AS (
    SELECT
        id,
        flight_number,
        name,
        date_utc::TIMESTAMP,
        date_unix,
        date_local,
        date_precision,
        static_fire_date_utc,
        static_fire_date_unix,
        tdb,
        net,
        "window",
        rocket,
        success,
        failures,
        upcoming,
        details,
        fairings,
        crew,
        ships,
        capsules,
        payloads,
        launchpad,
        cores,
        links,
        auto_update,
        CURRENT_TIMESTAMP AS transformation_updated_at
    FROM {{ source('pg_source', 'launches') }}
)
SELECT * FROM source
