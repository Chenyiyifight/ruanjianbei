from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from lightgbm.sklearn import LGBMClassifier
from django.views.decorators.csrf import csrf_exempt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np
from sklearn.metrics import f1_score
import pickle
import os
from django.http import JsonResponse
import csv
import json
import pickle
import pandas as pd
from sklearn.metrics import f1_score
# Create your views here.

def depart_list(request):
    return render(request, "depart_list.html")

## view.py

@csrf_exempt
def upload_excel(request):
    print(request.FILES)
    if 'file' not in request.FILES:
        return HttpResponse("No file part")
    file = request.FILES['file']
    if file:
        folder_path = "D:\\folder"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        custom_filename = "custom_name" + ".csv"

        with open(os.path.join(folder_path, custom_filename), 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        return HttpResponse("File uploaded successfully with custom name: " + custom_filename)
    else:
        return HttpResponse("File not found")

# 训练模型，具体不做要求，要求可以自己设置模型放置位置
def train_model(request):
    df = pd.read_csv('d:\\folder\\custom_name.csv', index_col=None)
    features = df.iloc[:, 1:-1]

    numeric_features = features.dtypes[features.dtypes != 'object'].index

    features[numeric_features] = features[numeric_features].apply(
        lambda x: (x - x.mean()) / (x.std())
    )

    features_labels = pd.concat([features, df[['label']]], axis=1)
    train_features = pd.concat([df[['sample_id']], features], axis=1)

    train_label = df[['sample_id', 'label']]

    df = pd.concat([train_features, train_label[['label']]], axis=1)

    X, Y = df.iloc[:, 1:-1], df.iloc[:, -1]

    x_train, x_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.2, random_state=123
    )
    lgb_clf = LGBMClassifier()
    # 在训练集上训练LightGBM模型
    lgb_clf.fit(x_train, y_train)
    #  在训练集和测试集上分别利用训练好的模型进行预测
    lgb_predict = lgb_clf.predict(x_test)
    with open('d:\\folder\\my_model.pkl', 'wb') as f:
        pickle.dump(lgb_clf, f)
    print(f1_score(y_test, lgb_predict, average="macro"))

    # return HttpResponse("模型训练成功")
    f1 = f1_score(y_test, lgb_predict, average="macro")
    return HttpResponse(f"F1 分数为: {f1}")
'''
def predict_data(request):
    with open('d:\\qq文件\\my_model.pkl', 'rb') as f:
        model = pickle.load(f)
    df = pd.read_csv('d:\\qq文件\\custom_name.csv', index_col=None)
    features = df.iloc[:, 1:-1]
    numeric_features = features.dtypes[features.dtypes != 'object'].index

    features[numeric_features] = features[numeric_features].apply(
        lambda x: (x - x.mean()) / (x.std())
    )

    features_labels = pd.concat([features, df[['label']]], axis=1)
    train_features = pd.concat([df[['sample_id']], features], axis=1)

    train_label = df[['sample_id', 'label']]

    df = pd.concat([train_features, train_label[['label']]], axis=1)
    X, Y = df.iloc[:, 1:-1], df.iloc[:, -1]
    model_predict = model.predict(X)
    print(f1_score(Y, model_predict, average="macro"))
    return HttpResponse("预测成功")
'''


def predict_data(request):
    with open('d:\\qq文件\\my_model.pkl', 'rb') as f:
        model = pickle.load(f)
    df = pd.read_csv('d:\\qq文件\\custom_name.csv', index_col=None)
    features = df.iloc[:, 1:-1]
    numeric_features = features.dtypes[features.dtypes != 'object'].index

    features[numeric_features] = features[numeric_features].apply(
        lambda x: (x - x.mean()) / (x.std())
    )

    features_labels = pd.concat([features, df[['label']]], axis=1)
    train_features = pd.concat([df[['sample_id']], features], axis=1)

    train_label = df[['sample_id', 'label']]

    df = pd.concat([train_features, train_label[['label']]], axis=1)
    X, Y = df.iloc[:, 1:-1], df.iloc[:, -1]
    model_predict = model.predict(X)
    f1 = f1_score(Y, model_predict, average="macro")
    confidence = model.predict_proba(X)  # 获取预测概率

    # 构建返回的数据字典
    response_data = {
        'f1_score': f1,
        'confidence': confidence.tolist()  # 将numpy数组转换为列表
    }

    # 将数据转换为JSON格式
    json_response = json.dumps(response_data)

    # 返回JSON响应
    return HttpResponse(json_response, content_type='application/json')






