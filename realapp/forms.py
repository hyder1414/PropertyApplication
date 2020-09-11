from .models import Property
from django.forms import ModelForm
class PropertyForm(ModelForm):
   class Meta:
      model=Property
      fields=['propertyid','propaddress','propcity','propstate','propzip','listingdate','solddate','saleprice','officeid']
