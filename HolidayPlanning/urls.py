from django.urls import path
from .views import *

app_name = 'HolidayPlanning'
urlpatterns = [
    path("listaattrazioni/", AttrazioniHome.as_view(), name="listaattrazioni"),
    path("attrazioni/", AttrazioniList.as_view(), name="attrazioni"),
    path("scegliattrazione/<pk>", ScegliOrarioGiornoAttrazione.as_view(), name="scegliattrazione"),
    path("listascelte/", ScelteList.as_view(), name="scelte"),
    path("detscelta/<pk>", DetailSceltaEntita.as_view(), name="dettaglioscelta"),
    path("detattrazione/<pk>/", DetailAttrazioneEntita.as_view(), name="dettaglioattr"),
    path("editscelta/<pk>/", ModificaScelta.as_view(), name="modificascelta"),
    path("cancellascelta/<pk>", CancellaScelta.as_view(), name="cancellascelta"),
    path("cerca/", cerca, name="cerca"),
    path("risultati/<str:stringa>/<str:where>/", RisultatiList.as_view(), name="risultati"),
    path("sceltafatta/<pk>/", SceltaFattaView.as_view(), name="sceltafatta"),
    path("creavacanza/", CreaVacanza.as_view(), name="creavacanza"),
]
