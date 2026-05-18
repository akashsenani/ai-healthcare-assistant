from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from .models import (
    UserProfile,
    BMIHistory
)

# =====================================================
# HOME PAGE
# =====================================================

def home(request):

    return render(
        request,
        'home.html'
    )

# =====================================================
# SIGNUP
# =====================================================

def signup_view(request):

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        # CHECK IF USER EXISTS
        if User.objects.filter(
            username=username
        ).exists():

            return render(

                request,

                'signup.html',

                {
                    'error':
                    'Username already exists'
                }
            )

        # CREATE USER
        user = User.objects.create_user(

            username=username,

            password=password
        )

        user.save()

        return redirect('login')

    return render(

        request,

        'signup.html'
    )

# =====================================================
# LOGIN
# =====================================================

def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(

            request,

            username=username,

            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

        else:

            return render(

                request,

                'login.html',

                {
                    'error':
                    'Invalid Credentials'
                }
            )

    return render(

        request,

        'login.html'
    )

# =====================================================
# LOGOUT
# =====================================================

def logout_view(request):

    logout(request)

    return redirect('home')

# =====================================================
# PROFILE PAGE
# =====================================================

def profile_view(request):

    if not request.user.is_authenticated:

        return redirect('login')

    # GET OR CREATE PROFILE
    profile, created = UserProfile.objects.get_or_create(

        user=request.user
    )

    if request.method == 'POST':

        age = request.POST['age']

        weight = float(
            request.POST['weight']
        )

        height_cm = float(
            request.POST['height']
        )

        # CONVERT CM TO METERS
        height_m = height_cm / 100

        # BMI CALCULATION
        bmi = weight / (
            height_cm * height_cm
        )

        # SAVE PROFILE
        profile.age = age

        profile.weight = weight

        profile.height = height_cm

        profile.bmi = round(
            bmi,
            2
        )

        profile.save()

        # SAVE BMI HISTORY
        latest_bmi = BMIHistory.objects.filter(

            user=request.user

        ).last()

        # AVOID DUPLICATES
        if (

            not latest_bmi or

            latest_bmi.bmi != profile.bmi
        ):

            BMIHistory.objects.create(

                user=request.user,

                bmi=profile.bmi
            )

    return render(

        request,

        'profile.html',

        {
            'profile': profile
        }
    )