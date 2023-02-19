from django.contrib import admin

from .models import (
    ConcertModel,
    TimeModel,
    TicketModel,
    LocationModel,
)

admin.site.register(ConcertModel)
admin.site.register(LocationModel)
admin.site.register(TimeModel)
admin.site.register(TicketModel)
