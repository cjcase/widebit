from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from widebit_web import models

@login_required
def index(request):
	template = "index.html"
	context = {}

	nutrients = models.Nutrient.objects.all()
	context['nutrients'] = nutrients
	return render(request, template, context)

