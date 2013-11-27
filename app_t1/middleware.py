import datetime
from app_t1.models import Requests

class RequestCountMiddleware(object):
    """
    Middleware class that store all http requests
    into database Requests
    """
    
    def process_request(self,request):   
        """
        Function which takes all input request
        """
    
        now_time = datetime.datetime.now()
        addr = request.META['REMOTE_ADDR']
        new_request = Requests(name=addr, time=now_time)
        new_request.save()
        return None
      


