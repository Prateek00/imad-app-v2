# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import PermissionsMixin
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect;
from . models import Leave, ApplicationRequest, RemainingLeaves;
from django.contrib.auth.decorators import login_required;
from . forms import LeaveForm, UserForm;
from django.db import transaction
from django.contrib.auth.models import User
import os;
from django.db.models import Max
from django.contrib import messages
from userprofile.models import FacultyProfile


# Create your views here.
@login_required(login_url='/login')
@transaction.atomic
def getLeaveTemplate(request):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)));
	if request.method == 'POST':
		leave_form = LeaveForm(request.POST)
		if leave_form.is_valid():
			instance = leave_form.save(commit=False);	
			instance.user = request.user;
			faculty = FacultyProfile.objects.filter(user = request.user ).first();
			print(faculty);
			instance.leaveto = faculty.facultyLeaveHead;

			last_id = Leave.objects.all().aggregate(Max('leave_id'));
			if last_id is not None:
				instance.leave_id = last_id['leave_id__max'] + 1;
			else:
				instance.leave_id = 1;
			print(last_id)
			instance.save();
			messages.success(request, 'Form submission successful')
			return HttpResponseRedirect('/leaveform');
	else:
		print(request.user.applied_for)
		leave_form = LeaveForm(initial={}); # returns a queryset and you need the leave?
	return render(request, BASE_DIR+"/templates/pages/leaveform.html", { 'leave_form':leave_form});

'''
@login_required(login_url='/login')
def getLeaveTemplate(request):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)));
	if request.method == 'POST':
		form = LeaveForm(request.POST, user=request.user)

		if form.is_valid():
			leave = Leave.objects.create(
				user = request.user,
				leave_type = leave_type,
				start_date = start_date,
				end_date = end_date,
				purpose = purpose,
				leave_address = form.cleaned_data['leave_address'],
				processing_status = processing_status,
			
			ApplicationRequest.objects.create(
				user = request.user,
				leave = leave,
			)

			return HttpResponse("Thankss");
	else:
		form = LeaveForm(initial={})
	return render(request, BASE_DIR+"/templates/pages/leaveform.html", {'form':form});
'''
