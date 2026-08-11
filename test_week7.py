from waypoint_core.distance import Distance
from waypoint_core.trail import Trail


# Test 1: Create a Trail directly
trail1 = Trail(
    1,
    "Blue Mountain Trail",
    Distance(8, "km"),
    450,
    "moderate"
)

print("Trail:", trail1)
print("Difficulty:", trail1.difficulty)


# Test 2: Create a Trail from a dictionary
trail_data = {
    "id": 2,
    "name": "Lake Trail",
    "distance": 5,
    "unit": "km",
    "elevation_gain_m": 200,
    "difficulty": "easy"
}

trail2 = Trail.from_dict(trail_data)

print("Trail from dictionary:", trail2)
print("Trail 2 difficulty:", trail2.difficulty)


# Test 3: Invalid difficulty
try:
    Trail(
        3,
        "Bad Trail",
        Distance(10, "km"),
        300,
        "impossible"
    )
except ValueError as error:
    print("Invalid difficulty test passed:", error)


# Test 4: Same ID means equal
trail3 = Trail(
    1,
    "Completely Different Trail",
    Distance(20, "km"),
    800,
    "hard"
)

print("Same ID equals:", trail1 == trail3)


# Test 5: Different ID means not equal
print("Different ID equals:", trail1 == trail2)


# Test 6: Change default unit
Trail.set_default_unit("mi")

trail4_data = {
    "id": 4,
    "name": "Mountain View",
    "distance": 10,
    "elevation_gain_m": 500,
    "difficulty": "hard"
}

trail4 = Trail.from_dict(trail4_data)

print("New trail default unit:", trail4.distance.unit)

# Restore default for later tests
Trail.set_default_unit("km")

from waypoint_core.itinerary import Itinerary


# Test 7: Create an itinerary
itinerary1 = Itinerary()

itinerary1.add_trail(trail1)
itinerary1.add_trail(trail2)
itinerary1.add_trail(trail3)

print("Itinerary 1 total:", itinerary1.total_distance())


# Test 8: A second itinerary should be independent
itinerary2 = Itinerary()

itinerary2.add_trail(trail2)

print("Itinerary 2 total:", itinerary2.total_distance())


# Test 9: Adding to itinerary 1 should not change itinerary 2
itinerary1.add_trail(trail4)

print("Itinerary 1 after adding trail 4:", itinerary1.total_distance())
print("Itinerary 2 remains:", itinerary2.total_distance())