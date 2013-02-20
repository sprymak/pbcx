from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect

from utils import ExchangeRate, parse_liqpay_exchanges

def index(request, template_name='finance/index.html'):
    '''Display finance overview page'''
    context = RequestContext(request)
    rates = parse_liqpay_exchanges()
    return render_to_response(template_name,
        {'rates':rates },
        context_instance=context)
