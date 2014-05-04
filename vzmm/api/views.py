

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Email
from api.serializers import EmailSerializer
from api.sgmail import SGClient
import json

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def email_tour(request):
    """
    List all code emails, or create a new snippet.
    """
    if request.method == 'GET':
        emails = Email.objects.all()
        serializer = EmailSerializer(emails, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        (status, msg) = send_email(**data)
        data['sg_status'] = status
        data['sg_msg'] = json.loads(msg).get('message')
        serializer = EmailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


def send_email(user_name=None, user_email=None, domain=None, comment=None):
    """
    Send the actual email
    """
    subject = "About your recent contact to %s" % (domain)
    from_email = "%s <%s>" %(user_name, user_email)
    sgc = SGClient()
    sgc.compose_msg(subject=subject, text=comment)
    return sgc.send(from_email=from_email,
        domain=domain)
