from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, candidate_dashboard, add_post, job_search_list, category, job_details, maintenance
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _

if settings.MAINTENANCE_MODE == True:
    urlpatterns = [
        path('', maintenance, name="maintenance"),
        path('i18n/', include('django.conf.urls.i18n')),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns = [
        path('', home, name="home"),
        path('i18n/', include('django.conf.urls.i18n')),
        # for Users or applicants
        path('add_post/', add_post, name='add_post'),
        path('candidate_dashboard', candidate_dashboard, name="candidate_dash"),
        path('job/', job_search_list, name='job-search-list'),
        path('category/<slug:cat_slug>/', category, name='category'),
        path('job_details/<int:pk>', job_details, name='job_details'),
        # for Companies
        # path("company_signup/", views.company_signup, name="company_signup"),
        # path("company_login/", views.company_login, name="company_login"),
        # path("company_homepage/", views.company_homepage, name="company_homepage"),
        # path("add_job/", views.add_job, name="add_job"),
        # path("job_list/", views.job_list, name="job_list"),
        # path("edit_job/<int:myid>/", views.edit_job, name="edit_job"),
        # path("company_logo/<int:myid>/", views.company_logo, name="company_logo"),
        # for admin
        # path("admin_login/", views.admin_login, name="admin_login"),
        # path("view_applicants/", views.view_applicants, name="view_applicants"),
        # path("delete_applicant/<int:myid>/", views.delete_applicant, name="delete_applicant"),
        # path("pending_companies/", views.pending_companies, name="pending_companies"),
        # path("accepted_companies/", views.accepted_companies, name="accepted_companies"),
        # path("rejected_companies/", views.rejected_companies, name="rejected_companies"),
        # path("all_companies/", views.all_companies, name="all_companies"),
        # path("change_status/<int:myid>/", views.change_status, name="change_status"),
        # path("delete_company/<int:myid>/", views.delete_company, name="delete_company"),
        ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
