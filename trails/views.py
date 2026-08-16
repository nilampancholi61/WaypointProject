from django.shortcuts import render

from .models import Park, Trail


def catalog(request):
    park_id = request.GET.get("park")

    trails = Trail.objects.filter(
        is_open=True
    ).order_by("distance_km")

    selected_park = None

    if park_id:
        selected_park = Park.objects.get(id=park_id)
        trails = trails.filter(park=selected_park)

    return render(
        request,
        "catalog.html",
        {
            "trails": trails,
            "parks": Park.objects.all().order_by("name"),
            "selected_park": selected_park,
        },
    )