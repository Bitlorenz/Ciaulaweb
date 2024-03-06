from django.urls import path
from .views import *

app_name = 'HolidayPlanning'
urlpatterns = [
    path("scegliattrazione/<pk>/<vacanza_id>", scegliattrazione, name="aggiungi"),  # la prima pk è dell'attrazione la seconda della vacanza
    path('scegliattrazione/<pk>/', scegliattrazione, name='scegli'),
    path("editscelta/<pk>/<vacanza_id>", ModificaScelta.as_view(), name="modificascelta"),
    path("cancellascelta/<pk>/<vacanza_id>", CancellaScelta.as_view(), name="cancellascelta"),
    path("spostamento/<par>/<vac>", AggiungiSpostamento.as_view(), name="spostamento"),
    path("creavacanza/", CreaVacanza.as_view(), name="creavacanza"),
    path("aggiungitour/<int:pk>", AggiungiTourVacanza.as_view(), name="aggiungitour"),
    path("vacanze/", VacanzeList.as_view(), name="vacanze"),
    path("vacanza/<int:pk>/", DettaglioVacanza.as_view(), name="dettagliovacanza"),
    path("vacanza/<pk>/modificavacanza/", ModificaVacanza.as_view(), name="modificavacanza"),
    path("vacanza/<pk>/stampavacanza/", stampaVacanza, name="stampavacanza"),
    path("tour/", vacanze_by_root, name="tourorganizzati"),
    path("dettour/<int:pk>", TourDetail.as_view(), name="dettagliotour")
    ]
