from django.shortcuts import render

# Create your views here.
def index(request):
	# Домашняя страница приложения LearningLog
	return render(request, 'learning_logs/index.html')