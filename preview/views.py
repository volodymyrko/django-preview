import random
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.utils.hashcompat import sha_constructor
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from django.conf import settings

from preview.models import BetaSignup 
from preview.forms import BetaSignupForm

def signup(request):
    if request.method == 'POST':
        form = BetaSignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            salt = sha_constructor(str(random.random())).hexdigest()[:5]
            if isinstance(email, unicode):
                email = email.encode('utf-8')
            activation_key = sha_constructor(salt+email).hexdigest()
            subsribe_email = form.save(commit=False)
            subsribe_email.key = activation_key
            subsribe_email.save()
            preview_send_mail = getattr(settings, 'PREVIEW_SEND_MAIL', True) 
            if preview_send_mail:
                if Site._meta.installed:
                    site = Site.objects.get_current()
                else:
                    site = request.get_host()
                subject = render_to_string('preview/email_subject.txt', {'site': site})
                message = render_to_string('preview/email.txt', {'url': reverse('preview_unsignup', args=[activation_key]), 'site': site })
                send_mail(subject , message, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=True)
            return redirect(reverse('preview_confirm'))
    else:
        form = BetaSignupForm()
    return render_to_response('preview/signup.html', {'form': form},
        context_instance=RequestContext(request))

def confirm(request):
    """ Confirmation Page """
    return render_to_response('preview/confirm.html',
        context_instance=RequestContext(request))

def unsignup(request, key):
    try:
        email = BetaSignup.objects.get(key=key)
    except ObjectDoesNotExist:
        email = None
    if email:
        email.delete()
    return render_to_response('preview/unsignup.html', {'email': email},
        context_instance=RequestContext(request))

