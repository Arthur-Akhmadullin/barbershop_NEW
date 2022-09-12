from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


@login_required
def dashboard(request):
    return render(request, 'barber_account/dashboard.html', {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создаем нового пользователя, но пока не сохраняем в базу данных.
            new_user = user_form.save(commit=False)
            # Задаем пользователю зашифрованный пароль.
            new_user.set_password(user_form.cleaned_data['password'])
            # Сохраняем пользователя в базе данных.
            Profile.objects.create(user=new_user)
            new_user.save()
            return render(request, 'barber_account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'barber_account/register.html', {'user_form': user_form})


@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST,
                                       files=request.FILES
                                       )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль успешно обновлен')
        else:
            messages.error(request, 'Ошибка обновления профиля')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'barber_account/profile_edit.html', {'user_form': user_form,
                                                                'profile_form': profile_form
                                                                }
                  )


@login_required
def show_my_orders(request):
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.filter(user=user).get()
    my_orders = profile.profile_orders.all()
    return render(request, 'barber_account/my_orders.html', {'my_orders': my_orders})