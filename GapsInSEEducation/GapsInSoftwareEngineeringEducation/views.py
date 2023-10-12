from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Skills, SkillOrderGuess
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def gaps_home(request):
    return render(request, "GISEE/index.html")


def resources(request):
    return render(request, "GISEE/resources.html")


def question1(request):
    return render(request, "GISEE/question1.html")


def question2(request):
    return render(request, "GISEE/question2.html")


def question3(request):
    return render(request, "GISEE/question3.html")


def guessing_question1(request):
    return render(request, "GISEE/guessing_questions1.html")


def guessing_question2(request):
    return render(request, "GISEE/guessing_question2.html")


def guessing_question3(request):
    return render(request, "GISEE/guessing_question3.html")


def guessing_question_submission(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == 'POST':
        guess = request.POST.get('guess')
        number_wrong = request.POST.get('number_wrong')
        question = request.POST.get('question')
        user = User.objects.get(username=request.session.get("username"))
        guess_db = SkillOrderGuess(skill_guess_array=guess, number_wrong=number_wrong, question=question, user=user)
        guess_db.save()
        return JsonResponse({'success': 'success'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid Ajax request.'}, status=400)


def question1_submit(request):
    if request.method == 'POST':
        # process the form
        user = User.objects.get(username=request.session.get("username"))
        c_slider = request.POST.get('c-slider')
        c_skill = Skills(skill_name='C',
                         skill_proficiency=0,
                         skill_guess_proficiency=c_slider,
                         skill_times_practiced=0,
                         user=user)
        c_skill.save()
        java_slider = request.POST.get('java-slider')
        java_skill = Skills(skill_name='Java',
                            skill_proficiency=0,
                            skill_guess_proficiency=java_slider,
                            skill_times_practiced=0,
                            user=user)
        java_skill.save()
        js_slider = request.POST.get('js-slider')
        js_skill = Skills(skill_name='Javascript',
                          skill_proficiency=0,
                          skill_guess_proficiency=js_slider,
                          skill_times_practiced=0,
                          user=user)
        js_skill.save()
        ts_slider = request.POST.get('ts-slider')
        ts_skill = Skills(skill_name='Typescript',
                          skill_proficiency=0,
                          skill_guess_proficiency=ts_slider,
                          skill_times_practiced=0,
                          user=user)
        ts_skill.save()
        cpp_slider = request.POST.get('cpp-slider')
        cpp_skill = Skills(skill_name='C++',
                           skill_proficiency=0,
                           skill_guess_proficiency=cpp_slider,
                           skill_times_practiced=0,
                           user=user)
        cpp_skill.save()
        linux_slider = request.POST.get('linux-slider')
        linux_skill = Skills(skill_name='Linux',
                             skill_proficiency=0,
                             skill_guess_proficiency=linux_slider,
                             skill_times_practiced=0,
                             user=user)
        linux_skill.save()
        sql_slider = request.POST.get('sql-slider')
        sql_skill = Skills(skill_name='SQL',
                           skill_proficiency=0,
                           skill_guess_proficiency=sql_slider,
                           skill_times_practiced=0,
                           user=user)
        sql_skill.save()
        html_slider = request.POST.get('html-slider')
        html_skill = Skills(skill_name='HTML',
                            skill_proficiency=0,
                            skill_guess_proficiency=html_slider,
                            skill_times_practiced=0,
                            user=user)
        html_skill.save()
        cs_slider = request.POST.get('cs-slider')
        cs_skill = Skills(skill_name='C#',
                          skill_proficiency=0,
                          skill_guess_proficiency=cs_slider,
                          skill_times_practiced=0,
                          user=user)
        cs_skill.save()
        python_slider = request.POST.get('python-slider')
        python_skill = Skills(skill_name='Python',
                              skill_proficiency=0,
                              skill_guess_proficiency=python_slider,
                              skill_times_practiced=0,
                              user=user)
        python_skill.save()
        return render(request, "GISEE/question2.html")
    else:
        return render(request, "GISEE/question2.html")


def question2_submit(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.session.get("username"))
        communication_slider = request.POST.get('c-slider')
        communication_skill = Skills(skill_name='Communication',
                                     skill_proficiency=0,
                                     skill_guess_proficiency=communication_slider,
                                     skill_times_practiced=0,
                                     user=user)
        communication_skill.save()
        planning_slider = request.POST.get('java-slider')
        planning_skill = Skills(skill_name='Planning',
                                skill_proficiency=0,
                                skill_guess_proficiency=planning_slider,
                                skill_times_practiced=0,
                                user=user)
        planning_skill.save()
        writing_slider = request.POST.get('js-slider')
        writing_skill = Skills(skill_name='Writing',
                               skill_proficiency=0,
                               skill_guess_proficiency=writing_slider,
                               skill_times_practiced=0,
                               user=user)
        writing_skill.save()
        requirement_scoping_slider = request.POST.get('ts-slider')
        rs_skill = Skills(skill_name='Requirement Scoping',
                          skill_proficiency=0,
                          skill_guess_proficiency=requirement_scoping_slider,
                          skill_times_practiced=0,
                          user=user)
        rs_skill.save()
        teamwork_slider = request.POST.get('cpp-slider')
        teamwork_skill = Skills(skill_name='Teamwork',
                                skill_proficiency=0,
                                skill_guess_proficiency=teamwork_slider,
                                skill_times_practiced=0,
                                user=user)
        teamwork_skill.save()
        return render(request, "GISEE/question3.html")
    else:
        return render(request, "GISEE/question3.html")


def question3_submit(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.session.get("username"))
        github_slider = request.POST.get('c-slider')
        github_skill = Skills(skill_name='Github',
                              skill_proficiency=0,
                              skill_guess_proficiency=github_slider,
                              skill_times_practiced=0,
                              user=user)
        github_skill.save()
        agile_slider = request.POST.get('java-slider')
        agile_skill = Skills(skill_name='Agile',
                             skill_proficiency=0,
                             skill_guess_proficiency=agile_slider,
                             skill_times_practiced=0,
                             user=user)
        agile_skill.save()
        documentation_slider = request.POST.get('js-slider')
        documentation_skill = Skills(skill_name='Documentation',
                                     skill_proficiency=0,
                                     skill_guess_proficiency=documentation_slider,
                                     skill_times_practiced=0,
                                     user=user)
        documentation_skill.save()
        project_planning_slider = request.POST.get('ts-slider')
        project_planning_skill = Skills(skill_name='Project Planning',
                                        skill_proficiency=0,
                                        skill_guess_proficiency=project_planning_slider,
                                        skill_times_practiced=0,
                                        user=user)
        project_planning_skill.save()
        docker_slider = request.POST.get('cpp-slider')
        docker_skill = Skills(skill_name='Docker',
                              skill_proficiency=0,
                              skill_guess_proficiency=docker_slider,
                              skill_times_practiced=0,
                              user=user)
        docker_skill.save()
        cloud_development_tools_slider = request.POST.get('linux-slider')
        cdt_skill = Skills(skill_name='Cloud Development Tools',
                           skill_proficiency=0,
                           skill_guess_proficiency=cloud_development_tools_slider,
                           skill_times_practiced=0,
                           user=user)
        cdt_skill.save()
        unit_testing_slider = request.POST.get('sql-slider')
        ut_skill = Skills(skill_name='Unit Testing',
                          skill_proficiency=0,
                          skill_guess_proficiency=unit_testing_slider,
                          skill_times_practiced=0,
                          user=user)
        ut_skill.save()
        return render(request, "GISEE/guessing_questions1.html")
    else:
        return render(request, "GISEE/guessing_questions1.html")


def skill_practice(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.POST.get("username"))
        skill = request.POST.get("skill")
        skills = Skills.objects.filter(user_id=user.id, skill_name=request.POST.get("skill"))
        skill_found = False
        for skill in skills.all():
            skill_found = True
            skill.skill_times_practiced = skill.skill_times_practiced + 1
            skill.save()
        if not skill_found:
            new_skill = Skills(skill_name=skill,
                               skill_proficiency=0,
                               skill_guess_proficiency=0,
                               skill_times_practiced=1,
                               user=user)
            new_skill.save()
    return render(request, "GISEE/resources.html")

