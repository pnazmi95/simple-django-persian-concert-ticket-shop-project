from django.shortcuts import render, redirect
from django.views import View


class HomeView(View):

    def get(self, request):
        return redirect('ticket_sales:concert_list_view')
