from django.db import models
from django.core.exceptions import ValidationError

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField


class IndexPage(Page):
    header_message = models.CharField(max_length=250)

    content_panels = Page.content_panels + [
        FieldPanel('header_message'),
    ]


class AboutPage(Page):
    header_message = models.CharField(max_length=250)

    content_panels = Page.content_panels + [
        FieldPanel('header_message'),
    ]

class ProductsPage(Page):
    header_message = models.CharField(max_length=250)

    content_panels = Page.content_panels + [
        FieldPanel('header_message'),
    ]

class SoftwareModemsPage(Page):
    header_message = models.CharField(max_length=250)

    content_panels = Page.content_panels + [
        FieldPanel('header_message'),
    ]

class ContactPage(Page):
    header_message = models.CharField(max_length=250)

    content_panels = Page.content_panels + [
        FieldPanel('header_message'),
    ]

class BlogPage(Page):
    header_message = models.CharField(max_length=250)

    content_panels = Page.content_panels + [
        FieldPanel('header_message'),
    ]

class PodcastEpisodePage(Page):
    header_message = models.CharField(max_length=250)

    episode_title = models.CharField(max_length=60,
                    help_text="maximum of 60 characters" )
    episode_subtitle = models.CharField(max_length=55,
                    help_text="maximum of 55 characters")
    episode_description = RichTextField(
        help_text = "Episode description or summary here. Max of 600 characters"
            )
    episode_thumbnail_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.PROTECT,
        related_name='+',
        help_text="Thumbnail image of the episode. Recommended dimension: 1140x570 pixels "
    )


    content_panels = Page.content_panels + [
        FieldPanel('header_message'),
        FieldPanel('episode_title'),
        FieldPanel('episode_subtitle'),
        FieldPanel('episode_description'),
        FieldPanel('episode_thumbnail_img'),
    ]

    def clean(self):
        super().clean()
        if len(self.episode_description) > 600:  # Replace with your max length
            raise ValidationError("Episode description exceeds maximum length of 1000 characters.")
        if self.episode_thumbnail_img == None:
            raise ValidationError("thumbnail image is required")
