from abc import ABC, abstractmethod

from waypoint_core.distance import Distance


class Trail(ABC):
    default_unit = "km"

    ALLOWED_DIFFICULTIES = {
        "easy",
        "moderate",
        "hard",
        "expert"
    }

    def __init__(
        self,
        trail_id,
        name,
        distance,
        elevation_gain_m,
        difficulty
    ):
        if not isinstance(distance, Distance):
            raise ValueError("distance must be a Distance object")

        self.id = trail_id
        self.name = name
        self.distance = distance
        self.elevation_gain_m = elevation_gain_m

        self.__difficulty = None
        self.set_difficulty(difficulty)

    @staticmethod
    def validate_difficulty(value):
        return value in Trail.ALLOWED_DIFFICULTIES

    def set_difficulty(self, value):
        if not self.validate_difficulty(value):
            raise ValueError("Invalid difficulty")

        self.__difficulty = value

    @property
    def difficulty(self):
        return self.__difficulty

    @classmethod
    def from_dict(cls, data):
        distance = Distance(
            data["distance"],
            data.get("unit", cls.default_unit)
        )

        return cls(
            data["id"],
            data["name"],
            distance,
            data["elevation_gain_m"],
            data["difficulty"]
        )

    @classmethod
    def set_default_unit(cls, unit):
        if unit not in ("km", "mi"):
            raise ValueError("Default unit must be 'km' or 'mi'")

        cls.default_unit = unit

    @abstractmethod
    def estimated_time(self):
        """Return the estimated time required to complete the trail."""
        pass

    @abstractmethod
    def summary(self):
        """Return a short description of the trail."""
        pass

    def __eq__(self, other):
        if not isinstance(other, Trail):
            return False

        return self.id == other.id

    def __str__(self):
        return f"{self.name} ({self.distance})"


class DayHike(Trail):
    PACE_KM_PER_HOUR = 4.0

    def __init__(
        self,
        trail_id,
        name,
        distance,
        elevation_gain_m,
        difficulty
    ):
        super().__init__(
            trail_id,
            name,
            distance,
            elevation_gain_m,
            difficulty
        )

    def estimated_time(self):
        distance_km = self.distance.convert().magnitude if self.distance.unit == "mi" else self.distance.magnitude
        return distance_km / self.PACE_KM_PER_HOUR

    def summary(self):
        return f"Day hike: {self.name} - {self.distance}"


class BackpackingRoute(Trail):
    PACE_KM_PER_HOUR = 3.0

    def __init__(
        self,
        trail_id,
        name,
        distance,
        elevation_gain_m,
        difficulty
    ):
        super().__init__(
            trail_id,
            name,
            distance,
            elevation_gain_m,
            difficulty
        )

    def estimated_time(self):
        distance_km = self.distance.convert().magnitude if self.distance.unit == "mi" else self.distance.magnitude
        return distance_km / self.PACE_KM_PER_HOUR

    def summary(self):
        return f"Backpacking route: {self.name} - {self.distance}"


class TrailRun(Trail):
    PACE_KM_PER_HOUR = 8.0

    def __init__(
        self,
        trail_id,
        name,
        distance,
        elevation_gain_m,
        difficulty
    ):
        super().__init__(
            trail_id,
            name,
            distance,
            elevation_gain_m,
            difficulty
        )

    def estimated_time(self):
        distance_km = self.distance.convert().magnitude if self.distance.unit == "mi" else self.distance.magnitude
        return distance_km / self.PACE_KM_PER_HOUR

    def summary(self):
        return f"Trail run: {self.name} - {self.distance}"

class GearMixin:
    def gear_list(self):
        return [
            "water",
            "first aid kit",
            "trail map"
        ]


class GuidanceMixin:
    def guidance(self):
        return "Follow marked trail signs and stay on the designated route."

class AdventureDayHike(GearMixin, GuidanceMixin, DayHike):
    pass

class GuidedDayHike(DayHike):
    def __init__(
        self,
        trail_id,
        name,
        distance,
        elevation_gain_m,
        difficulty,
        guide_name
    ):
        super().__init__(
            trail_id,
            name,
            distance,
            elevation_gain_m,
            difficulty
        )

        self.guide_name = guide_name

    def summary(self):
        base_summary = super().summary()
        return f"{base_summary} - Guide: {self.guide_name}"