from django.shortcuts import render

from myproject.models import UserInsert
from django.contrib import messages


def insertRecord(request):
    if request.method == "POST":
        if request.POST.get("username") and request.POST.get("password"):
            saverecord = UserInsert()
            saverecord.username = request.POST.get("username")
            saverecord.password = request.POST.get("password")
            saverecord.save()
            messages.success(request, "Record Saved successfully")
            return render(request, "base.html", {})
    else:
        return render(request, "base.html", {})
