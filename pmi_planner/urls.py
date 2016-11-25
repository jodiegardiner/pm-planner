from django.conf.urls import url, include
from django.contrib import admin
from core import views as core_views
from accounts import urls as accounts_urls
from threads import urls as forum_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.get_index, name="index"),

    url(r'^client/$', core_views.client_list, name='clients'),
    url(r'^client/(?P<id>\d+)$', core_views.client_details, name='client_detail'),
    url(r'^create/', core_views.create_client, name="create"),

    url(r'^update_add/', core_views.update_address, name="update_add"),
    url(r'^update_email/', core_views.update_email, name="update_email"),
    url(r'^update_phone/', core_views.update_phone, name="update_phone"),
    url(r'^update_c_notes/', core_views.update_c_notes, name="update_c_notes"),
    url(r'^update_p_notes/', core_views.update_p_notes, name="update_p_notes"),
    url(r'^update_due_date/', core_views.update_due_date, name="update_due_date"),
    url(r'^update_dob/', core_views.update_dob, name="update_dob"),
    url(r'^update_height/', core_views.update_height, name="update_height"),
    url(r'^update_weight/', core_views.update_weight, name="update_weight"),
    url(r'^update_bmi/', core_views.update_bmi, name="update_bmi"),
    url(r'^update_bt/', core_views.update_bt, name="update_bt"),
    url(r'^update_haemo/', core_views.update_haemo, name="update_haemo"),
    url(r'^update_sero/', core_views.update_sero, name="update_sero"),
    url(r'^update_gp/', core_views.update_gp, name="update_gp"),
    url(r'^update_gp_tel/', core_views.update_gp_tel, name="update_gp_tel"),
    url(r'^update_hosp/', core_views.update_hosp, name="update_hosp"),
    url(r'^update_hosp_num/', core_views.update_hosp_num, name="update_hosp_num"),
    url(r'^update_para/', core_views.update_para, name="update_para"),
    url(r'^update_prev_pregs/', core_views.update_prev_pregs, name="update_prev_pregs"),
    url(r'^update_wcc/', core_views.update_wcc, name="update_wcc"),
    url(r'^update_phn/', core_views.update_phn, name="update_phn"),
    url(r'^update_cons/', core_views.update_cons, name="update_cons"),
    url(r'^update_p_site/', core_views.update_p_site, name="update_p_site"),

    url(r'', include(accounts_urls)),
    url(r'', include(forum_urls)),
]
