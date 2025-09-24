from django import forms
from .models import BudgetAlert

class BudgetAlertForm(forms.ModelForm):
    notifications = forms.MultipleChoiceField(
        choices=BudgetAlert.NOTIFICATION_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = BudgetAlert
        fields = ['category', 'amount_limit', 'trigger_threshold', 'notifications']
