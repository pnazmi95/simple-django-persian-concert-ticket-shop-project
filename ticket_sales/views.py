from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import ticket_sales
from .models import (
    ProfileModel,
    TimeModel,
    TicketModel,
    ConcertModel,
    LocationModel,
)
import accounts
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import SearchForm, ConcertForm
from django.views import View


def concert_list_view(request):
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        search_text = search_form.cleaned_data["search_text"]
        concerts = ConcertModel.objects.filter(name__contains=search_text)
    else:
        concerts = ConcertModel.objects.all()

    context = {
        "concert_list": concerts,
        "concert_count": concerts.count(),
        "search_form": search_form
    }

    return render(request, "ticket_sales/concert_list.html", context=context)


class LocationListView(View):
    template_name = "ticket_sales/location_list.html"

    def get(self, request):
        locations = LocationModel.objects.all()

        context = {
            "location_list": locations,
        }

        return render(request, self.template_name, context=context)


class ConcertDetailsView(View):
    template_name = "ticket_sales/concert_details.html"

    def get(self, request, concert_id):
        concert = ConcertModel.objects.get(pk=concert_id)

        context = {
            "concert_details": concert
        }

        return render(request, self.template_name, context)


class TimeView(View):
    template_name = "ticket_sales/time_list.html"

    def get(self, request):
        times = TimeModel.objects.all()

        context = {
            "time_list": times,
        }

        return render(request, self.template_name, context)


class ConcertEditView(View):
    template_name = "ticket_sales/concert_edit.html"
    form_class = ConcertForm

    def post(self, request, concert_id):
        concert = ConcertModel.objects.get(pk=concert_id)

        concert_form = self.form_class(request.POST, request.FILES, instance=concert)
        if concert_form.is_valid:
            concert_form.save()
            return redirect('ticket_sales:concert_list_view')
        else:
            context = {
                "concert_form": concert_form,
                "concert_pic": concert.poster
            }

            return render(request, self.template_name, context)

    def get(self, request, concert_id):
        concert = ConcertModel.objects.get(pk=concert_id)
        concert_form = self.form_class(instance=concert)
        context = {
            "concert_form": concert_form,
            "concert_pic": concert.poster
        }
        return render(request, self.template_name, context)
