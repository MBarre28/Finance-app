from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
@login_required
def home(request):
    budgets = Budget.objects.filter(user=request.user)
    goals = SavingsGoal.objects.filter(user=request.user)
    return render(request, 'financeapp/home.html', {'budgets': budgets, 'goals': goals})

@login_required
def budget_list(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'financeapp/budget_list.html', {'budgets': budgets})

@login_required
def budget_create(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('budget_list')
    else:
        form = BudgetForm()
    return render(request, 'financeapp/budget_form.html', {'form': form})

@login_required
def goal_list(request):
    goals = SavingsGoal.objects.filter(user=request.user)
    return render(request, 'financeapp/goal_list.html', {'goals': goals})

@login_required
def goal_create(request):
    if request.method == 'POST':
        form = SavingsGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('goal_list')
    else:
        form = SavingsGoalForm()
    return render(request, 'financeapp/goal_form.html', {'form': form})