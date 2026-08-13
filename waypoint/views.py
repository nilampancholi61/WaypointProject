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
