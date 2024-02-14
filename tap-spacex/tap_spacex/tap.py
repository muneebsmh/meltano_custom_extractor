"""spacex tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_spacex import streams


class Tapspacex(Tap):
    """spacex tap class."""

    name = "tap-spacex"

    def discover_streams(self) -> list[streams.spacexStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.ShipsStream(self),
            streams.CrewStream(self),
            streams.LaunchesStream(self),
            streams.LaunchpadStream(self),
            streams.StarlinkStream(self),
            streams.RocketsStream(self),
            streams.PayloadsStream(self)
        ]

