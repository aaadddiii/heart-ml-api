from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import pickle
import numpy as np
import pandas as pd

# 1. #3 (age)
# 2. #4 (sex)
# 3. #9 (cp)
# 4. #10 (trestbps)
# 5. #12 (chol)
# 6. #16 (fbs)
# 7. #19 (restecg)
# 8. #32 (thalach)
# 9. #38 (exang)
# 10. #40 (oldpeak)
# 11. #41 (slope)
# 12. #44 (ca)
# # 13. #51 (thal)
# age: age in years
# 4 sex: sex (1 = male; 0 = female)
#  cp: chest pain type
# -- Value 1: typical angina
# -- Value 2: atypical angina
# -- Value 3: non-anginal pain
# -- Value 4: asymptomatic
#  trestbps: resting blood pressure (in mm Hg on admission to the hospital)
# 11 htn
# 12 chol: serum cholestoral in mg/dl
# fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
#  restecg: resting electrocardiographic results
# -- Value 0: normal
# -- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
# -- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
# 32 thalach: maximum heart rate achieved
#  exang: exercise induced angina (1 = yes; 0 = no)
#  oldpeak = ST depression induced by exercise relative to rest
#   slope: the slope of the peak exercise ST segment
# -- Value 1: upsloping
# -- Value 2: flat
# -- Value 3: downsloping
#  ca: number of major vessels (0-3) colored by flourosopy
#  thal: 3 = normal; 6 = fixed defect; 7 = reversable defect
# example : [57,1,3,170,288,0,0,159,0,0.2,1,0,3]
@api_view(["POST"])
def IdealWeight(heartdata):
    try:
        data = json.load(heartdata)
        model = pickle.load(open("heart/heart_model.pkl","rb"))
        arr = pd.DataFrame([[data['age'],data['sex'],data['cp'],data['trestbps'],data['chol'],data['fbs'],data['restecg'],data['thalach'],data['exang'],data['oldpeak'],data['slope'],data['ca'],data['thal']]])
        mypred = model.predict(arr)[0]
        return Response(mypred)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
        
