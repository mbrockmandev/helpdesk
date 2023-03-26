from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
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
            print(ticket)
            return redirect("ticket_detail", ticket_id=ticket.id)
    else:
        form = TicketForm()
    return render(request, "new_ticket.html", {"form": form})


def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, "ticket_detail.html", {"ticket": ticket})


def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.delete()
    return redirect("ticket_list")


class MyLoginView(LoginView):
    template_name = "login.html"
    success_url = "/tickets/"
