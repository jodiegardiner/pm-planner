from __future__ import print_function
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, reverse
from .forms import ClientCreationForm
from .models import Client, PregnancyEvent, Pregnancy
from django.utils import timezone
from calendar_api import create_calendar_entries
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
import datetime
from event_package import generate_events
from oauth2client import client
from pmi_planner import settings
from oauth2client.client import OAuth2WebServerFlow


# Create your views here.


def get_index(request):
    return render(request, 'index.html')


@login_required(login_url='/login/')
def create_client(request):
    if request.method == 'POST':
        form = ClientCreationForm(request.POST)
        if form.is_valid():
            client = form.save()
            preg = Pregnancy()
            preg.client = client
            if form.data['due_date']:
                due_date = datetime.datetime.strptime(request.POST.get('due_date', timezone.now()), "%Y-%m-%d")
                preg.due_date = due_date
                preg.week_care_commences = int(request.POST.get('purchased_plan'))

                # Google Calendar event generation temporarily disabled

                # events = generate_events(preg, client)
                # responses = create_calendar_entries(events)
                # for response in responses:
                #     messages.success(request,
                #                  "<a target='_blank' href=" + response["url"] + "><p>Google Calendar event created - " + response[
                #                      "name"] + " - click to view</p></a>")

            preg.save()
            messages.success(request, "Client created successfully")

            return redirect(client_details, client.pk)
    else:
        form = ClientCreationForm()

    args = {'form': form}
    return render(request, 'create.html', args)


@login_required(login_url='/login/')
def client_list(request):
    clients = Client.objects.filter()
    pregs = Pregnancy.objects.filter()
    return render(request, "client_list.html", {'clients': clients, 'pregs': pregs})


@login_required(login_url='/login/')
def client_details(request, id):
    client = get_object_or_404(Client, pk=id)
    pregs = Pregnancy.objects.filter(client=client.id)
    return render(request, "client_detail.html", {'client': client, 'pregs': pregs})


def search(request):
    search_term = request.GET.get('search_term')
    clients = Client.objects.filter(name__icontains=search_term)
    if len(clients) > 0:
        return render(request, "client_list.html", {'clients': clients})
    else:
        messages.error(request, "No matches for the search: '" + search_term + "'.")
        clients = Client.objects.filter()
        return render(request, "client_list.html", {'clients': clients})


def update_address(request):
    id = request.POST.get('pk')
    client = get_object_or_404(Client, pk=id)
    client.address = request.POST.get('value')
    client.save()
    messages.success(request, "Successfully updated client address")
    return render(request, "client_detail.html")


def update_email(request):
    id = request.POST.get('pk')
    client = get_object_or_404(Client, pk=id)
    client.email = request.POST.get('value')
    client.save()
    messages.success(request, "Successfully updated client email")
    return render(request, "client_detail.html")


def update_phone(request):
    id = request.POST.get('pk')
    client = get_object_or_404(Client, pk=id)
    client.phone = request.POST.get('value')
    client.save()
    messages.success(request, "Successfully updated client phone number")
    return render(request, "client_detail.html")


def update_c_notes(request):
    id = request.POST.get('pk')
    client = get_object_or_404(Client, pk=id)
    client.notes = request.POST.get('value')
    client.save()
    messages.success(request, "Successfully updated client notes")
    return render(request, "client_detail.html")


def update_p_notes(request):
    id = request.POST.get('pk')
    preg = get_object_or_404(Pregnancy, pk=id)
    preg.notes = request.POST.get('value')
    preg.save()
    return render(request, "client_detail.html")


def update_due_date(request):
    id = request.POST.get('pk')
    preg = get_object_or_404(Pregnancy, pk=id)
    preg.due_date = request.POST.get('value')
    preg.save()
    return render(request, "client_detail.html")


def update_dob(request):
    id = request.POST.get('pk')
    client = get_object_or_404(Client, pk=id)
    client.dob = request.POST.get('value')
    client.save()
    return render(request, "client_detail.html")


def update_height(request):
    id = request.POST.get('pk')
    client = get_object_or_404(Client, pk=id)
    client.height = request.POST.get('value')
    client.save()
    return render(request, "client_detail.html")


def update_weight(request):
    id = request.POST.get('pk')
    client = get_object_or_404(Client, pk=id)
    client.weight = request.POST.get('value')
    client.save()
    return render(request, "client_detail.html")


def update_bmi(request):
    id = request.POST.get('pk')
    client = get_object_or_404(Client, pk=id)
    client.bmi = request.POST.get('value')
    client.save()
    return render(request, "client_detail.html")


def update_bt(request):
    id = request.POST.get('pk')
    client = get_object_or_404(Client, pk=id)
    client.blood_type = request.POST.get('value')
    client.save()
    return render(request, "client_detail.html")


def update_haemo(request):
    id = request.POST.get('pk')
    client = get_object_or_404(Client, pk=id)
    client.haemoglobin = request.POST.get('value')
    client.save()
    return render(request, "client_detail.html")


def update_sero(request):
    id = request.POST.get('pk')
    client = get_object_or_404(Client, pk=id)
    client.serology = request.POST.get('value')
    client.save()
    return render(request, "client_detail.html")


def update_gp(request):
    id = request.POST.get('pk')
    client = get_object_or_404(Client, pk=id)
    client.gp = request.POST.get('value')
    client.save()
    return render(request, "client_detail.html")


def update_gp_tel(request):
    id = request.POST.get('pk')
    client = get_object_or_404(Client, pk=id)
    client.gp_tel = request.POST.get('value')
    client.save()
    return render(request, "client_detail.html")


def update_hosp(request):
    id = request.POST.get('pk')
    client = get_object_or_404(Client, pk=id)
    client.hospital = request.POST.get('value')
    client.save()
    return render(request, "client_detail.html")


def update_hosp_num(request):
    id = request.POST.get('pk')
    client = get_object_or_404(Client, pk=id)
    client.hospital_num = request.POST.get('value')
    client.save()
    return render(request, "client_detail.html")


def update_para(request):
    id = request.POST.get('pk')
    client = get_object_or_404(Client, pk=id)
    client.parity = request.POST.get('value')
    client.save()
    return render(request, "client_detail.html")


def update_prev_pregs(request):
    id = request.POST.get('pk')
    client = get_object_or_404(Client, pk=id)
    client.prev_pregs = request.POST.get('value')
    client.save()
    return render(request, "client_detail.html")


def update_wcc(request):
    id = request.POST.get('pk')
    preg = get_object_or_404(Pregnancy, pk=id)
    preg.week_care_commences = request.POST.get('value')
    preg.save()
    return render(request, "client_detail.html")


def update_p_site(request):
    id = request.POST.get('pk')
    preg = get_object_or_404(Pregnancy, pk=id)
    preg.placental_site = request.POST.get('value')
    preg.save()
    return render(request, "client_detail.html")


def update_cons(request):
    id = request.POST.get('pk')
    preg = get_object_or_404(Pregnancy, pk=id)
    preg.consultant_clinic = request.POST.get('value')
    preg.save()
    return render(request, "client_detail.html")


def update_phn(request):
    id = request.POST.get('pk')
    preg = get_object_or_404(Pregnancy, pk=id)
    preg.public_health_nurse = request.POST.get('value')
    preg.save()
    return render(request, "client_detail.html")


def get_oauth_flow_object(request):
    client_id = settings.GOOGLE_CLIENT_ID
    client_secret = settings.GOOGLE_CLIENT_SECRET
    scope = settings.GOOGLE_OAUTH2_SCOPE

    redirect_url = request.build_absolute_uri(reverse('oauth_complete'))

    return OAuth2WebServerFlow(client_id=client_id,
                               client_secret=client_secret,
                               scope=scope,
                               redirect_uri=redirect_url)


def oauth_start(request):
    flow = get_oauth_flow_object(request)
    auth_uri = flow.step1_get_authorize_url()
    return redirect(auth_uri)


def oauth_complete(request):
    flow = get_oauth_flow_object(request)
    auth_code = request.GET.get('code')
    credentials = flow.step2_exchange(auth_code)

    auth_token = str(credentials.access_token)

    redirect_url = request.build_absolute_uri(reverse('index'))
    response = redirect(redirect_url)
    response.set_cookie('credentials', credentials.to_json())
    messages.success(request, "Application is authorised to write Google Calendar entries!")
    return response
