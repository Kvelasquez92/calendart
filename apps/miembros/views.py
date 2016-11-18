from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from apps.miembros.forms import MemberForm

# Create your views here.

class MemberRegister(CreateView):
    form_class = MemberForm
    template_name = 'miembros/member_form.html'
    success_url = reverse_lazy('home:index')
