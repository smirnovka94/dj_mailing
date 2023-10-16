from django.conf import settings
from django.core.cache import cache

def get_cache_clients(self):
    if settings.CACHE_ENABLED:
        key = 'category_list'
        clients_list = cache.get(key)
        if clients_list is None:
            clients_list = self.object_list.all()
            cache.set(key, clients_list)
    else:
        clients_list = self.object_list.all()

    return clients_list