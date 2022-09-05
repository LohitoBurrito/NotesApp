from ctypes import sizeof
from fileinput import filename
from queue import Empty
import string
from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import fileUploadG, fileUploadL, fileUploadB, graingerMajor, lasMajor, giesMajor
from .models import contributors
from django.core.mail import send_mail


# Create your views here.
def index(request):
    creators = contributors.objects.all()
    if 'send' in request.POST:
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        send_mail(subject, email+": "+content, email,['lohitm2@illinois.edu'], fail_silently=False)
        return redirect('contact')
    return render(request, 'front.html', {'creators': creators})

def contact(request):
    if 'goBack' in request.POST:
        return redirect('index')
    return render(request, 'contact.html')

def login(request):
    if 'loginButton' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            department = request.POST['Department']
            if (department == 'choose-department'):
                messages.info(request, 'choose department')
                return redirect('login')
            elif (department == 'grainger'):
                return redirect(grainger)
            elif (department == 'gies'):
                return redirect('gies')
            else:
                return redirect('las')
        else:
            messages.info(request, 'credentials invalid')
            return redirect('login')
    
    if 'registerButton' in request.POST:
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            username = request.POST['username']
            email = request.POST['email']
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already used')
                return redirect('login')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('login')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request, 'account created, please log in')
                return redirect('login')

    return render(request, 'login.html')

def grainger(request):
    selected = graingerMajor.objects.all()
    displayedNotes = fileUploadG.objects.all()

    if 'ApplyFilters' in request.POST:
        majorTag = request.POST.get('Courses')
        Num = request.POST.get('Course_Number')
        Name = request.POST.get('name')
        username = request.POST.get('maker')
        
        if majorTag != 'CourseTag':
            if Num != "":
                if Name != "":
                    if username != "":
                        displayedNotes = fileUploadG.objects.all().filter(courseTag = majorTag, courseNum = Num, name = Name, creator = username)
                    else:
                        displayedNotes = fileUploadG.objects.all().filter(courseTag = majorTag, courseNum = Num, name = Name)
                else:
                    if username != "":
                        displayedNotes = fileUploadG.objects.all().filter(courseTag = majorTag, courseNum = Num, creator = username) 
                    else:
                        displayedNotes = fileUploadG.objects.all().filter(courseTag = majorTag, courseNum = Num) 
            else:
                if Name != "":
                    if username != "":
                        displayedNotes = fileUploadG.objects.all().filter(courseTag = majorTag, name = Name, creator = username)
                    else:
                        displayedNotes = fileUploadG.objects.all().filter(courseTag = majorTag, name = Name)
                else:
                    if username != "":
                        displayedNotes = fileUploadG.objects.all().filter(courseTag = majorTag, creator = username)
                    else:
                        displayedNotes = fileUploadG.objects.all().filter(courseTag = majorTag) 
        else: 
            if Num != "":
                if Name != "":
                    if username != "":
                        displayedNotes = fileUploadG.objects.all().filter(courseNum = Num, name = Name, creator = username)
                    else:
                        displayedNotes = fileUploadG.objects.all().filter(courseNum = Num, name = Name)
                else:
                    if username != "":
                        displayedNotes = fileUploadG.objects.all().filter(courseNum = Num, creator = username)
                    else:
                        displayedNotes = fileUploadG.objects.all().filter(courseNum = Num) 
            else:
                if Name != "":
                    if username != "":
                        displayedNotes = fileUploadG.objects.all().filter(name = Name, creator = username)
                    else:
                        displayedNotes = fileUploadG.objects.all().filter(name = Name)
                else:
                    if username != "":
                        displayedNotes = fileUploadG.objects.all().filter(creator = username)
                    else:
                        displayedNotes = fileUploadG.objects.all() 


    return render(request, 'grainger.html', {'selected': selected, 'displayedNotes': displayedNotes})

def addNotesGrainger(request):
    selected = graingerMajor.objects.all()
    if 'ReturnButton' in request.POST:
        majorTag = request.POST.get('CourseTag')
        Num = request.POST.get('CourseNumber')
        Name = request.POST.get('NameOfNotes')
        fileName = request.FILES['file']
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        if len(Num) == 0 or len(Name) == 0 or len(majorTag) == 0 or len(fileName) == 0:
            return redirect('grainger')
        note = fileUploadG.objects.create(courseTag = majorTag, courseNum = Num, name = Name, file = fileName, creator = username)
        note.save()

        CheckContributor = contributors.objects.all().filter(creatorName = username).exists()
        if not CheckContributor:
            person = contributors.objects.create(creatorName = username)
            person.save()
        return redirect('grainger')

    return render(request, 'addNotesGrainger.html', {'selected': selected})

def edit(request, id, branch: str):
    if branch == 'grainger':
        selected = graingerMajor.objects.all()
        if 'delete' in request.POST:
            fileUploadG.objects.all().filter(id = id).delete()
            username = None
            if request.user.is_authenticated:
                username = request.user.username
            checkContributor = fileUploadG.objects.all().filter(creator = username).exists()
            if not checkContributor:
                contributors.objects.all().filter(creatorName = username).delete()
            return redirect('grainger')

        if 'editComplete' in request.POST:
            fileUploadG.objects.all().filter(id = id).delete()
            majorTag = request.POST.get('CourseTag')
            Num = request.POST.get('CourseNumber')
            Name = request.POST.get('NameOfNotes')
            fileName = request.FILES['file']
            username = None
            if request.user.is_authenticated:
                username = request.user.username
            if len(Num) == 0 or len(Name) == 0 or len(majorTag) == 0 or len(fileName) == 0:
                return redirect('grainger')
            note = fileUploadG.objects.create(id = id, courseTag = majorTag, courseNum = Num, name = Name, file = fileName, creator = username)
            note.save()        
            return redirect('grainger')
    if branch == 'las':
        selected = lasMajor.objects.all()
        if 'delete' in request.POST:
            fileUploadL.objects.all().filter(id = id).delete()
            username = None
            if request.user.is_authenticated:
                username = request.user.username
            checkContributor = fileUploadL.objects.all().filter(creator = username).exists()
            if not checkContributor:
                contributors.objects.all().filter(creatorName = username).delete()
            return redirect('las')

        if 'editComplete' in request.POST:
            fileUploadL.objects.all().filter(id = id).delete()
            majorTag = request.POST.get('CourseTag')
            Num = request.POST.get('CourseNumber')
            Name = request.POST.get('NameOfNotes')
            fileName = request.FILES['file']
            username = None
            if request.user.is_authenticated:
                username = request.user.username
            if len(Num) == 0 or len(Name) == 0 or len(majorTag) == 0 or len(fileName) == 0:
                return redirect('las')
            note = fileUploadL.objects.create(id = id, courseTag = majorTag, courseNum = Num, name = Name, file = fileName, creator = username)
            note.save()        
            return redirect('las')
    
    if branch == 'gies':
        selected = giesMajor.objects.all()
        if 'delete' in request.POST:
            fileUploadB.objects.all().filter(id = id).delete()
            username = None
            if request.user.is_authenticated:
                username = request.user.username
            checkContributor = fileUploadB.objects.all().filter(creator = username).exists()
            if not checkContributor:
                contributors.objects.all().filter(creatorName = username).delete()
            return redirect('las')

        if 'editComplete' in request.POST:
            fileUploadB.objects.all().filter(id = id).delete()
            majorTag = request.POST.get('CourseTag')
            Num = request.POST.get('CourseNumber')
            Name = request.POST.get('NameOfNotes')
            fileName = request.FILES['file']
            username = None
            if request.user.is_authenticated:
                username = request.user.username
            if len(Num) == 0 or len(Name) == 0 or len(majorTag) == 0 or len(fileName) == 0:
                return redirect('gies')
            note = fileUploadB.objects.create(id = id, courseTag = majorTag, courseNum = Num, name = Name, file = fileName, creator = username)
            note.save()        
            return redirect('gies')
    
    return render(request, 'edit.html', {'selected': selected})

def las(request):
    selected = lasMajor.objects.all()
    displayedNotes = fileUploadL.objects.all()

    if 'ApplyFilters' in request.POST:
        majorTag = request.POST.get('Courses')
        Num = request.POST.get('Course_Number')
        Name = request.POST.get('name')
        username = request.POST.get('maker')
        
        if majorTag != 'CourseTag':
            if Num != "":
                if Name != "":
                    if username != "":
                        displayedNotes = fileUploadL.objects.all().filter(courseTag = majorTag, courseNum = Num, name = Name, creator = username)
                    else:
                        displayedNotes = fileUploadL.objects.all().filter(courseTag = majorTag, courseNum = Num, name = Name)
                else:
                    if username != "":
                        displayedNotes = fileUploadL.objects.all().filter(courseTag = majorTag, courseNum = Num, creator = username) 
                    else:
                        displayedNotes = fileUploadL.objects.all().filter(courseTag = majorTag, courseNum = Num) 
            else:
                if Name != "":
                    if username != "":
                        displayedNotes = fileUploadL.objects.all().filter(courseTag = majorTag, name = Name, creator = username)
                    else:
                        displayedNotes = fileUploadL.objects.all().filter(courseTag = majorTag, name = Name)
                else:
                    if username != "":
                        displayedNotes = fileUploadL.objects.all().filter(courseTag = majorTag, creator = username)
                    else:
                        displayedNotes = fileUploadL.objects.all().filter(courseTag = majorTag) 
        else: 
            if Num != "":
                if Name != "":
                    if username != "":
                        displayedNotes = fileUploadL.objects.all().filter(courseNum = Num, name = Name, creator = username)
                    else:
                        displayedNotes = fileUploadL.objects.all().filter(courseNum = Num, name = Name)
                else:
                    if username != "":
                        displayedNotes = fileUploadL.objects.all().filter(courseNum = Num, creator = username)
                    else:
                        displayedNotes = fileUploadL.objects.all().filter(courseNum = Num) 
            else:
                if Name != "":
                    if username != "":
                        displayedNotes = fileUploadL.objects.all().filter(name = Name, creator = username)
                    else:
                        displayedNotes = fileUploadL.objects.all().filter(name = Name)
                else:
                    if username != "":
                        displayedNotes = fileUploadL.objects.all().filter(creator = username)
                    else:
                        displayedNotes = fileUploadL.objects.all() 

    return render(request, 'las.html', {'selected': selected, 'displayedNotes': displayedNotes})

def gies(request):
    selected = giesMajor.objects.all()
    displayedNotes = fileUploadB.objects.all()

    if 'ApplyFilters' in request.POST:
        majorTag = request.POST.get('Courses')
        Num = request.POST.get('Course_Number')
        Name = request.POST.get('name')
        username = request.POST.get('maker')
        
        if majorTag != 'CourseTag':
            if Num != "":
                if Name != "":
                    if username != "":
                        displayedNotes = fileUploadB.objects.all().filter(courseTag = majorTag, courseNum = Num, name = Name, creator = username)
                    else:
                        displayedNotes = fileUploadB.objects.all().filter(courseTag = majorTag, courseNum = Num, name = Name)
                else:
                    if username != "":
                        displayedNotes = fileUploadB.objects.all().filter(courseTag = majorTag, courseNum = Num, creator = username) 
                    else:
                        displayedNotes = fileUploadB.objects.all().filter(courseTag = majorTag, courseNum = Num) 
            else:
                if Name != "":
                    if username != "":
                        displayedNotes = fileUploadB.objects.all().filter(courseTag = majorTag, name = Name, creator = username)
                    else:
                        displayedNotes = fileUploadB.objects.all().filter(courseTag = majorTag, name = Name)
                else:
                    if username != "":
                        displayedNotes = fileUploadB.objects.all().filter(courseTag = majorTag, creator = username)
                    else:
                        displayedNotes = fileUploadB.objects.all().filter(courseTag = majorTag) 
        else: 
            if Num != "":
                if Name != "":
                    if username != "":
                        displayedNotes = fileUploadB.objects.all().filter(courseNum = Num, name = Name, creator = username)
                    else:
                        displayedNotes = fileUploadB.objects.all().filter(courseNum = Num, name = Name)
                else:
                    if username != "":
                        displayedNotes = fileUploadB.objects.all().filter(courseNum = Num, creator = username)
                    else:
                        displayedNotes = fileUploadB.objects.all().filter(courseNum = Num) 
            else:
                if Name != "":
                    if username != "":
                        displayedNotes = fileUploadB.objects.all().filter(name = Name, creator = username)
                    else:
                        displayedNotes = fileUploadB.objects.all().filter(name = Name)
                else:
                    if username != "":
                        displayedNotes = fileUploadB.objects.all().filter(creator = username)
                    else:
                        displayedNotes = fileUploadB.objects.all() 
    return render(request, 'gies.html', {'selected': selected, 'displayedNotes': displayedNotes})

def addNotesLas(request):
    selected = lasMajor.objects.all()
    if 'ReturnButton' in request.POST:
        majorTag = request.POST.get('CourseTag')
        Num = request.POST.get('CourseNumber')
        Name = request.POST.get('NameOfNotes')
        fileName = request.FILES['file']
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        if len(Num) == 0 or len(Name) == 0 or len(majorTag) == 0 or len(fileName) == 0:
            return redirect('las')
        note = fileUploadL.objects.create(courseTag = majorTag, courseNum = Num, name = Name, file = fileName, creator = username)
        note.save()

        CheckContributor = contributors.objects.all().filter(creatorName = username).exists()
        if not CheckContributor:
            person = contributors.objects.create(creatorName = username)
            person.save()
        return redirect('las')

    return render(request, 'addNotesLas.html', {'selected': selected})

def addNotesGies(request):
    selected = giesMajor.objects.all()
    if 'ReturnButton' in request.POST:
        majorTag = request.POST.get('CourseTag')
        Num = request.POST.get('CourseNumber')
        Name = request.POST.get('NameOfNotes')
        fileName = request.FILES['file']
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        if len(Num) == 0 or len(Name) == 0 or len(majorTag) == 0 or len(fileName) == 0:
            return redirect('gies')
        note = fileUploadB.objects.create(courseTag = majorTag, courseNum = Num, name = Name, file = fileName, creator = username)
        note.save()

        CheckContributor = contributors.objects.all().filter(creatorName = username).exists()
        if not CheckContributor:
            person = contributors.objects.create(creatorName = username)
            person.save()
        return redirect('gies')

    return render(request, 'addNotesGies.html', {'selected': selected})