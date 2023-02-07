from datetime import time, datetime
from django.db.models import Max
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler

import csv
import multiprocessing
import numpy as np
import pandas as pd
import threading

from . import models
from . import forms


# Create your app services here

class GeneralServices:
    @staticmethod
    def service_check_login(request):
        try:
            user_match = models.User.objects.filter(user_id=request.session['user_id'],
                                                    user_name=request.session['user_name']).first()
            if request.session['login'] != '0' and user_match is not None:
                return True

        except Exception as e:
            return False

    @staticmethod
    def service_logout(request):  # Logout service procedure, View extended service
        SessionServices.releaseSession(request)
        return HttpResponseRedirect(reverse('view_login'))

    @staticmethod
    def lsProcessData(request, user_fk):
        # Data process here!
        # All key noise will be normalized here
        def keyNormalizer(key: str):
            # Normalize method: whitespace removal, lowercasing key
            return key.replace(" ", "").lower()

        # Feature Scaler with hash map
        def rainfallScaler(key):
            rf_map = {'<1.000': .16,
                      '1.000-2.000': .32,
                      '2.000-2.500': .48,
                      '2.500-3.000': .64,
                      '3.000-3.500': .80,
                      '>3.500': .96,
                      }
            try:
                return rf_map[keyNormalizer(key)]
            except Exception as e:
                print(e)
            return key

        def slopesScaler(key):
            sl_map = {'(0-3)%': .16,
                      '(3-8)%': .32,
                      '(8-15)%': .48,
                      '(15-25)%': .64,
                      '(25-45)%': .80,
                      '>45%': .96,
                      }
            try:
                return sl_map[keyNormalizer(key)]
            except Exception as e:
                print(e)
            return key

        def soilTypeScaler(key):
            st_map = {'andiceutropepts': 0.04,
                      'pemukiman': 0.08,
                      'typiceutropepts': 0.12,
                      'typictropaquepts': 0.16,
                      'typictroporthents': 0.2,
                      'typicustorthents': 0.24,
                      'andicdystropepts': 0.28,
                      'andichapludolls': 0.32,
                      'typicfragiaquents': 0.36,
                      'typichapluderts': 0.4,
                      'typichapludands': 0.44,
                      'typicfluvaquents': 0.48,
                      'typictropofluvents': 0.52,
                      'lithicustorthents': 0.56,
                      'typicendoaquents': 0.6,
                      'lithicustropepts': 0.64,
                      'singkapanbatuan': 0.68,
                      'typicustropepts': 0.72,
                      'kawasanmiliter': 0.76,
                      'vertictropaquepts': 0.8,
                      'typichaplusterts': 0.84,
                      'lahankritis': 0.88,
                      'fluvaquenticeutropepts': 0.92,
                      'aerictropaquepts': 0.96,
                      'verticeutropepts': 1,
                      }
            try:
                return st_map[keyNormalizer(key)]
            except Exception as e:
                print(e)
            return key

        features, features_model = ['rainfall', 'slopes', 'soil_type'], ['mm_0', 'mm_1']
        label = ['suitability']

        try:
            # models.User.objects.get(user_id=user_fk)
            # Saving fetched Queryset to pandas DataFrame
            print('LS-classifying process')
            LSDataFormService.lsDataAddFromTable(request, user_fk)

            df_train = pd.DataFrame.from_records(
                models.LandData.objects.all().filter(land_data_fk_user_id=user_fk,
                                                     land_data_type='train').values_list('land_data_id',
                                                                                         'land_data_object_id',
                                                                                         'land_data_rainfall',
                                                                                         'land_data_slopes',
                                                                                         'land_data_soil_type',
                                                                                         'land_data_suitability')
            )
            df_test = pd.DataFrame.from_records(
                models.LandData.objects.all().filter(land_data_fk_user_id=request.session['user_id'],
                                                     land_data_type='test').values_list('land_data_id',
                                                                                        'land_data_object_id',
                                                                                        'land_data_rainfall',
                                                                                        'land_data_slopes',
                                                                                        'land_data_soil_type',
                                                                                        'land_data_suitability')
            )

            # Replacing dfs header
            for _df in [df_train, df_test]:
                _df.columns = ['id', 'object_id', 'rainfall', 'slopes', 'soil_type', 'suitability']

            # Feature Scaling (Convert cat. val to num. val)
            for _df in [df_train, df_test]:  # !! ERROR
                for i, row in _df.iterrows():
                    _df.at[i, 'rainfall'] = rainfallScaler(_df.iloc[i]['rainfall'])
                    _df.at[i, 'slopes'] = slopesScaler(_df.iloc[i]['slopes'])
                    _df.at[i, 'soil_type'] = soilTypeScaler(_df.iloc[i]['soil_type'])

            # Dimensionality reduction with SVD
            def svd(_df):
                tsvd = TruncatedSVD(n_components=2).fit_transform(_df[['rainfall', 'slopes', 'soil_type']])
                _df = _df.join(pd.DataFrame(tsvd))

                return _df

            # Scaling (0 - 1)(positive) with MinMax Scaler
            def minMax(_df):
                scaler = MinMaxScaler()
                scaler.fit(_df[[0, 1]])
                scaler_df = pd.DataFrame(scaler.transform(_df[[0, 1]]))
                scaler_df.rename(columns={0: 'mm_0', 1: 'mm_1'}, inplace=True)
                _df = _df.join(scaler_df)

                return _df

            df_train, df_test = minMax(svd(df_train)), minMax(svd(df_test))

            # #####
            # pd.set_option('display.max_columns', None)
            # for oid, _0, _1 in zip(
            #         df_train['object_id'],
            #         df_train[0],
            #         df_train[1]):
            #     print(str(oid) + ',' + str(_0) + ',' + str(_1))
            # ####

            # X & Y Splitting
            x_train, y_train = df_train[features_model], df_train[label]
            x_test, y_test = df_test[features_model], df_test[label]

            # Build NB Model
            model = GaussianNB()
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)

            # Saving / Update predicted test label manually
            for i, row in df_test.iterrows():
                models.LandData.objects.filter(land_data_id=df_test.iloc[i]['id']). \
                    update(land_data_suitability=y_pred[i])

            return True

        except Exception as e:
            print('process ERROR', e)

        return False

    @staticmethod
    def lsExportCsv(request, user_fk, data_type):
        try:
            f_name = f"ls_{'model' if data_type == 'train' else 'test'}_data-{datetime.today().strftime('%Y%m%d%H%M%S')}.csv"
            response = HttpResponse(content_type='text/csv',
                                    headers={'Content-Disposition': f'attachment; filename="{f_name}"'})
            writer = csv.writer(response)
            writer.writerow(['no', 'object_id', 'curah_hujan', 'lereng', 'jenis_tanah', 'kesesuaian'])

            ls_data = models.LandData.objects.filter(land_data_fk_user_id=user_fk,
                                                     land_data_type=data_type). \
                values_list('land_data_object_id', 'land_data_rainfall', 'land_data_slopes', 'land_data_soil_type',
                            'land_data_suitability')
            for i, lsd in enumerate(ls_data):
                writer.writerow([i, lsd[0], lsd[1], lsd[2], lsd[3], lsd[4].replace('\r', '')])

            return response
        except Exception as e:
            return False


class SessionServices:
    """
        Session variables:
        - User ID (user_id)
        - Login Status (login)
    """

    @staticmethod
    def setUserSession(request, user_id, user_name):
        request.session['user_id'] = user_id
        request.session['user_name'] = user_name

    @staticmethod
    def setLoginSession(request, user_id, user_name):
        SessionServices.setUserSession(request, user_id, user_name)
        request.session['login'] = '1'
        request.session['login_start_time'] = str(datetime.now())
        request.session['login_start_time_hour'] = str(datetime.now().strftime('%H:%M'))
        request.session['login_time'] = str(datetime.now())

    @staticmethod
    def setReqStatusSession(request, status: int, msg=""):
        request.session['request_status'] = str(status)
        request.session['request_status_msg'] = msg

    @staticmethod
    def setRoutineSession(request):
        def updateLoginTime():
            return datetime.now().strftime('%H:%M:%S')

        request.session['login_time'] = updateLoginTime()

    @staticmethod
    def releaseSession(request):
        request.session['login'] = '0'
        request.session['user_id'] = ''
        request.session['user_name'] = ''
        request.session['login_start_time'] = ''
        # del request.session['login']
        # del request.session['user_id']


class UserFormServices(forms.UserForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def createUser(request):
        if request.method == "POST":
            form = forms.UserForm(request.POST)

            if form.is_valid():
                try:
                    form.save()
                    return True
                except Exception as e:
                    print(e)
            else:
                print(form.errors.as_data())
        else:
            form = forms.UserForm()

        return False

    @staticmethod
    def updateUser(request, user_pk):
        if request.method == "POST":
            user = models.User.objects.get(user_id=user_pk)
            form = forms.UserForm(request.POST, instance=user)

            if form.is_valid():
                try:
                    form.save()
                    return True
                except Exception as e:
                    print(e)
            else:
                print(form.errors.as_data())
        else:
            form = forms.UserForm()

        return False

    @staticmethod
    def validateUser(request):
        """
        :param request:
        :return:
        """
        if request.method == "POST":
            login_user_name = request.POST['user_name']
            login_user_password = request.POST['user_password']
            user_match = models.User.objects.filter(user_name=login_user_name,
                                                    user_password=login_user_password).first()
            if user_match is not None:
                return True

        return False


class LSDataFormService(forms.LSDataForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def lsDataAddFromTable(request, user_fk):
        if request.method == "POST":
            try:
                data = request.POST
                form_ids = list()

                for did, oid, rf, sl, st, su, acc in zip(data.getlist('land_data_id'),
                                                         data.getlist('land_data_object_id'),
                                                         data.getlist('land_data_rainfall'),
                                                         data.getlist('land_data_slopes'),
                                                         data.getlist('land_data_soil_type'),
                                                         data.getlist('land_data_suitability'),
                                                         data.getlist('land_data_accuracy')):

                    # If land data id empty, then do data create
                    if not did:
                        print('LS - land data id empty, creating data')

                        # If duplicate object id with same user id not found
                        if models.LandData.objects.filter(land_data_object_id=oid,
                                                          land_data_fk_user_id=user_fk).count() == 0:
                            print('LS - land data obj id not found duplicate, continue process')

                        did = models.LandData.objects.all().aggregate(Max('land_data_id')) \
                                  ['land_data_id__max'] + 1 if models.LandData.objects.count() > 0 else 1
                        models.LandData(land_data_id=did,
                                        land_data_object_id=oid,
                                        land_data_rainfall=rf, land_data_slopes=sl, land_data_soil_type=st,
                                        land_data_suitability=su, land_data_type=data.get('land_data_type'),
                                        land_data_accuracy=float(0) if not acc else float(acc),
                                        land_data_fk_user_id=models.User.objects.get(user_id=user_fk)).save()

                    else:
                        # If land data id found in land data table, then do data update
                        if models.LandData.objects.filter(land_data_id=did).count() > 0:
                            print('LS - land data id not empty, updating data')
                            models.LandData.objects.filter(land_data_id=did). \
                                update(land_data_id=did,
                                       land_data_object_id=oid,
                                       land_data_rainfall=rf, land_data_slopes=sl, land_data_soil_type=st,
                                       land_data_suitability=su, land_data_type=data.get('land_data_type'),
                                       land_data_accuracy=acc,
                                       land_data_fk_user_id=models.User.objects.get(user_id=user_fk))

                    form_ids.append(int(did))

                # Find for difference id to complete delete process
                data_ids = models.LandData.objects.filter(land_data_type=data.get('land_data_type'),
                                                          land_data_fk_user_id=models.User.objects.get(user_id=user_fk))
                model_ids = [row.land_data_id for row in data_ids]
                diff_ids = [item for item in model_ids if item not in form_ids]

                for did in diff_ids:
                    models.LandData.objects.get(land_data_id=did).delete()

                return {'rst': 1}

            except Exception as e:
                return False

    @staticmethod
    def lsDataAddFromCsvImport(request, user_fk):
        if request.method == "POST":
            print(request.method)
            try:
                print(f"LS - upload csv ({request.POST['land_data_type']})")
                csv_file = request.FILES['csv_file']
                with_header = True if request.POST['with_header'] == 'on' else False
                with_number = True if request.POST['with_number'] == 'on' else False
                print(request.POST['with_number'])

                if not csv_file.name.endswith('.csv'):
                    print('File is not csv type')

                if csv_file.multiple_chunks():
                    print('Uploaded file is too big')

                file_data = csv_file.read().decode("utf-8")

                rows = file_data.split("\n")
                # default_header = ['no', 'obj_id', 'rf', 'sl', 'st', 'ls']
                header = rows[0].split(",")

                if len(header) != 6:
                    raise Exception

                if with_header:
                    rows = rows[1:]

                for i, row in enumerate(rows):
                    if i == len(rows) - 1:
                        break

                    fields = row.split(",")

                    if with_number:
                        fields = fields[1:]

                    models.LandData(land_data_id=
                                    models.LandData.objects.all().aggregate(Max('land_data_id')) \
                                        ['land_data_id__max'] + 1 if models.LandData.objects.count() > 0 else 1,
                                    land_data_object_id=fields[0],
                                    land_data_rainfall=fields[1],
                                    land_data_slopes=fields[2],
                                    land_data_soil_type=fields[3],
                                    land_data_suitability=fields[4],
                                    land_data_type=request.POST['land_data_type'],
                                    land_data_accuracy=float(0),
                                    land_data_fk_user_id=models.User.objects.get(user_id=user_fk)).save()

                return {'rst': 1}

            except Exception as e:
                print(e)
                return False


class GuestBookFormService(models.GuestBook):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def createGuest(request, user_fk):
        if request.method == "POST":
            rp = request.POST
            guest_id = models.GuestBook.objects.all().aggregate(Max('guest_id'))[
                           'guest_id__max'] + 1 if models.GuestBook.objects.count() > 0 else 1
            models.GuestBook(guest_id=guest_id,
                             guest_name=rp['guest_name'],
                             guest_type=rp['guest_type'],
                             guest_instance_purpose=rp['guest_instance_purpose'],
                             guest_necessary=rp['guest_necessary'],
                             guest_arrival_date=datetime.now(),
                             guest_fk_user_id=models.User.objects.get(user_id=user_fk)).save()

            return True

        return False
