from django.views.generic import CreateView, UpdateView, DeleteView
from Apps.comments.models import Commentaires

class Createcomments(CreateView):
    model = Commentaires
    success_url = '/Cv/'
    