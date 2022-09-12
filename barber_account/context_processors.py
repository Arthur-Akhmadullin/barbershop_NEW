from .forms import LoginForm


def loginform(request):
    return {'form': LoginForm}