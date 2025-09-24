from django.shortcuts import render, redirect, get_object_or_404
from .models import BudgetAlert
from .forms import BudgetAlertForm

def budget_alerts(request):
    # Show all alerts (ignoring user for now)
    alerts = BudgetAlert.objects.all()

    if request.method == 'POST':
        form = BudgetAlertForm(request.POST)
        if form.is_valid():
            alert = form.save(commit=False)
            # no user assignment for now
            alert.save()
            return redirect('budget_alerts')
    else:
        form = BudgetAlertForm()

    return render(request, 'budget_alerts.html', {
        'form': form,
        'alerts': alerts
    })

def delete_alert(request, alert_id):
    alert = get_object_or_404(BudgetAlert, id=alert_id)
    alert.delete()
    return redirect('budget_alerts')
# Create your views here.