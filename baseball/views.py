from django.shortcuts import render, get_object_or_404 #does try/catch in one line
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Batter
from .forms import BatterForm


def index(request):
    all_batters = Batter.objects.all()
    return render(request, 'baseball/index.html', {'all_batters': all_batters})

def detail(request, batter_id):
    batter = get_object_or_404(Batter, pk=batter_id) #replaces try/except statement
    return render(request, 'baseball/detail.html', {'batter': batter})

@login_required()
def new_batter(request): #add a new batter
    if request.method != 'POST': #no data submitted, create blank form
        form = BatterForm()
    else: #POST data submitted, process the data
        form = BatterForm()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('baseball:batters'))

    context = {'form': form}
    return render(request, 'baseball/new_batter.html', context)



"""

Needs work
def edit_batter(request, batter_id):
    #edit existing player
    batter = Batter.objects.get(pk=batter_id)
    if request.method != 'POST':
        form = BatterForm(instance=batter)
    else:  # POST data submitted, process the data
        form = BatterForm(instance=batter, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('baseball:batters', args=[batter_id]))


    context = {'batter': batter, 'form': form}
    return render(request, 'baseball/edit_batter.html', context)
"""