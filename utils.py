from money import Currency, CURRENCY
from decimal import Decimal
import urllib
import xml.dom
from xml.dom import minidom
from models import ExchangeRate

RATES_URL = "https://liqpay.com/exchanges/exchanges.cgi"

def parse_liqpay_exchanges():
    """
<rates> 
  <EUR> 
    <RUR>41.2499</RUR> 
    <UAH>11.5500</UAH> 
    <USD>1.4154</USD> 
  </EUR> 
  <RUR> 
    <EUR>0.0226</EUR> 
    <UAH>0.2680</UAH> 
    <USD>0.0328</USD> 
  </RUR> 
  <UAH> 
    <EUR>0.0843</EUR> 
    <RUR>3.5714</RUR> 
    <USD>0.1225</USD> 
  </UAH> 
  <USD> 
    <EUR>0.6818</EUR> 
    <RUR>28.8571</RUR> 
    <UAH>8.0800</UAH> 
  </USD> 
</rates> 
    """
    CURRENCY['RUR'] = Currency(code='RUR', numeric='643', name='Russian Ruble', countries=['RUSSIAN FEDERATION'])
    rates = []
    dom = minidom.parse(urllib.urlopen(RATES_URL))
    if dom.documentElement.tagName != "rates":
        return rates
    for node1 in dom.documentElement.childNodes:
        if node1.nodeType == xml.dom.Node.ELEMENT_NODE:
            # get primary currency code
            code = node1.tagName.encode('utf-8')
            primary_currency = CURRENCY[code]
            for node2 in node1.childNodes:
                value = None
                secondary_currency = None
                if node2.nodeType == xml.dom.Node.ELEMENT_NODE:
                    code = node2.tagName.encode('utf-8')
                    secondary_currency = CURRENCY[code]
                    # find value
                    for node3 in node2.childNodes:
                        if node3.nodeType == xml.dom.Node.TEXT_NODE and (node3.nodeValue is not None):
                            value = Decimal(node3.nodeValue)
                if (primary_currency is not None) and (secondary_currency is not None) and (value is not None):
                    rates.append(ExchangeRate(primary_currency, secondary_currency, value))
    dom.unlink()
    return rates
