from django.shortcuts import render


def home(request):
    return render(request, "home.html", {"greeting": "Welcome to Waypoint!"})


def report(request):
    if request.method == "GET":
        return render(request, "report.html")

    name = request.POST.get("name", "")
    email = request.POST.get("email", "")
    trail = request.POST.get("trail", "")
    note = request.POST.get("note", "")

    return render(
        request,
        "thank_you.html",
        {
            "name": name,
            "email": email,
            "trail": trail,
            "note": note,
        },
    )

def search(request):
    query = request.GET.get("q", "")

    return render(
        request,
        "search.html",
        {"query": query},
    )
def catalog(request):
    trails = [
        {
            "name": "Pine Ridge Trail",
            "distance": 5.5,
            "elevation": 220,
            "difficulty": "easy",
            "is_open": True,
        },
        {
            "name": "Eagle Peak",
            "distance": 8.2,
            "elevation": 450,
            "difficulty": "moderate",
            "is_open": True,
        },
        {
            "name": "Mountain Pass",
            "distance": 12.7,
            "elevation": 780,
            "difficulty": "hard",
            "is_open": True,
        },
        {
            "name": "Canyon Loop",
            "distance": 15.4,
            "elevation": 920,
            "difficulty": "expert",
            "is_open": False,
        },
        {
            "name": "Lake View Trail",
            "distance": 6.8,
            "elevation": 310,
            "difficulty": "moderate",
            "is_open": True,
        },
        {
            "name": "Forest Challenge",
            "distance": 10.9,
            "elevation": 650,
            "difficulty": "expert",
            "is_open": False,
        },
    ]

    return render(
        request,
        "catalog.html",
        {"trails": trails},
    )
