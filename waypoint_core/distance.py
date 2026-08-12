class Distance:
    KM_TO_MILES = 0.621371

    def __init__(self, magnitude, unit):
        if magnitude < 0:
            raise ValueError("Distance cannot be negative")

        if unit not in ("km", "mi"):
            raise ValueError("Unit must be 'km' or 'mi'")

        self._magnitude = magnitude
        self._unit = unit

    @property
    def magnitude(self):
        return self._magnitude

    @property
    def unit(self):
        return self._unit

    def convert(self):
        if self._unit == "km":
            converted_magnitude = self._magnitude * self.KM_TO_MILES
            return Distance(converted_magnitude, "mi")

        converted_magnitude = self._magnitude / self.KM_TO_MILES
        return Distance(converted_magnitude, "km")

    def _to_km(self):
        """Return the distance magnitude expressed in kilometers."""
        if self._unit == "km":
            return self._magnitude

        return self._magnitude / self.KM_TO_MILES

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented

        total_km = self._to_km() + other._to_km()
        return Distance(total_km, "km")

    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented

        difference_km = self._to_km() - other._to_km()

        if difference_km < 0:
            raise ValueError("Distance cannot be negative")

        return Distance(difference_km, "km")

    def __eq__(self, other):
        if not isinstance(other, Distance):
            return False

        return abs(self._to_km() - other._to_km()) < 0.000001

    def __lt__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented

        return self._to_km() < other._to_km()

    def __le__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented

        return self._to_km() <= other._to_km()

    def __gt__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented

        return self._to_km() > other._to_km()

    def __ge__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented

        return self._to_km() >= other._to_km()

    def __str__(self):
        return f"{self._magnitude:g} {self._unit}"

    def __repr__(self):
        return f"Distance({self._magnitude!r}, {self._unit!r})"