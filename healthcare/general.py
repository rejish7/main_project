from unicodedata import category
from .models import Category,Setting

def global_data_pass(request):
    data = {
        'categories':Category.objects.all(),
        'setting':Setting.objects.all()
        
    }
    return data