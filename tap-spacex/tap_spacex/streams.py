"""Stream type classes for tap-spacex."""

from __future__ import annotations

import sys
import typing as t

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_spacex.client import spacexStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources


# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = importlib_resources.files(__package__) / "schemas"
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class ShipsStream(spacexStream):
    """Define custom stream."""

    name = "ships"
    path = "/ships"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType, required=True),
        th.Property("name", th.StringType, required=True),
        th.Property("legacy_id", th.StringType),
        th.Property("model", th.StringType),
        th.Property("type", th.StringType),
        th.Property("roles", th.ArrayType(th.StringType)),
        th.Property("active", th.BooleanType, required=True),
        th.Property("imo", th.NumberType),
        th.Property("mmsi", th.NumberType),
        th.Property("abs", th.NumberType),
        th.Property("class", th.NumberType),
        th.Property("mass_kg", th.NumberType),
        th.Property("mass_lbs", th.NumberType),
        th.Property("year_built", th.NumberType),
        th.Property("home_port", th.StringType),
        th.Property("status", th.StringType),
        th.Property("speed_kn", th.NumberType),
        th.Property("course_deg", th.NumberType),
        th.Property("latitude", th.NumberType),
        th.Property("longitude", th.NumberType),
        th.Property("last_ais_update", th.StringType),
        th.Property("link", th.StringType),
        th.Property("image", th.StringType),
        th.Property("launches", th.ArrayType(th.UUIDType))
    ).to_dict()


class CrewStream(spacexStream):
    """Define custom stream."""

    name = "crew"
    path = "/crew"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("status", th.StringType, required=True),
        th.Property("agency", th.StringType),
        th.Property("image", th.StringType),
        th.Property("wikipedia", th.StringType),
        th.Property("launches", th.ArrayType(th.UUIDType))
    ).to_dict()


class LaunchesStream(spacexStream):
    """Define custom stream."""

    name = "launches"
    path = "/launches"
    primary_keys = ["id"]
    replication_key = "date_utc"
    replication_method = "INCREMENTAL"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("flight_number", th.NumberType, required=True),
        th.Property("name", th.StringType, required=True),
        th.Property("date_utc", th.StringType, required=True),
        th.Property("date_unix", th.NumberType, required=True),
        th.Property("date_local", th.StringType, required=True),
        th.Property("date_precision", th.StringType),
        th.Property("static_fire_date_utc", th.StringType, default=None),
        th.Property("static_fire_date_unix", th.NumberType, default=None),
        th.Property("tdb", th.BooleanType, default=False),
        th.Property("net", th.BooleanType, default=False),
        th.Property("window", th.NumberType, default=None),
        th.Property("rocket", th.UUIDType, default=None),
        th.Property("success", th.BooleanType, default=None),
        th.Property("failures", th.ArrayType(
            th.ObjectType(
                th.Property("time", th.NumberType),
                th.Property("altitude", th.NumberType),
                th.Property("reason", th.StringType)
            )
        )),
        th.Property("upcoming", th.BooleanType, required=True),
        th.Property("details", th.StringType, default=None),
        th.Property("fairings", th.ObjectType(
            th.Property("reused", th.BooleanType, default=None),
            th.Property("recovery_attempt", th.BooleanType, default=None),
            th.Property("recovered", th.BooleanType, default=None),
            th.Property("ships", th.ArrayType(th.UUIDType))
        )),
        th.Property("crew", th.ArrayType(
            th.ObjectType(
                th.Property("crew", th.UUIDType, default=None),
                th.Property("role", th.StringType, default=None)
            )
        )),
        th.Property("ships", th.ArrayType(th.UUIDType)),
        th.Property("capsules", th.ArrayType(th.UUIDType)),
        th.Property("payloads", th.ArrayType(th.UUIDType)),
        th.Property("launchpad", th.UUIDType, default=None),
        th.Property("cores", th.ArrayType(
            th.ObjectType(
                th.Property("core", th.UUIDType, default=None),
                th.Property("flight", th.NumberType, default=None),
                th.Property("gridfins", th.BooleanType, default=None),
                th.Property("legs", th.BooleanType, default=None),
                th.Property("reused", th.BooleanType, default=None),
                th.Property("landing_attempt", th.BooleanType, default=None),
                th.Property("landing_success", th.BooleanType, default=None),
                th.Property("landing_type", th.StringType, default=None),
                th.Property("landpad", th.UUIDType, default=None)
            )
        )),
        th.Property("links", th.ObjectType(
            th.Property("patch", th.ObjectType(
                th.Property("small", th.StringType, default=None),
                th.Property("large", th.StringType, default=None)
            )),
            th.Property("reddit", th.ObjectType(
                th.Property("campaign", th.StringType, default=None),
                th.Property("launch", th.StringType, default=None),
                th.Property("media", th.StringType, default=None),
                th.Property("recovery", th.StringType, default=None)
            )),
            th.Property("flickr", th.ObjectType(
                th.Property("small", th.ArrayType(th.StringType)),
                th.Property("original", th.ArrayType(th.StringType))
            )),
            th.Property("presskit", th.StringType, default=None),
            th.Property("webcast", th.StringType, default=None),
            th.Property("youtube_id", th.StringType, default=None),
            th.Property("article", th.StringType, default=None),
            th.Property("wikipedia", th.StringType, default=None)
        )),
        th.Property("auto_update", th.BooleanType, default=True)
    ).to_dict()


class LaunchpadStream(spacexStream):
    """Define custom stream."""

    name = "launchpads"
    path = "/launchpads"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType, default=None),
        th.Property("full_name", th.StringType, default=None),
        th.Property("status", th.StringType, required=True),
        th.Property("locality", th.StringType, default=None),
        th.Property("region", th.StringType, default=None),
        th.Property("timezone", th.StringType, default=None),
        th.Property("latitude", th.NumberType, default=None),
        th.Property("longitude", th.NumberType, default=None),
        th.Property("launch_attempts", th.NumberType, default=0),
        th.Property("launch_successes", th.NumberType, default=0),
        th.Property("rockets", th.ArrayType(th.UUIDType)),
        th.Property("launches", th.ArrayType(th.UUIDType))
    ).to_dict()


class StarlinkStream(spacexStream):
    """Define custom stream."""

    name = "starlink"
    path = "/starlink"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("version", th.StringType, default=None),
        th.Property("launch", th.StringType, default=None),
        th.Property("longitude", th.NumberType, default=None),
        th.Property("latitude", th.NumberType, default=None),
        th.Property("height_km", th.NumberType, default=None),
        th.Property("velocity_kms", th.NumberType, default=None),
        th.Property("spaceTrack", th.ObjectType(
            th.Property("CCSDS_OMM_VERS", th.StringType, default=None),
            th.Property("COMMENT", th.StringType, default=None),
            th.Property("CREATION_DATE", th.StringType, default=None),
            th.Property("ORIGINATOR", th.StringType, default=None),
            th.Property("OBJECT_NAME", th.StringType, default=None),
            th.Property("OBJECT_ID", th.StringType, default=None),
            th.Property("CENTER_NAME", th.StringType, default=None),
            th.Property("REF_FRAME", th.StringType, default=None),
            th.Property("TIME_SYSTEM", th.StringType, default=None),
            th.Property("MEAN_ELEMENT_THEORY", th.StringType, default=None),
            th.Property("EPOCH", th.StringType, default=None),
            th.Property("MEAN_MOTION", th.NumberType, default=None),
            th.Property("ECCENTRICITY", th.NumberType, default=None),
            th.Property("INCLINATION", th.NumberType, default=None),
            th.Property("RA_OF_ASC_NODE", th.NumberType, default=None),
            th.Property("ARG_OF_PERICENTER", th.NumberType, default=None),
            th.Property("MEAN_ANOMALY", th.NumberType, default=None),
            th.Property("EPHEMERIS_TYPE", th.NumberType, default=None),
            th.Property("CLASSIFICATION_TYPE", th.StringType, default=None),
            th.Property("NORAD_CAT_ID", th.NumberType, default=None),
            th.Property("ELEMENT_SET_NO", th.NumberType, default=None),
            th.Property("REV_AT_EPOCH", th.NumberType, default=None),
            th.Property("BSTAR", th.NumberType, default=None),
            th.Property("MEAN_MOTION_DOT", th.NumberType, default=None),
            th.Property("MEAN_MOTION_DDOT", th.NumberType, default=None),
            th.Property("SEMIMAJOR_AXIS", th.NumberType, default=None),
            th.Property("PERIOD", th.NumberType, default=None),
            th.Property("APOAPSIS", th.NumberType, default=None),
            th.Property("PERIAPSIS", th.NumberType, default=None),
            th.Property("OBJECT_TYPE", th.StringType, default=None),
            th.Property("RCS_SIZE", th.StringType, default=None),
            th.Property("COUNTRY_CODE", th.StringType, default=None),
            th.Property("LAUNCH_DATE", th.StringType, default=None),
            th.Property("SITE", th.StringType, default=None),
            th.Property("DECAY_DATE", th.StringType, default=None),
            th.Property("DECAYED", th.NumberType, default=None),
            th.Property("FILE", th.NumberType, default=None),
            th.Property("GP_ID", th.NumberType, default=None),
            th.Property("TLE_LINE0", th.StringType, default=None),
            th.Property("TLE_LINE1", th.StringType, default=None),
            th.Property("TLE_LINE2", th.StringType, default=None)
        ))
    ).to_dict()


class RocketsStream(spacexStream):
    """Define custom stream."""

    name = "rockets"
    path = "/rockets"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("type", th.StringType),
        th.Property("active", th.BooleanType),
        th.Property("stages", th.NumberType),
        th.Property("boosters", th.NumberType),
        th.Property("cost_per_launch", th.NumberType),
        th.Property("success_rate_pct", th.NumberType),
        th.Property("first_flight", th.StringType),
        th.Property("country", th.StringType),
        th.Property("company", th.StringType),
        th.Property("height", th.ObjectType(
            th.Property("meters", th.NumberType),
            th.Property("feet", th.NumberType)
        )),
        th.Property("diameter", th.ObjectType(
            th.Property("meters", th.NumberType),
            th.Property("feet", th.NumberType)
        )),
        th.Property("mass", th.ObjectType(
            th.Property("kg", th.NumberType),
            th.Property("lb", th.NumberType)
        )),
        th.Property("payload_weights", th.ArrayType(th.ObjectType())),
        th.Property("first_stage", th.ObjectType(
            th.Property("reusable", th.BooleanType),
            th.Property("engines", th.NumberType),
            th.Property("fuel_amount_tons", th.NumberType),
            th.Property("burn_time_sec", th.NumberType),
            th.Property("thrust_sea_level", th.ObjectType(
                th.Property("kN", th.NumberType),
                th.Property("lbf", th.NumberType)
            )),
            th.Property("thrust_vacuum", th.ObjectType(
                th.Property("kN", th.NumberType),
                th.Property("lbf", th.NumberType)
            ))
        )),
        th.Property("second_stage", th.ObjectType(
            th.Property("reusable", th.BooleanType),
            th.Property("engines", th.NumberType),
            th.Property("fuel_amount_tons", th.NumberType),
            th.Property("burn_time_sec", th.NumberType),
            th.Property("thrust", th.ObjectType(
                th.Property("kN", th.NumberType),
                th.Property("lbf", th.NumberType)
            )),
            th.Property("payloads", th.ObjectType(
                th.Property("option_1", th.StringType),
                th.Property("composite_fairing", th.ObjectType(
                    th.Property("height", th.ObjectType(
                        th.Property("meters", th.NumberType),
                        th.Property("feet", th.NumberType)
                    )),
                    th.Property("diameter", th.ObjectType(
                        th.Property("meters", th.NumberType),
                        th.Property("feet", th.NumberType)
                    ))
                ))
            ))
        )),
        th.Property("engines", th.ObjectType(
            th.Property("number", th.NumberType),
            th.Property("type", th.StringType),
            th.Property("version", th.StringType),
            th.Property("layout", th.StringType),
            th.Property("isp", th.ObjectType(
                th.Property("sea_level", th.NumberType),
                th.Property("vacuum", th.NumberType)
            )),
            th.Property("engine_loss_max", th.NumberType),
            th.Property("propellant_1", th.StringType),
            th.Property("propellant_2", th.StringType),
            th.Property("thrust_sea_level", th.ObjectType(
                th.Property("kN", th.NumberType),
                th.Property("lbf", th.NumberType)
            )),
            th.Property("thrust_vacuum", th.ObjectType(
                th.Property("kN", th.NumberType),
                th.Property("lbf", th.NumberType)
            )),
            th.Property("thrust_to_weight", th.NumberType)
        )),
        th.Property("landing_legs", th.ObjectType(
            th.Property("number", th.NumberType),
            th.Property("material", th.StringType)
        )),
        th.Property("flickr_images", th.ArrayType(th.StringType)),
        th.Property("wikipedia", th.StringType),
        th.Property("description", th.StringType)
    ).to_dict()

class PayloadsStream(spacexStream):
    """Define custom stream."""

    name = "payloads"
    path = "/payloads"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType, default=None),
        th.Property("type", th.StringType, default=None),
        th.Property("reused", th.BooleanType, default=False),
        th.Property("launch", th.UUIDType, default=None),
        th.Property("customers", th.ArrayType(th.StringType)),
        th.Property("norad_ids", th.ArrayType(th.NumberType)),
        th.Property("nationalities", th.ArrayType(th.StringType)),
        th.Property("manufacturers", th.ArrayType(th.StringType)),
        th.Property("mass_kg", th.NumberType, default=None),
        th.Property("mass_lbs", th.NumberType, default=None),
        th.Property("orbit", th.StringType, default=None),
        th.Property("reference_system", th.StringType, default=None),
        th.Property("regime", th.StringType, default=None),
        th.Property("longitude", th.NumberType, default=None),
        th.Property("semi_major_axis_km", th.NumberType, default=None),
        th.Property("eccentricity", th.NumberType, default=None),
        th.Property("periapsis_km", th.NumberType, default=None),
        th.Property("apoapsis_km", th.NumberType, default=None),
        th.Property("inclination_deg", th.NumberType, default=None),
        th.Property("period_min", th.NumberType, default=None),
        th.Property("lifespan_years", th.NumberType, default=None),
        th.Property("epoch", th.StringType, default=None),
        th.Property("mean_motion", th.NumberType, default=None),
        th.Property("raan", th.NumberType, default=None),
        th.Property("arg_of_pericenter", th.NumberType, default=None),
        th.Property("mean_anomaly", th.NumberType, default=None),
        th.Property("dragon", th.ObjectType(
            th.Property("capsule", th.UUIDType, default=None),
            th.Property("mass_returned_kg", th.NumberType, default=None),
            th.Property("mass_returned_lbs", th.NumberType, default=None),
            th.Property("flight_time_sec", th.NumberType, default=None),
            th.Property("manifest", th.StringType, default=None),
            th.Property("water_landing", th.BooleanType, default=None),
            th.Property("land_landing", th.BooleanType, default=None)
        ))
    ).to_dict()




