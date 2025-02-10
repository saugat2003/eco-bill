# filepath: /C:/Users/Acer/OneDrive/Desktop/ecobill/eco-bill/eco-bill/base/utils.py

from io import BytesIO
from django.template.loader import get_template
from django.template import Context
from xhtml2pdf import pisa
from django.http import HttpResponse

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return result.getvalue()
    return None