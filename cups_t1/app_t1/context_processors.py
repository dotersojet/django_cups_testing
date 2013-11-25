from django.conf import settings

def settings_context_processor(request):
    arg_list = [arg for arg in dir(settings) if not arg.startswith('_')]
    w = {}
    for key in arg_list:
        w[key] = settings.__getattr__(key)
    return {'settings': w}
    
