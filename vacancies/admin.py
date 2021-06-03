from django.contrib import admin
from .models import Vacancy, Company, Specialty, Application, Resume, StatusModel, GradeModel
from .token import account_activation_token
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from .models import Specialty, Application
from django.views.generic import CreateView
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .queue import SendMail
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.postgres.search import SearchVector
from .token import account_activation_token

# def send_letter(modeladmin, request, queryset):
#     queryset[0].user.profile.verified_token = account_activation_token.make_token(queryset[0].user)
#     queryset[0].user.save()
#     VERIFY_URL = (f'http://127./news/{queryset[0].user.profile.verified_token}/verify/')
#     html_message1 = loader.render_to_string('news/html-message.html', {
#     'user': queryset[0].user.username,
#     'verify_ulr': VERIFY_URL,
#     'date': date
#     })
#     mail = EmailMessage("Письмо подтверждения", html_message1, to=[f'{queryset[0].user.email}'])
#     new_send_email(mail)

ad = SendMail()


def send_letter(useras, resumesa, queryset):
    for resume in queryset:
        resume.token = account_activation_token.make_token(resume.user)
        resume.save()
        VERIFY_URL = (f'https://jumanji-vacancies.herokuapp.com/{resume.user.resume.token}/verify/')
        resume.user.save()
        html = loader.render_to_string('EmailHTML.html', {
            'user': resume.user,
            'url': VERIFY_URL
        })
        mail = EmailMessage("Письмо подтверждения", html, to=[f'{resume.user.email}'])
        ad.new_send_email(email=mail)


send_letter.short_description = 'Sending mails'


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'verified')
    actions = [send_letter]


admin.site.register(Resume, CustomUserAdmin)
admin.site.register(Vacancy)
admin.site.register(GradeModel)
admin.site.register(StatusModel)
admin.site.register(Company)
admin.site.register(Specialty)
admin.site.register(Application)
