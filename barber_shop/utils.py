from pytils.translit import slugify

def gen_slug(obj_title):
    return slugify(obj_title)


class ShopMixin:
    def get_filter_context(self, **kwargs):
        from .models import ProductGroup, Manufacturer
        context = kwargs
        context['groups_in_filter'] = ProductGroup.objects.all().order_by('group')
        manufacturer_names = Manufacturer.objects.all().order_by('manufacturer')
        names_in_filter = []
        for name in manufacturer_names:
            names_in_filter.append(name.__str__())
        context['names_in_filter'] = names_in_filter
        return context

    def get_pagination_parameters(self, **kwargs):
        context = kwargs
        get_copy = self.request.GET.copy()
        path_parameters = get_copy.pop('page', True) and get_copy.urlencode()
        context['path_parameters'] = path_parameters
        return context

