from .cart import Cart
# from .forms import LoginForm


def cart(request):
	return {'cart': Cart(request)}

# def loginform(request):
# 	return {'form': LoginForm}