from django.shortcuts import render, get_object_or_404
from django.views.generic import  DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Property, Propertyowner, Propertyownership, Salesoffice, Firm, Employee
from .forms import PropertyForm
from django.http import HttpResponseRedirect
# Create your views here.
# we have two kinds of
def index(request):
   title=" Real Estate Firm System"
   intro=" This is a simple website for a real estate firm"
   return render(request, 'realapp/index.html',{'title': title, 'intro':intro})

def property_list(request):
    propertyList=Property.objects.all()
    return render(request,'realapp/propertylist.html', {'title': 'List of Properties','propertylist':propertyList})
def property_detail(request, id):
  pid=int(id)
  propertyDetail=Property.objects.get(propertyid=pid)
  return render(request, 'realapp/propertydetail.html', {'title': 'Property Details', 'propertydetail':propertyDetail})
#-- a form view
def property_edit(request, id):
# retrieve the property by id
   pid=int(id)
   submitted=False
 #  oneProperty=get_object_or_404(Property, propertyid=pid)
   oneProperty=Property.objects.get(pk=pid)
   if request.method=='POST':
     #form was submitted
     form=PropertyForm(request.POST)
     if form.is_valid():
        # form fields passed validation
  #     p=Property.objects.get(pk=pid)
       f=PropertyForm(request.POST, instance=p)
       f.save()
   else:
       form=PropertyForm(oneProperty)
#       form.populate_obj(oneProperty)
   return render(request, 'realapp/propertyedit.html',{'form':form})
class PropertyUpdate(UpdateView):
   model=Property
   fields=['propaddress','propcity','propstate','propzip','listingdate','solddate','saleprice','officeid' ]
   success_url=reverse_lazy('property_list')
   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pagetitle'] = "Edit Property Details"
        return context
class PropertyCreate(CreateView):
   model=Property
   fields='__all__'
   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pagetitle'] = "Add a New Property Details"
        return context
class OwnerList(ListView):
    model=Propertyowner
    success_url=reverse_lazy('owner_list')
class OwnerDetail(DetailView):
    model=Propertyowner
    success_url=reverse_lazy('owner_list')
class OwnerUpdate(UpdateView):
    model=Propertyowner
    fields=['ownerlastname','ownerfirstname']
#    template_name='templates\realapp\propertyowner_update.html'
    success_url=reverse_lazy('owner_list')

class PropertyOwnerList(ListView):
    template_name='realapp/ownershipsearchlist.html'
    def get_queryset(self):
        if self.request.method=="GET":
           zipcode=self.request.GET.get('zipcode', None)
      # add in a queryset
           if zipcode is not None:
             return  Propertyownership.objects.all().select_related('propertyid', 'ownerid').filter(
     propertyid__propzip=zipcode).values(
     'propertyid','propertyid__propaddress', 'propertyid__propcity','propertyid__propzip','percentowned','propertyid__solddate','ownerid', 'ownerid__ownerfirstname','ownerid__ownerlastname')
 #     print (results)
  #    return results




