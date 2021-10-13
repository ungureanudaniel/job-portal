from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Skill, AppliedJobs, SavedJobs, AvailableCountry
from recruiters.models import Job, Applicants, Selected
from .forms import ProfileUpdateForm, NewSkillForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator

#--------------------------------home view-------------------------------------
def home(request):
    template = 'candidates/home.html'
    countries_list = AvailableCountry.objects.all()
    context = {
        'home_page': "active",
        'countries_list': countries_list,
    }
    return render(request, template, context)

#----------------------------job search list ----------------------------------
def job_search_list(request):
    template = 'candidates/job_search_list.html'
    query = request.GET.get('p')
    loc = request.GET.get('q')
    object_list = []
    if(query == None):
        object_list = Job.objects.all()
    else:
        title_list = Job.objects.filter(title__icontains=query).order_by('-date_posted')
        skill_list = Job.objects.filter(skills_req__icontains=query).order_by('-date_posted')
        company_list = Job.objects.filter(company__icontains=query).order_by('-date_posted')
        job_type_list = Job.objects.filter(job_type__icontains=query).order_by('-date_posted')
        for i in title_list:
            object_list.append(i)
        for i in skill_list:
            if i not in object_list:
                object_list.append(i)
        for i in company_list:
            if i not in object_list:
                object_list.append(i)
        for i in job_type_list:
            if i not in object_list:
                object_list.append(i)
    if(loc == None):
        locat = Job.objects.all()
    else:
        locat = Job.objects.filter(
            location__icontains=loc).order_by('-date_posted')
    final_list = []
    for i in object_list:
        if i in locat:
            final_list.append(i)
    paginator = Paginator(final_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'jobs': page_obj,
        'query': query,
    }
    return render(request, template, context)

#----------------------------JOB DETAIL VIEW-----------------------------------
def job_detail(request, slug):
    template = 'candidates/job_detail.html'
    job = get_object_or_404(Job, slug=slug)
    apply_button = 0
    save_button = 0
    profile = Profile.objects.filter(user=request.user).first()
    if AppliedJobs.objects.filter(user=request.user).filter(job=job).exists():
        apply_button = 1
    if SavedJobs.objects.filter(user=request.user).filter(job=job).exists():
        save_button = 1
    relevant_jobs = []
    jobs1 = Job.objects.filter(
        company__icontains=job.company).order_by('-date_posted')
    jobs2 = Job.objects.filter(
        job_type__icontains=job.job_type).order_by('-date_posted')
    jobs3 = Job.objects.filter(
        title__icontains=job.title).order_by('-date_posted')
    for i in jobs1:
        if len(relevant_jobs) > 5:
            break
        if i not in relevant_jobs and i != job:
            relevant_jobs.append(i)
    for i in jobs2:
        if len(relevant_jobs) > 5:
            break
        if i not in relevant_jobs and i != job:
            relevant_jobs.append(i)
    for i in jobs3:
        if len(relevant_jobs) > 5:
            break
        if i not in relevant_jobs and i != job:
            relevant_jobs.append(i)

    context = {
        'job': job,
        'profile': profile,
        'apply_button': apply_button,
        'save_button': save_button,
        'relevant_jobs': relevant_jobs,
        'candidate_navbar': 1,
        }
    return render(request, template, context)

#--------------------------SAVED JOBS -----------------------------------------
@login_required
def saved_jobs(request):
    template = 'candidates/saved_jobs.html'
    jobs = SavedJobs.objects.filter(
        user=request.user).order_by('-date_posted')

    context = {
        'jobs': jobs,
        'candidate_navbar': 1,
        }
    return render(request, template, context)
