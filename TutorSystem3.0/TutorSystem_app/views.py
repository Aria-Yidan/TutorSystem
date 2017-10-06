# -*- coding:UTF-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User

from TutorSystem_app.models import Teacher, Student, Tutor_information, Student_information, Judge, Precontract


HOMEPAGE_URL = "http://victorydets.sinaapp.com/"

def TutorSystem_begin(request):
    Username = request.user.username
    user_type = False
    try:
        Teacher.objects.get(Username = request.user)
        user_type = True
    except:
        user_type = False
    TutorIF_list = Tutor_information.objects.all()
    G_math = list(Tutor_information.objects.filter(Grade__contains="高 一",Subject__contains="数 学") |Tutor_information.objects.filter(Grade__contains="高 二",Subject__contains="数 学") |Tutor_information.objects.filter(Grade__contains="高 三",Subject__contains="数 学"))
    G_chinese = list(Tutor_information.objects.filter(Grade__contains="高 一",Subject__contains="语 文") |Tutor_information.objects.filter(Grade__contains="高 二",Subject__contains="语 文") |Tutor_information.objects.filter(Grade__contains="高 三",Subject__contains="语 文"))
    G_english = list(Tutor_information.objects.filter(Grade__contains="高 一",Subject__contains="英 语") |Tutor_information.objects.filter(Grade__contains="高 二",Subject__contains="英 语") |Tutor_information.objects.filter(Grade__contains="高 三",Subject__contains="英 语"))
    G_chemistry = list(Tutor_information.objects.filter(Grade__contains="高 一",Subject__contains="化 学") |Tutor_information.objects.filter(Grade__contains="高 二",Subject__contains="化 学") |Tutor_information.objects.filter(Grade__contains="高 三",Subject__contains="化 学"))
    G_physics = list(Tutor_information.objects.filter(Grade__contains="高 一",Subject__contains="物 理") |Tutor_information.objects.filter(Grade__contains="高 二",Subject__contains="物 理") |Tutor_information.objects.filter(Grade__contains="高 三",Subject__contains="物 理"))
    G_biology = list(Tutor_information.objects.filter(Grade__contains="高 一",Subject__contains="生 物") |Tutor_information.objects.filter(Grade__contains="高 二",Subject__contains="生 物") |Tutor_information.objects.filter(Grade__contains="高 三",Subject__contains="生 物"))
    C_math = list(Tutor_information.objects.filter(Grade__contains="初 一",Subject__contains="数 学") |Tutor_information.objects.filter(Grade__contains="初 二",Subject__contains="数 学") |Tutor_information.objects.filter(Grade__contains="初 三",Subject__contains="数 学"))
    C_chinese = list(Tutor_information.objects.filter(Grade__contains="初 一",Subject__contains="语 文") |Tutor_information.objects.filter(Grade__contains="初 二",Subject__contains="语 文") |Tutor_information.objects.filter(Grade__contains="初 三",Subject__contains="语 文"))
    C_english = list(Tutor_information.objects.filter(Grade__contains="初 一",Subject__contains="英 语") |Tutor_information.objects.filter(Grade__contains="初 二",Subject__contains="英 语") |Tutor_information.objects.filter(Grade__contains="初 三",Subject__contains="英 语"))
    C_chemistry = list(Tutor_information.objects.filter(Grade__contains="初 一",Subject__contains="化 学") |Tutor_information.objects.filter(Grade__contains="初 二",Subject__contains="化 学") |Tutor_information.objects.filter(Grade__contains="初 三",Subject__contains="化 学"))
    C_physics = list(Tutor_information.objects.filter(Grade__contains="初 一",Subject__contains="物 理") |Tutor_information.objects.filter(Grade__contains="初 二",Subject__contains="物 理") |Tutor_information.objects.filter(Grade__contains="初 三",Subject__contains="物 理"))
    C_biology = list(Tutor_information.objects.filter(Grade__contains="初 一",Subject__contains="生 物") |Tutor_information.objects.filter(Grade__contains="初 二",Subject__contains="生 物") |Tutor_information.objects.filter(Grade__contains="初 三",Subject__contains="生 物")) 
    
    G_math = Choose_for_homepage(G_math)
    G_chinese = Choose_for_homepage(G_chinese)
    G_english = Choose_for_homepage(G_english)
    G_chemistry = Choose_for_homepage(G_chemistry)
    G_physics = Choose_for_homepage(G_physics)
    G_biology = Choose_for_homepage(G_biology)
    C_math = Choose_for_homepage(C_math)
    C_chinese = Choose_for_homepage(C_chinese)
    C_english = Choose_for_homepage(C_english)
    C_chemistry = Choose_for_homepage(C_chemistry)
    C_physics = Choose_for_homepage(C_physics)
    C_biology = Choose_for_homepage(C_biology)
    
    return render_to_response('TutorSystem_begin.html',locals())

def TutorSystem_search(request):
    global Dic_week,Dic_time_quantum
    Username = request.user.username
    user_type = False
    try:
        Teacher.objects.get(Username = request.user)
        user_type = True
    except:
        user_type = False
    error = []
    Teacher_find = None
    Tutor_IF_list = []
    My_search = None
    if request.POST:
        post = request.POST
        if post["Day"] == "ALL":
            if post["Day_time"] == "ALL":
                My_search = post["Grade"] + ">>" + post["Subject"] + ">>" + u"全 部" + ">>" + u"全 部"
            else:
                My_search = post["Grade"] + ">>" + post["Subject"] + ">>" + u"全 部" + ">>" + Dic_time_quantum[int(post["Day_time"])]
        else:
            if post["Day_time"] == "ALL":
                My_search = post["Grade"] + ">>" + post["Subject"] + ">>" + Dic_week[int(post["Day"])] + ">>" + u"全 部"
            else:
                My_search = post["Grade"] + ">>" + post["Subject"] + ">>" + Dic_week[int(post["Day"])] + ">>" + Dic_time_quantum[int(post["Day_time"])]
        if post["Grade"] == "ALL":
            if post["Subject"] == "ALL":
                Tutor_IF_list = Tutor_information.objects.all()
            else:
                Tutor_IF_list = Tutor_information.objects.filter(Subject__contains=post["Subject"])
        else:
            if post["Subject"] == "ALL":
                Tutor_IF_list = Tutor_information.objects.filter(Grade__contains=post["Grade"])
            else:
                Tutor_IF_list = Tutor_information.objects.filter(Subject__contains=post["Subject"],Grade__contains=post["Grade"])
        Tutor_IF_list = list(Tutor_IF_list) #change QuerySet into List
        if Tutor_IF_list:
            del_IF = []
            if post["Day"] == "ALL":
                if post["Day_time"] != "ALL":
                    for IF in Tutor_IF_list:
                        if IF.Time[(int(post["Day_time"]))*7:(int(post["Day_time"]))*7+7] == "NNNNNNN":
                            del_IF.append(IF)
            else:
                if post["Day_time"] == "ALL":
                    for IF in Tutor_IF_list:
                        if (IF.Time[int(post["Day"])] == "N") and (IF.Time[int(post["Day"])+7] == "N") and (IF.Time[int(post["Day"])+14] == "N"):
                            del_IF.append(IF)
                else:
                    for IF in Tutor_IF_list:
                        if IF.Time[int(post["Day"]) +(int(post["Day_time"]))*7] == "N":
                            del_IF.append(IF)
            for IF in del_IF:
                Tutor_IF_list.remove(IF)
        Teacher_find = True
    return render_to_response('TutorSystem_search.html',locals())

def TutorSystem_reg(request):
    error = []
    reg_success = False
    if request.POST:
        post = request.POST
        #--Error check--#
        username = post['Username']
        if username == '':
            error.append("请输入用户名")
            return render_to_response('TutorSystem_registration.html',locals())
        if User.objects.filter(username = post['Username']):
            error.append("用户名已存在")
            return render_to_response('TutorSystem_registration.html',locals())
        password = post['Password']
        if len(password) < 4:
            error.append("密码格式不正确")
            return render_to_response('TutorSystem_registration.html',locals())
        if len(post["Phone"]) != 11:
            error.append("电话号码位数不正确")
            return render_to_response('TutorSystem_registration.html',locals())
        for i in post["Phone"]:
            if ord(i) < 48 or ord(i) > 57:
                error.append("电话号码包含非法字符")
                return render_to_response('TutorSystem_registration.html',locals())
        #--Add user--#
        repassword = post['rePassword']
        if repassword == password:
             if post['UserType'] == "stu" :
                user = User.objects.create_user(username=username,password=password)
                user.save()
                new_student = Student.objects.create(
                    StudentID = "default",
                    Username = user,
                    Grade = '',
                    Sex = True,
                    Email = '',
                    Phone = post["Phone"]
                )
                new_student.StudentID = "Stu" + str(new_student.id)
                new_student.save()
                reg_success = True
             elif post['UserType'] == "tut" :
                user = User.objects.create_user(username=username,password=password)
                user.save()
                new_teacher = Teacher.objects.create(
                    TeacherID = "default",
                    Username = user,
                    Age = '',
                    Sex = True,
                    Email = '',
                    Phone = post["Phone"],
                    School = '',
                    Introduction = ''
                )
                new_teacher.TeacherID = "Tut" + str(new_teacher.id)
                new_teacher.save()
                reg_success = True
             else:
                error.append("请选择用户身份")
        else:
            error.append("确认密码与密码不一致")
    return render_to_response('TutorSystem_registration.html',locals())

def TutorSystem_login(request):
    error = []
    if request.POST:
        post = request.POST
        username = post['Username']
        try:
            User.objects.get(username = post['Username'])
            password = post['Password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(HOMEPAGE_URL)
            else:
               error.append("密码错误")
        except:
            error.append("用户不存在")
            return render_to_response('TutorSystem_login.html',locals())
    return render_to_response('TutorSystem_login.html',locals())

def TutorSystem_logout(request):
    auth.logout(request)
    return HttpResponseRedirect(HOMEPAGE_URL)

def person_center(request): 
    if request.user.username :
        username = request.user.username
        user = User.objects.get(username = username)
        
        if Teacher.objects.filter(Username = user):
            return HttpResponseRedirect(HOMEPAGE_URL+"person_center/tutor")
        else:
            return HttpResponseRedirect(HOMEPAGE_URL+"person_center/student")

    return HttpResponseRedirect(HOMEPAGE_URL)


def person_center_tutor(request):
    Username = request.user.username
    try:
        Teacher.objects.get(Username = request.user)
        user_type = True
    except:
        user_type = False
    tutor = None
    inf_flag = False
    newpre_flag = False
    newpre_number = 0
    if request.user.username and user_type:
        tutor = Teacher.objects.get(Username = request.user)
        tut_inf_list = Tutor_information.objects.filter(TeacherID = tutor)
        if tut_inf_list:
            inf_flag = True
            new_pre = Precontract.objects.filter(TeacherID = tutor,State="Apply_by_student")
            if new_pre :
                newpre_flag = True
                newpre_number = len(new_pre)
            else:
            	newpre_flag = False
        else:
            inf_flag = False
        
        return render_to_response('person_center_tutor.html',locals())
    return HttpResponseRedirect(HOMEPAGE_URL)


def person_center_student(request):
    Username = request.user.username
    try:
        Teacher.objects.get(Username = request.user)
        user_type = True
    except:
        user_type = False
    inf_flag = False
    successpre = None
    successpre_flag = False
    successpre_number = 0
    if request.user.username and (not user_type):
        Stu = Student.objects.get(Username = request.user)
        stu_inf = Student_information.objects.filter(StudentID = Stu)
        if stu_inf :
            inf_flag = True
            successpre = Precontract.objects.filter(StudentID = Stu.StudentID,State="Pass_by_teacher")
            if successpre:
            	successpre_flag = True
                successpre_number = len(successpre)
                
        else:
            inf_flag = False
        return render_to_response('person_center_stu.html',locals())
    return HttpResponseRedirect(HOMEPAGE_URL)
