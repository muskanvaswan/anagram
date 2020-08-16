from django.shortcuts import render
from .util import solve
# Create your views here.
def ana(request):
    return render(request, "anagram/form.html")

def solution(request):
    a = request.POST["q"]
    sol = solve2(a)
    context = {
        "s": sol,
        "given": a
    }
    return render(request, "anagram/result.html", context)
