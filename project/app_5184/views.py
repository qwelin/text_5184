import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web51842.settings")
django.setup()
from django.shortcuts import render
from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from app_5184.models import Text
from app.s51842 import search


class UserForm(forms.Form):
    user_id = forms.CharField(label='准考证号码：',max_length=12,min_length=12)
    user_name = forms.CharField(label='姓名：',max_length=8)

def register(request):

    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            req_text_id = uf.cleaned_data['user_id']#获取学生提交自考证号
            req_text_name = uf.cleaned_data['user_name']
            #print(req_text_id,req_text_name)
            y = Text.objects.filter(zx_id=req_text_id)
            if len(y) == 0:
                if req_text_id.isdigit():
                    b = search(req_text_id)
                    if len(b) != 0 :
                        if req_text_name == b[0]['姓名']:
                            ret = b
                            http2 = []
                            for i in ret:
                                print(i)
                                text = Text()
                                text.zx_id = i['准考证号']
                                text.zk_name = i['姓名']
                                text.dat = i['考试时间']
                                text.subject = i['科目名称']
                                text.subject_id = i['科目代码']
                                text.scort = i['考试成绩']
                                text.save()
                                l = '准考证号: ' + text.zx_id + " - "+'考生姓名: ' + text.zk_name +" - "+ '考试时间 :' + text.dat +" - "+ '考试科目 :'+text.subject +" - "+'科目代码 :'+text.subject_id +" - "+ '考试成绩 :'+text.scort +'<br>'
                                http2.append(l)
                            # 返回注册成功页面
                            print(ret)

                            return HttpResponse(http2)
                        else:
                            return HttpResponse(u'准考证号码和姓名不对应')
                    else:
                        return HttpResponse(u'系统繁忙,请重新输入')
                else:
                    return HttpResponse(u'请正确输入12位准考证号码')
            else:
                all_data = Text.objects.filter(zx_id=req_text_id)
                if req_text_name == all_data[0].zk_name:
                    html =[]
                    for i in all_data:
                        g ='准考证号: ' + i.zx_id + " - "+'考生姓名: ' + i.zk_name +" - "+ '考试时间 :' + i.dat +" - "+ '考试科目 :'+i.subject +" - "+'科目代码 :'+i.subject_id +" - "+ '考试成绩 :'+i.scort +'<br>'
                        html.append(g)
                    return HttpResponse(html)
                else:
                    return HttpResponse(u'准考证号码和姓名不对应')
    else:
        uf = UserForm()
    return render_to_response('register.html', {'uf':uf})