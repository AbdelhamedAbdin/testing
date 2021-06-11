from django.shortcuts import render, redirect
from .models import Response, Student, Character, Error
from django.core.paginator import Paginator
from .custom_decorators import decoratorDirect
from .models import History
from ipware import get_client_ip


def record_history_action(request, is_visitor):
    print(is_visitor)


@decoratorDirect
def student_response_list(request):
    characters = Character.objects.all().distinct()
    errors = Error.objects.all().distinct()
    students = Student.objects.all().distinct()
    responses = Response.objects.all().distinct()

    unique_grade = []
    error_class = []
    error_number = []
    error_unit = []
    error_type = []
    regularity = []
    remark = []

    char, reg, complex, grade, gender, correct, err_class, err_number = None, None, None, None, None, None, None, None
    err_unit, err_type, rem, err, stud = None, None, None, None, None

    character_req = request.GET.get('char')
    regularity_req = request.GET.get('reg')
    complexity_req = request.GET.get('complex')
    grade_req = request.GET.get('grade')
    gender_req = request.GET.get('gender')
    correct_req = request.GET.get('correct')
    errorClass_req = request.GET.get('error_class')
    errorNumber_req = request.GET.get('error_number')
    errorUnit_req = request.GET.get('error_unit')
    errorType_req = request.GET.get('error_type')
    remark_req = request.GET.get('remark')

    for student in students:
        unique_grade.append(student.grade)
    unique_grade = list(set(unique_grade))

    for error in errors:
        error_class.append(error.error_class)
        error_number.append(error.error_number)
        error_unit.append(error.error_unit)
        error_type.append(error.error_type)
        remark.append(error.remark)
    error_class = list(set(error_class))
    error_number = list(set(error_number))
    error_unit = list(set(error_unit))
    error_type = list(set(error_type))
    remark = list(set(remark))

    for c in characters:
        regularity.append(c.regularity)
    regularity = list(set(regularity))

    # specify selected attribute for select input
    if character_req and character_req != 'all':
        char = Character.objects.get(id=int(character_req))

    if regularity_req and regularity_req != 'all':
        reg = regularity_req

    if complexity_req and complexity_req != 'all':
        complex = complexity_req

    if grade_req and grade_req != 'all':
        grade = grade_req

    if gender_req and gender_req != 'all':
        gender = gender_req

    if correct_req and correct_req != 'all':
        correct = correct_req

    if errorClass_req and errorClass_req != 'all':
        err_class = errorClass_req

    if errorType_req and errorType_req != 'all':
        err_type = errorType_req

    if errorUnit_req and errorUnit_req != 'all':
        err_unit = errorUnit_req

    if errorNumber_req and errorNumber_req != 'all':
        err_number = errorNumber_req

    if remark_req and remark_req != 'all':
        rem = remark_req

    # filter by response_field to get the specific data
    all_char = Character.objects.all()
    resp = Response.objects.all()
    all_student = Student.objects.all()
    all_error = Error.objects.all()
    reg_list = []
    comp_list = []
    grade_list = []
    gender_list = []
    errClass_list = []
    errNumber_list = []
    errType_list = []
    errUnit_list = []
    remark_list = []

    if 'char' in request.GET:
        if character_req == 'all':
            all_char = all_char
            resp = resp
        else:
            all_char = all_char.filter(id=character_req)
            resp = resp.filter(character__in=all_char)

    if 'reg' in request.GET:
        if regularity_req == 'all':
            all_char = all_char
            resp = resp
        else:
            all_char = all_char.filter(regularity=regularity_req)
            for c in all_char:
                reg_list.append(c.regularity)
            resp = resp.filter(character__regularity__in=reg_list)

    if 'complex' in request.GET:
        if complexity_req == 'all':
            all_char = all_char
            resp = resp
        else:
            all_char = all_char.filter(complexity=complexity_req)
            for c in all_char:
                comp_list.append(c.complexity)
            resp = resp.filter(character__complexity__in=comp_list)

    if 'grade' in request.GET:
        if grade_req == 'all':
            all_student = all_student
            resp = resp
        else:
            all_student = all_student.filter(grade=grade_req)
            for s in all_student:
                grade_list.append(str(s.grade))
            resp = resp.filter(student__grade__in=grade_list)

    if 'gender' in request.GET:
        if gender_req == 'all':
            all_student = all_student
            resp = resp
        else:
            all_student = all_student.filter(gender=gender_req)
            for s in all_student:
                gender_list.append(str(s.gender))
            resp = resp.filter(student__gender__in=gender_list)

    if 'correct' in request.GET:
        if correct_req == 'all':
            resp = resp
        else:
            resp = resp.filter(correct=correct_req)

    if 'error_class' in request.GET:
        if errorClass_req == 'all':
            all_error = all_error
            resp = resp
        else:
            all_error = all_error.filter(error_class=errorClass_req)
            for e in all_error:
                errClass_list.append(e.error_class)
            resp = resp.filter(student__error__error_class__in=errClass_list)

    if 'error_number' in request.GET:
        if errorNumber_req == 'all':
            all_error = all_error
            resp = resp
        else:
            all_error = all_error.filter(error_number=errorNumber_req)
            for e in all_error:
                errNumber_list.append(e.error_number)
            resp = resp.filter(student__error__error_number__in=errNumber_list)

    if 'error_type' in request.GET:
        if errorType_req == 'all':
            all_error = all_error
            resp = resp
        else:
            all_error = all_error.filter(error_type=errorType_req)
            for e in all_error:
                errType_list.append(e.error_type)
            resp = resp.filter(student__error__error_type__in=errType_list)

    if 'error_unit' in request.GET:
        if errorUnit_req == 'all':
            all_error = all_error
            resp = resp
        else:
            all_error = all_error.filter(error_unit=errorUnit_req)
            for e in all_error:
                errUnit_list.append(e.error_unit)
            resp = resp.filter(student__error__error_unit__in=errUnit_list)

    if 'remark' in request.GET:
        if remark_req == 'all':
            all_error = all_error
            resp = resp
        else:
            all_error = all_error.filter(remark=remark_req)
            for e in all_error:
                remark_list.append(e.remark)
            resp = resp.filter(student__error__remark__in=remark_list)

    all_response = resp
    paginator = Paginator(all_response, 100)
    page_number = request.GET.get('page_number')
    all_response = paginator.get_page(page_number)
    if all_response.has_next():
        next_url = f"{request.get_raw_uri()}&page_number={all_response.next_page_number()}"
    else:
        next_url = ''

    if all_response.has_previous():
        prev_url = f"{request.get_raw_uri()}&page_number={all_response.previous_page_number()}"
    else:
        prev_url = ''

    print(request.is_visitor)

    context = {
        'all_response': all_response,
        'all_error': all_error,
        'responses': responses,
        'students': students,
        'next_url': next_url,
        'prev_url': prev_url,
        'errors': errors,
        'characters': characters,
        'unique_grade': unique_grade,
        'error_class': error_class,
        'error_number': error_number,
        'error_unit': error_unit,
        'error_type': error_type,
        'regularity': regularity,
        'remark': remark,
        'char': char,
        'reg': reg,
        'complex': complex,
        'grade': grade,
        'gender': gender,
        'correct': correct,
        'err_class': err_class,
        'err_unit': err_unit,
        'err_number': err_number,
        'err_type': err_type,
        'rem': rem
    }
    return render(request, 'student_grade/response_view.html', context)
