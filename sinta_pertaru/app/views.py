from datetime import time, datetime
from django.db.models import Max
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.decorators.cache import never_cache
from . import models
from . import services
import datetime

# Create your views here.

# Templates path
index_tmpl_path = 'index.html'
dshb_tmpl_path = 'dashboard.html'
login_tmpl_path = 'auth-login.html'
signup_tmpl_path = 'auth-sign-up.html'
ls_tmpl_path = 'land-suitability.html'
gs_tmpl_path = 'gis-service.html'
gb_tmpl_path = 'guest-book.html'
up_tmpl_path = 'user-profile-edit.html'
info_tmpl_path = 'pages-info.html'
help_tmpl_path = 'pages-help.html'
err404_tmpl_path = 'pages-error-404.html'

# Dummy exists user id / employee id
dummy_uid = ['1', '2', '3', '4', '5',
             '6', '7', '8', '9', '10']


@never_cache
def view_index(request):  # Welcome to Sinta Pertaru Greeting
    template = loader.get_template(index_tmpl_path)
    context = {'request': request}

    return HttpResponse(template.render(context))


@never_cache
def view_dashboard(request, login=0):
    template = loader.get_template(dshb_tmpl_path)
    context = {'request': request}

    if login == 1:
        context.update({'rst': '1',
                        'rmg': f"Selamat datang, {request.session['user_name']}"})
    try:
        if not services.GeneralServices.service_check_login(request):
            return HttpResponseRedirect(reverse('view_login', kwargs={'login': 0}))
    except Exception as e:
        print(e)
        return HttpResponseRedirect(reverse('view_login'))

    return HttpResponse(template.render(context))


@never_cache
def view_login(request, login=1, signup=0):  # User Login Page
    template = loader.get_template(login_tmpl_path)
    context = {'request': request, }

    # Add success message if signup success
    if signup == 1:
        context.update({'rst': 1,
                        'rmg': 'Selamat, akun anda berhasil dibuat!'})

    # Add error message if not login
    if login == 0:
        context.update({'rst': '0',
                        'rmg': 'Anda belum masuk, silahkan masuk terlebih dahulu'})

    if request.method == "POST":
        rp = request.POST

        if rp['form'] == 'user_login':
            if services.UserFormServices.validateUser(request):
                # Get id for matched user
                user_login = models.User.objects.get(user_name=request.POST['user_name'],
                                                     user_password=request.POST['user_password'])
                # Set session data
                services.SessionServices.setLoginSession(request,
                                                         user_id=user_login.user_id,
                                                         user_name=user_login.user_name)

                return HttpResponseRedirect(reverse('view_dashboard', kwargs={'login': 1}))

            else:
                context.update({'rst': '0',
                                'rmg': 'Gagal masuk, nama pengguna dan kata sandi tidak cocok!'})

    return HttpResponse(template.render(context))


@never_cache
def view_signup(request):  # New User Signup Page
    template = loader.get_template(signup_tmpl_path)
    context = {'request': request, }

    if request.method == "POST":
        rp = request.POST

        if rp['form'] == 'userSignUp':
            # If employee id exists in Employee table (T)
            if models.Employee.objects.filter(employee_id=rp['user_fk_employee_id']).count():
                print('SIGNUP - nip terdaftar')

                # If employee id exists in User table as fk (F)
                if models.User.objects.filter(user_fk_employee_id=rp['user_fk_employee_id']).count():
                    print('SIGNUP - nip memiliki akun')
                    context.update({'rst': '0',
                                    'rmg': 'Gagal, nomor pegawai sudah memiliki akun!'})

                else:
                    # If current user name not exists in User table (T)
                    if models.User.objects.filter(user_name=rp['user_name']).count() == 0:
                        print('SIGNUP - username tersedia')

                        request.POST._mutable = True
                        request.POST['user_id'] = \
                            models.User.objects.all().aggregate(Max('user_id'))['user_id__max'] + 1 if \
                                models.User.objects.count() > 0 else 1  # Select max id
                        request.POST['user_joined_date'] = datetime.datetime.now()
                        request.POST._mutable = False

                        if services.UserFormServices.createUser(request):
                            return HttpResponseRedirect(reverse('view_login', kwargs={'signup': 1}))

                    else:
                        print('SIGNUP - username tidak tersedia')
                        context.update({'rst': '0',
                                        'rmg': 'Gagal, nama pengguna sudah ada!'})
            else:
                print('SIGNUP - nip tidak terdaftar')
                context.update({'rst': '0',
                                'rmg': 'Gagal, nomor pegawai tidak terdaftar!'})

    return HttpResponse(template.render(context))


@never_cache
def view_gis_service(request):
    template = loader.get_template(gs_tmpl_path)
    context = {'request': request}

    if not services.GeneralServices.service_check_login(request):
        return HttpResponseRedirect(reverse('view_login', kwargs={'login': 0}))

    if request.method == "POST":
        pass

    return HttpResponse(template.render(context))


@never_cache
def view_ls(request):
    template = loader.get_template(ls_tmpl_path)
    context = {'request': request,
               'page_title': 'Sinta Pertaru - Analisis Kesesuaian Lahan'}

    if not services.GeneralServices.service_check_login(request):
        return HttpResponseRedirect(reverse('view_login', kwargs={'login': 0}))

    if request.method == "POST":
        if 'land_data' in request.POST:
            print('LS-table data process')
            add_from_table = services.LSDataFormService.lsDataAddFromTable(request, request.session['user_id'])

            if add_from_table:
                context.update({'rst': 1,
                                'rmg': 'Data berhasil diubah'})
            else:
                context.update({'rst': 0,
                                'rmg': 'Data gagal diubah'})

        elif 'csv_import' in request.POST:
            print('LS-csv data import process')
            add_from_csv = services.LSDataFormService.lsDataAddFromCsvImport(request, request.session['user_id'])

            if add_from_csv:
                context.update({'rst': 1,
                                'rmg': 'Impor data csv berhasil'})
            else:
                context.update({'rst': 0,
                                'rmg': 'Import data csv gagal'})

        if 'process' in request.POST:
            if request.POST['process'] == '1':
                # Data process here!
                print('LS-classifying test data')

                test = services.GeneralServices.lsProcessData(request, request.session['user_id'])
                if test:
                    context.update({'rst': 1,
                                    'rmg': 'Proses klasifikasi berhasil!'})
                else:
                    context.update({'rst': 0,
                                    'rmg': 'Proses klasifikasi gagal!'})

    land_data = models.LandData.objects.all().filter(land_data_fk_user_id=request.session['user_id'])
    train_data = land_data.filter(land_data_type='train')
    test_data = land_data.filter(land_data_type='test')
    train_ulb_data = train_data.filter(land_data_suitability__exact='')
    train_lb_data = train_data.exclude(land_data_suitability__exact='')
    test_ulb_data = test_data.filter(land_data_suitability__exact='')
    test_lb_data = test_data.exclude(land_data_suitability__exact='')

    context.update({
        'train_data': train_data,
        'train_data_total': train_data.count(),
        'test_data': test_data,
        'test_data_total': test_data.count(),
        'train_unlabeled_data': train_ulb_data.count(),
        'train_labeled_data': train_lb_data.count(),
        'test_unlabeled_data': test_ulb_data.count(),
        'test_labeled_data': test_lb_data.count()
    })
    return HttpResponse(template.render(context))


@never_cache
def view_export_csv(request, data_type=''):
    if not services.GeneralServices.service_check_login(request):
        return HttpResponseRedirect(reverse('view_login', kwargs={'login': 0}))

    csv_response = services.GeneralServices.lsExportCsv(request, request.session['user_id'], data_type)

    if csv_response:
        return csv_response
    else:
        return False


@never_cache
def view_guest_book(request):
    template = loader.get_template(gb_tmpl_path)
    context = {'request': request,
               'page_title': 'Sinta Pertaru - Buku Tamu'}

    if not services.GeneralServices.service_check_login(request):
        return HttpResponseRedirect(reverse('view_login', kwargs={'login': 0}))

    if request.method == "POST":
        rp = request.POST

        # Action for FORM Add Guest
        if rp['form'] == 'add_guest':
            if services.GuestBookFormService.createGuest(request, request.session['user_id']):
                context.update({'rst': '1',
                                'rmg': 'Tamu berhasil ditambahkan'})
            else:
                context.update({'rst': '0',
                                'rmg': 'Tamu gagal ditambahkan'})

    guest_list = models.GuestBook.objects.all()
    today_guest_list = models.GuestBook.objects.filter(guest_arrival_date__day=datetime.datetime.today().day)

    context.update({'guest_list': guest_list,
                    'guest_list_r': guest_list.reverse(),
                    'guest_list_total': guest_list.count(),
                    'today_guest_list': today_guest_list,
                    'today_guest_list_total': today_guest_list.count()})

    return HttpResponse(template.render(context))


@never_cache
def view_user_profile(request):
    template = loader.get_template(up_tmpl_path)
    context = {'request': request,
               'page_title': 'Sinta Pertaru - Profilku',
               'request_stat': 'none'}

    if not services.GeneralServices.service_check_login(request):
        return HttpResponseRedirect(reverse('view_login', kwargs={'login': 0}))

    if request.method == "POST":
        rp = request.POST

        # Change request post date to required form
        rp._mutable = True
        rp['user_joined_date'] = models.User.objects.get(user_id=request.session['user_id']).user_joined_date
        rp._mutable = False

        # Action for FORM Edit Profile
        if rp['form'] == 'edit_profile':
            if services.UserFormServices.updateUser(request, request.session['user_id']):
                services.SessionServices.setLoginSession(request,
                                                         request.session['user_id'],
                                                         rp['user_name'])
                context.update({'rst': '1',
                                'rmg': 'Profil Anda berhasil diubah!'})
            else:
                context.update({'rst': '0',
                                'rmg': 'Profil Anda gagal diubah!'})

        # Action for FORM Change Password
        if rp['form'] == 'change_password':
            if models.User.objects.filter(user_id=request.session['user_id'],
                                          user_name=request.session['user_name'],
                                          user_password=rp['user_password']).exists() and \
                    rp['user_password_new'] == rp['user_password_new_confirm']:
                models.User.objects.filter(user_id=request.session['user_id']). \
                    update(user_password=rp['user_password_new'])
                # services.UserFormServices.updateUser(request, request.session['user_id'])
                context.update({'rst': '1',
                                'rmg': 'Kata Sandi berhasil diubah'})
            else:
                context.update({'rst': '0',
                                'rmg': 'Kata sandi Anda gagal diubah'})

    context.update({'user_data': models.User.objects.get(user_id=request.session['user_id'])})

    return HttpResponse(template.render(context))


@never_cache
def view_help(request):
    template = loader.get_template(help_tmpl_path)
    context = {'request': request}

    if not services.GeneralServices.service_check_login(request):
        return HttpResponseRedirect(reverse('view_login', kwargs={'login': 0}))

    if request.method == "POST":
        pass

    return HttpResponse(template.render(context))


@never_cache
def view_info(request):
    template = loader.get_template(info_tmpl_path)
    context = {'request': request}

    if not services.GeneralServices.service_check_login(request):
        return HttpResponseRedirect(reverse('view_login', kwargs={'login': 0}))

    if request.method == "POST":
        pass

    return HttpResponse(template.render(context))


# Exception
@never_cache
def view_err404(request):  # Error 404 - Page Not Found
    template = loader.get_template(err404_tmpl_path)
    context = {'request': request}

    if request.method == "POST":
        pass

    return HttpResponse(template.render(context))
