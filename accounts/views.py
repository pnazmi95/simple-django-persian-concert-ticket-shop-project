from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.conf import settings
from accounts.forms import ProfileRegisterForm, ProfileEditForm, UserEditForm
from django.contrib.auth.models import User
from accounts.models import ProfileModel
from django.views import View


class LoginView(View):
    template_name = "accounts/login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get("next"))

            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            context = {
                "username": username,
                "error_message": "کاربری با این مشخصات یافت نشد",
            }
            return render(request, self.template_name, context)


class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated and request.user.is_active:
            logout(request)
            return redirect('ticket_sales:concert_list_view')
        else:
            return redirect('accounts:login')


class ProfileView(View):
    template_name = "accounts/profile.html"

    def get(self, request):
        profile = request.user.profile

        context = {
            "profile": profile
        }

        return render(request, self.template_name, context)


class ProfileRegisterView(View):
    template_name = "accounts/profile_register.html"
    form_class = ProfileRegisterForm

    def get(self, request):
        profile_register_form = self.form_class()

        context = {
            "form_data": profile_register_form
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        profile_register_form = self.form_class(request.POST, request.FILES)
        if profile_register_form.is_valid():
            cd = profile_register_form.cleaned_data
            user = User.objects.create_user(
                username=cd["username"],
                email=cd['email'],
                password=cd['password'],
                first_name=cd['first_name'],
                last_name=cd['last_name'],
            )
            user.save()

            profile_model = ProfileModel(
                user=user,
                profile_pic=cd['profile_pic'],
                gender=cd['gender'],
                credit=cd['credit'],
            )

            profile_model.save()

            return redirect('ticket_sales:concert_list_view')
        else:
            context = {
                "form_data": profile_register_form
            }

            return render(request, self.template_name, context=context)


class ProfileEditView(View):
    template_name = "accounts/profile_edit.html"
    form_class_profile = ProfileEditForm
    form_class_user = UserEditForm

    def post(self, request):
        profile_edit_form = self.form_class_profile(request.POST, request.FILES, instance=request.user.profile)
        user_edit_form = self.form_class_user(request.POST, instance=request.user)
        if profile_edit_form.is_valid and user_edit_form.is_valid:
            profile_edit_form.save()
            user_edit_form.save()
            return redirect('accounts:profile')
        else:
            context = {

                "profile_edit_form": profile_edit_form,
                "user_edit_form": user_edit_form,
                "profile_pic": request.user.profile.profile_pic,

            }

            return render(request, self.template_name, context=context)

    def get(self, request):
        profile_edit_form = self.form_class_profile(instance=request.user.profile)
        user_edit_form = self.form_class_user(instance=request.user)

        context = {

            "profile_edit_form": profile_edit_form,
            "user_edit_form": user_edit_form,
            "profile_pic": request.user.profile.profile_pic,

        }

        return render(request, self.template_name, context=context)
