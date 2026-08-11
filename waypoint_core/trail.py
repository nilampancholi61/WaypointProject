from waypoint_core.distance import Distance


class Trail:
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

    def __eq__(self, other):
        if not isinstance(other, Trail):
            return False

        return self.id == other.id

    def __str__(self):
        return f"{self.name} ({self.distance})"