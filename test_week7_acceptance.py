from waypoint_core.distance import Distance
from waypoint_core.trail import DayHike, TrailRun
from waypoint_core.itinerary import Itinerary


# Acceptance Test 1:

trail_data = {
    "id": 101,
    "name": "Maple Ridge Trail",
    "distance": 10,
    "unit": "km",
    "elevation_gain_m": 500,
    "difficulty": "moderate"
}

trail = DayHike.from_dict(trail_data)

assert trail.name == "Maple Ridge Trail"
assert trail.distance.magnitude == 10
assert trail.distance.unit == "km"
assert trail.elevation_gain_m == 500
assert trail.difficulty == "moderate"

try:
    Distance(-5, "km")
    assert False, "Negative distance should raise ValueError"
except ValueError:
    pass

try:
    DayHike(
        102,
        "Invalid Trail",
        Distance(5, "km"),
        100,
        "invalid"
    )
    assert False, "Invalid difficulty should raise ValueError"
except ValueError:
    pass


# Acceptance Test 2:

trail_a = DayHike(
    200,
    "Trail A",
    Distance(5, "km"),
    100,
    "easy"
)

trail_b = TrailRun(
    200,
    "Completely Different Trail",
    Distance(20, "km"),
    900,
    "expert"
)

assert trail_a == trail_b


# Acceptance Test 3:

original = Distance(10, "km")
miles = original.convert()
back_to_km = miles.convert()

assert abs(back_to_km.magnitude - 10) < 0.0001


# Acceptance Test 4:

trail_1 = DayHike(
    301,
    "Trail One",
    Distance(5, "km"),
    100,
    "easy"
)

trail_2 = DayHike(
    302,
    "Trail Two",
    Distance(8, "km"),
    200,
    "moderate"
)

trail_3 = TrailRun(
    303,
    "Trail Three",
    Distance(7, "km"),
    300,
    "hard"
)

itinerary_1 = Itinerary()

itinerary_1.add_trail(trail_1)
itinerary_1.add_trail(trail_2)
itinerary_1.add_trail(trail_3)

assert itinerary_1.total_distance().magnitude == 20


# Acceptance Test 5:

itinerary_2 = Itinerary()

itinerary_2.add_trail(trail_1)

assert itinerary_2.total_distance().magnitude == 5

itinerary_1.add_trail(
    DayHike(
        304,
        "Extra Trail",
        Distance(10, "km"),
        400,
        "hard"
    )
)

assert itinerary_1.total_distance().magnitude == 30

# itinerary_2 must remain unchanged
assert itinerary_2.total_distance().magnitude == 5


# Acceptance Test 6:

existing_trail = DayHike(
    400,
    "Existing Trail",
    Distance(10, "km"),
    100,
    "easy"
)

DayHike.set_default_unit("mi")

new_trail_data = {
    "id": 401,
    "name": "New Trail",
    "distance": 10,
    "elevation_gain_m": 200,
    "difficulty": "moderate"
}

new_trail = DayHike.from_dict(new_trail_data)

assert existing_trail.distance.unit == "km"
assert new_trail.distance.unit == "mi"

# Restore default for future work
TrailRun.set_default_unit("km")


print("ALL WEEK 7 ACCEPTANCE TESTS PASSED")