from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

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
