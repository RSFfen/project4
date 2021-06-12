from django.views.generic import TemplateView, CreateView 
from .models import Comment

class HomePageView(TemplateView):
    template_name = 'home.html'
    context_object_name = 'all_comments_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_comments_list'] = Comment.objects.all()
        return context

class AboutPageView(TemplateView):
    template_name = 'about.html'

class KorolIShutPageView(TemplateView):
    template_name = 'korolishut.html'

class SektorGazaPageView(TemplateView):
    template_name = 'sektorgaza.html'

class KinoPageView(TemplateView):
    template_name = 'kino.html'

class LeningradPageView(TemplateView):
    template_name = 'leningrad.html'

class ZveriPageView(TemplateView):
    template_name = 'zveri.html'

class SplinPageView(TemplateView):
    template_name = 'splin.html'

class DDTPageView(TemplateView):
    template_name = 'ddt.html'

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_new.html'
    fields = ('text',)