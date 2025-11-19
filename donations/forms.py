from django import forms
from datetime import date, datetime
from django.core.exceptions import ValidationError
from beneficiaries.models import Beneficiary
from stock.models import StockEntry 
from donations.models import Donation











class DonationRegisterForm(forms.Form):
  

    beneficiaries = forms.ModelMultipleChoiceField(
    queryset = Beneficiary.objects.none(),
    required = True,
    label= '',
    error_messages={
        'required': 'Selecione pelo menos um beneficiário.',
    },
    widget= forms.CheckboxSelectMultiple(attrs = {"class" : "block w-full rounded-lg border border-border-light bg-primary border focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2"}
    )

    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = date.today()
        
        self.fields['beneficiaries'].queryset = Beneficiary.objects.filter(
            status="active"
        ).exclude(
            donation__donation_month=str(today.month),
            donation__donation_year=today.year
        )



    def clean(self):
        cleaned_data = super().clean()
        selected_beneficiaries = cleaned_data.get('beneficiaries')
        
        if selected_beneficiaries:
            available_stock_entry = StockEntry.objects.filter(
                is_available=True
            ).exclude(
                donation__isnull=False
            ).count()
            
            beneficiaries_count = selected_beneficiaries.count()
            
            if beneficiaries_count > available_stock_entry:
                raise forms.ValidationError(
                    f'Apenas {available_stock_entry} entrada(s) de estoque disponível(is). '
                    f'Você selecionou {beneficiaries_count} beneficiário(s).'
                )
        
        return cleaned_data
    




    def save(self):
        today = date.today()
        now = datetime.now()
        selected_beneficiaries = self.cleaned_data['beneficiaries']
        
        available_stock_entries = StockEntry.objects.filter(
            is_available=True
        ).exclude(
            donation__isnull=False
        )[:selected_beneficiaries.count()]
        
        donations_created = []
        
        for beneficiary, stock_entry in zip(selected_beneficiaries, available_stock_entries):
            
            donation = Donation.objects.create(
                beneficiary_fk=beneficiary,
                stock_entry_fk=stock_entry,
                donation_month=str(today.month),
                donation_year=today.year,
                description=f" "
            )
            
            stock_entry.is_available = False
            stock_entry.exit_date = today
            stock_entry.exit_time = now.time()
            stock_entry.save()
            
            donations_created.append(donation)
        
        return donations_created


       


  