from django.test import TestCase

from waypoint_core.distance import Distance

from .models import Trail


class TrailViewTests(TestCase):

    def test_catalog_shows_only_open_trails(self):
        Trail.objects.create(
            name="Open Trail",
            distance_km=5.00,
            elevation_gain=100,
            difficulty="easy",
            is_open=True,
        )

        Trail.objects.create(
            name="Closed Trail",
            distance_km=8.00,
            elevation_gain=200,
            difficulty="moderate",
            is_open=False,
        )

        response = self.client.get("/catalog/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Open Trail")
        self.assertNotContains(response, "Closed Trail")

    def test_trail_detail_returns_404_for_missing_trail(self):
        response = self.client.get("/catalog/trail/9999/")

        self.assertEqual(response.status_code, 404)


class DistanceTests(TestCase):

    def test_distance_rejects_negative_values(self):
        with self.assertRaises(ValueError):
            Distance(-5, "km")