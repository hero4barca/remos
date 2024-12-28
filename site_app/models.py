from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class IndexPage(Page):
    header_message = models.CharField(max_length=250)

    content_panels = Page.content_panels + [
        FieldPanel('header_message'),
    ]