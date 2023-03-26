from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm


# Create your views here.
def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, "ticket_list.html", {"tickets": tickets})


@login_required
def new_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("ticket_detail", pk=ticket.pk)
    else:
        form = TicketForm()
    return render(request, "new_ticket.html", {"form": form})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("ticket_list")
        else:
            return render(
                request, "login.html", {"error_message": "Invalid Login Credentials."}
            )
    else:
        return render(request, "login.html")
