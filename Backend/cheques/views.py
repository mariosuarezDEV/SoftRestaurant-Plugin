import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.formats import date_format

from .models import Cheques, Cheqdet, Productos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

