from waypoint_core.distance import Distance
from waypoint_core.trail import (
    Trail,
    DayHike,
    BackpackingRoute,
    TrailRun
)


# WP-201: Trail must be abstract

try:
    Trail(
        1,
        "Test Trail",
        Distance(5, "km"),
        100,
        "easy"
    )
    assert False, "Trail should not be directly instantiable"
except TypeError:
    pass


# WP-201: Concrete trail classes

day_hike = DayHike(
    2,
    "Day Hike",
    Distance(8, "km"),
    200,
    "moderate"
)

backpacking = BackpackingRoute(
    3,
    "Backpacking Route",
    Distance(8, "km"),
    500,
    "hard"
)

trail_run = TrailRun(
    4,
    "Trail Run",
    Distance(8, "km"),
    100,
    "easy"
)

assert day_hike.estimated_time() == 2.0
assert backpacking.estimated_time() == 8 / 3
assert trail_run.estimated_time() == 1.0

assert day_hike.summary()
assert backpacking.summary()
assert trail_run.summary()


# WP-202: Addition

result = Distance(3, "km") + Distance(2, "km")

assert result.magnitude == 5
assert result.unit == "km"


# WP-202: Subtraction

result = Distance(5, "km") - Distance(2, "km")

assert result.magnitude == 3
assert result.unit == "km"


# WP-202: Equality

assert Distance(5, "km") == Distance(5, "km")
assert Distance(1, "km") == Distance(0.621371, "mi")


# WP-202: Comparisons

assert Distance(5, "km") > Distance(2, "km")
assert Distance(2, "km") < Distance(5, "km")


# WP-202: Sorting

distances = [
    Distance(5, "km"),
    Distance(1, "km"),
    Distance(3, "km")
]

sorted_distances = sorted(distances)

assert sorted_distances[0] == Distance(1, "km")
assert sorted_distances[1] == Distance(3, "km")
assert sorted_distances[2] == Distance(5, "km")


# WP-202: String representation

distance = Distance(5, "km")

assert str(distance) == "5 km"
assert repr(distance) == "Distance(5, 'km')"


# WP-202: Mixed-unit arithmetic

mixed_addition = Distance(5, "km") + Distance(1, "mi")

assert abs(mixed_addition.magnitude - 6.6093445) < 0.000001
assert mixed_addition.unit == "km"

mixed_subtraction = Distance(5, "km") - Distance(1, "mi")

assert abs(mixed_subtraction.magnitude - 3.3906555) < 0.000001
assert mixed_subtraction.unit == "km"


print("ALL WEEK 8 WP-201 AND WP-202 TESTS PASSED")