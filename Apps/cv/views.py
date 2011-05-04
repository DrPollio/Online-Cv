from django.views.generic import ListView, DetailView
from Apps.cv.models import *

class CvView(DetailView):
    model=Info
    template_name='Cv/cv_detail.html'
    queryset=info.formation_set.all()