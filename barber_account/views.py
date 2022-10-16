from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


@login_required
def dashboard(request):
    return render(request, 'barber_account/dashboard.html', {'section': 'dashboard'})

@login_required
def show_my_orders(request):
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.filter(user=user).get()
    my_orders = profile.profile_orders.all()
    return render(request, 'barber_account/my_orders.html', {'my_orders': my_orders})


class Register(View):
    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создаем нового пользователя, но пока не сохраняем в базу данных.
            new_user = user_form.save(commit=False)
            # Задаем пользователю зашифрованный пароль.
            new_user.set_password(user_form.cleaned_data['password'])
            # Сохраняем пользователя в базе данных.
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'barber_account/register_done.html', {'new_user': new_user})

    def get(self, request):
        user_form = UserRegistrationForm()
        return render(request, 'barber_account/register.html', {'user_form': user_form})


class ProfileEdit(LoginRequiredMixin, View):
    def post(self, request):
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
        return self.get(request)

    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'barber_account/profile_edit.html', {'user_form': user_form,
                                                                    'profile_form': profile_form
                                                                    }
                      )