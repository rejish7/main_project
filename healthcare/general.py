
from .models import Setting

def global_data_pass(request):
    data = {
        'setting':Setting.objects.first(),    
    }
    return  data