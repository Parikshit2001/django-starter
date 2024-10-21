from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, "app_starter/all_chai.html", {"chais": chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, "app_starter/chai_detail.html", {"chai": chai})