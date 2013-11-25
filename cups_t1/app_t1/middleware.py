import datetime
from app_t1.models import Request

class RequestCounting(object):

    def process_request(self, request):
        new = Request()
        new.name = request.META['REMOTE_ADDR']
        new.time = datetime.datetime.now()
        new.save()
        return None
