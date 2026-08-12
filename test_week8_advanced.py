from waypoint_core.distance import Distance
from waypoint_core.trail import (
    Trail,
    DayHike,
    BackpackingRoute,
    TrailRun,
    GuidedDayHike,
    AdventureDayHike,
)

# WP-203 Test 1:
# DayHike should initialize the Trail fields through super().__init__.

day_hike = DayHike(
    501,
    "Day Hike",
    Distance(8, "km"),
    300,
    "easy",
)

assert day_hike.id == 501
assert day_hike.name == "Day Hike"
assert day_hike.distance.magnitude == 8
assert day_hike.distance.unit == "km"
assert day_hike.elevation_gain_m == 300
assert day_hike.difficulty == "easy"


# WP-203 Test 2:
# BackpackingRoute should also initialize Trail fields through super().

backpacking = BackpackingRoute(
    502,
    "Backpacking Route",
    Distance(12, "km"),
    800,
    "hard",
)

assert backpacking.id == 502
assert backpacking.name == "Backpacking Route"
assert backpacking.distance.magnitude == 12
assert backpacking.elevation_gain_m == 800
assert backpacking.difficulty == "hard"


# WP-203 Test 3:
# TrailRun should initialize Trail fields through super().

trail_run = TrailRun(
    503,
    "Trail Run",
    Distance(6, "km"),
    150,
    "moderate",
)

assert trail_run.id == 503
assert trail_run.name == "Trail Run"
assert trail_run.distance.magnitude == 6
assert trail_run.elevation_gain_m == 150
assert trail_run.difficulty == "moderate"


# WP-203 Test 4:
# GuidedDayHike adds a new field while inheriting
# the normal DayHike/Trail fields.

guided = GuidedDayHike(
    504,
    "Guided Mountain Trail",
    Distance(8, "km"),
    400,
    "moderate",
    "Alex",
)

assert guided.id == 504
assert guided.name == "Guided Mountain Trail"
assert guided.distance.magnitude == 8
assert guided.elevation_gain_m == 400
assert guided.difficulty == "moderate"
assert guided.guide_name == "Alex"


# WP-203 Test 5:
# GuidedDayHike should still use DayHike's estimated_time().

assert guided.estimated_time() == 2.0


# WP-203 Test 6:
# Verify the inheritance hierarchy.

assert GuidedDayHike.__mro__[0] is GuidedDayHike
assert GuidedDayHike.__mro__[1] is DayHike
assert GuidedDayHike.__mro__[2].__name__ == "Trail"


print("ALL WP-203 TESTS PASSED")

# WP-204 Test 1:


guided_summary = guided.summary()

assert guided_summary == (
    "Day hike: Guided Mountain Trail - 8 km - Guide: Alex"
)


# WP-204 Test 2:


regular_day_hike = DayHike(
    505,
    "Regular Mountain Trail",
    Distance(8, "km"),
    300,
    "moderate",
)

assert regular_day_hike.summary() == (
    "Day hike: Regular Mountain Trail - 8 km"
)


print("ALL WP-203 AND WP-204 TESTS PASSED")

# WP-205 Test 1:
# AdventureDayHike should receive behavior from both mixins.

adventure = AdventureDayHike(
    601,
    "Adventure Trail",
    Distance(10, "km"),
    400,
    "hard",
)

assert adventure.gear_list() == [
    "water",
    "first aid kit",
    "trail map"
]

assert adventure.guidance() == (
    "Follow marked trail signs and stay on the designated route."
)


# WP-205 Test 2:
# AdventureDayHike should still receive DayHike behavior.

assert adventure.estimated_time() == 2.5


# WP-205 Test 3:
# Verify the expected MRO.

mro = AdventureDayHike.__mro__

assert mro[0] is AdventureDayHike
assert mro[1].__name__ == "GearMixin"
assert mro[2].__name__ == "GuidanceMixin"
assert mro[3] is DayHike


print("ALL WP-203, WP-204 AND WP-205 TESTS PASSED")

# WP-206:
# One polymorphic loop should work with different trail types
# without checking their concrete classes.

def print_estimated_times(trails):
    for trail in trails:
        print(f"{type(trail).__name__}: {trail.estimated_time()}")


# WP-206 Test 1:
# A mixed list of different Trail subclasses should work.

mixed_trails = [
    DayHike(
        701,
        "Day Hike",
        Distance(8, "km"),
        300,
        "easy",
    ),
    BackpackingRoute(
        702,
        "Backpacking Route",
        Distance(9, "km"),
        700,
        "hard",
    ),
    TrailRun(
        703,
        "Trail Run",
        Distance(8, "km"),
        200,
        "moderate",
    ),
]

print_estimated_times(mixed_trails)


# WP-206 Test 2:
# FakeTrail uses duck typing.
# It does NOT inherit from Trail.

class FakeTrail:
    def __init__(self, estimated_hours):
        self._estimated_hours = estimated_hours

    def estimated_time(self):
        return self._estimated_hours


fake_trail = FakeTrail(1.5)

assert not isinstance(fake_trail, Trail)
assert fake_trail.estimated_time() == 1.5


# WP-206 Test 3:
# FakeTrail should work in the exact same polymorphic loop.

mixed_with_fake = mixed_trails + [fake_trail]

print_estimated_times(mixed_with_fake)


print("ALL WP-203, WP-204, WP-205 AND WP-206 TESTS PASSED")