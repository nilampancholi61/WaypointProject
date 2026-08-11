from waypoint_core.distance import Distance


class Itinerary:
    def __init__(self):
        self.trails = []

    def add_trail(self, trail):
        self.trails.append(trail)

    def total_distance(self):
        total_km = 0

        for trail in self.trails:
            if trail.distance.unit == "km":
                total_km += trail.distance.magnitude
            else:
                total_km += trail.distance.convert().magnitude

        return Distance(total_km, "km")