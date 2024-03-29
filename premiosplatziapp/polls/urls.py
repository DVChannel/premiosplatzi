from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
   path("",  views.IndexView.as_view(), name="index"),
    #ex: /polls/5/
    path("<int:pk>/detail/",  views.DetailView.as_view(), name="detail"),
    #ex: /polls/5/results
    path("<int:pk>/results/",  views.results, name="results"),
    #ex: /polls/5/vote
    path("<int:question_id>/results/vote",  views.ResultView.as_view(), name="vote"),
]