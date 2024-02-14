-- Description: Model to calculate total satellites, total launches, average satellites per launch, and average days between launches for Starlink satellites
{{
    config(
        target_schema=env_var('target_schema'),
        materialized='table'
    )
}}
WITH launch_dates AS (
    SELECT
        id AS launch_id,
        name,
        date_utc launch_date_utc,
        LAG(date_utc) OVER (ORDER BY date_utc) AS previous_launch_date_utc
    FROM
        {{ ref('model_launches') }}
    WHERE
        "name" LIKE '%Starlink%'
), satellites as (
    SELECT
        id AS satellite_id,
        version,
        launch,
        longitude,
        latitude,
        height_km,
        velocity_kms,
        "spaceTrack"
    FROM
        {{ ref('model_starlink') }}
)
SELECT
    COUNT(DISTINCT s.satellite_id) AS total_satellites,
    COUNT(DISTINCT l.launch_id) AS total_launches,
    COUNT(DISTINCT s.satellite_id) / COUNT(DISTINCT l.launch_id) AS avg_satellites_per_launch,
    AVG(EXTRACT(EPOCH FROM (launch_date_utc - previous_launch_date_utc)) / 86400) AS avg_days_between_launches,
    CURRENT_TIMESTAMP AS transformation_updated_at
FROM satellites s
INNER JOIN
    launch_dates l
ON
    s.launch = l.launch_id
