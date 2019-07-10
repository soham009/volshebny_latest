from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from generateletter.models import Visaletters
from translate import Translator

# Create your views here.

# Our original index view function
# Corresponds to original_index.html (rename it to index.html to use it!)

# def index(request):
#     my_dict = {'insert_me':"Now I am coming from first_app/index.html!"}
#     # Make sure this is pointing to the correct index
#     return render(request,'first_app/index.html',context=my_dict)

@method_decorator(login_required, name='dispatch')
class list_view(ListView):
    model = Visaletters
    context_object_name = "list_view"
    template_name = "generateletter/list.html"

@method_decorator(login_required, name='dispatch')
class list_view_copy(ListView):
    model = Visaletters
    context_object_name = "list_view"
    template_name = "generateletter/list_copy.html"

class gen_eng_visa(DetailView):
    model = Visaletters
    context_object_name = "detail_visa"
    template_name = "generateletter/gen_eng_visa.html"

class gen_rus_visa(DetailView):
    model = Visaletters
    context_object_name = "russian_visa"
    template_name = "generateletter/gen_rus_visa.html"

class gen_eng_voucher(DetailView):
    model = Visaletters
    context_object_name = "english_voucher"
    template_name = "generateletter/gen_eng_voucher.html"

class gen_rus_voucher(DetailView):
    model = Visaletters
    context_object_name = "russian_voucher"
    template_name = "generateletter/gen_rus_voucher.html"

def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'generateletter/error_500.html', data)

def reports(request):
    data = { }
    return render(request, 'generateletter/reports.html', data)


def visa_letter_detail(request,visa_letter_id):
    translator= Translator(to_lang="ru")
    russian_visa = Visaletters.objects.get(pk=int(visa_letter_id))
    russian = {'Country': translator.translate(russian_visa.Country.name),
               'Routes_and_Places': translator.translate(russian_visa.Routes_and_Places),
               'hotels': translator.translate(russian_visa.hotels),
               }
    return render(request, 'generateletter/russian_visaletter.html', { 'russian_visa': russian_visa,'russian': russian })
