from django import forms
from django.utils import timezone

from .models import * 


class AddUserForm(forms.ModelForm):

    class Meta:
        model = OcservUser
        exclude = ('oc_active',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['desc'].widget.attrs.update({"rows" : '8'})

    def clean_oc_username(self):
        oc_username = self.cleaned_data['oc_username']
        obj = OcservUser.objects.filter(oc_username=oc_username)
        if obj.exists():
            raise forms.ValidationError("نام کاربری تکراری است".title())
        return oc_username

    def clean_expire_date(self):
        expire_date = self.cleaned_data['expire_date']  
        if expire_date and expire_date <= timezone.now().date():
            raise forms.ValidationError("تاریخ انقضا نمیتواند برابر و یا کوچکتر از تاریخ امروز باشد".title())
        return expire_date