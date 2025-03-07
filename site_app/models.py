from django.db import models
from django.core.exceptions import ValidationError
import datetime

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.blocks import TextBlock, CharBlock, URLBlock, RichTextBlock, BooleanBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock, ImageBlock
from wagtail.embeds.blocks import EmbedBlock



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

    date = models.DateField(auto_now_add=True)


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

class ImageTextBlock(StructBlock):
    text = RichTextBlock(required=True, help_text="Add the text for this section")
    image = ImageBlock(required=True, help_text="Choose an image for this section")
    text_on_left = BooleanBlock(
        required=False,
        default=True,
        help_text="Check this box to position the text on the left and the image on the right. Uncheck to reverse."
    )

    class Meta:
        template = "site_app/blocks/image_text_block.html"  # Template to render this block
        icon = "image"  # Wagtail editor icon


class TwoImagesBlock(StructBlock):
    image_1 = ImageBlock(required=True, help_text="Choose an image for this section")
    image_2 = ImageBlock(required=True, help_text="Choose an image for this section")
    class Meta:
        template = "site_app/blocks/two_images_block.html"  # Template to render this block
        icon = "image"  # Wagtail editor icon

class EmbedTextBlock(StructBlock):
    text = RichTextBlock(required=True, help_text="Add the text for this section")
    media = EmbedBlock(max_width=500,
                        max_height=300,
                        max_length=200,
                        required=True, help_text="Enter url for embeded media")
    text_on_left = BooleanBlock(
        required=False,
        default=True,
        help_text="Check this box to position the text on the left and the image on the right. Uncheck to reverse."
    )

    class Meta:
        template = "site_app/blocks/media_text_block.html"  # Template to render this block
        icon = "image"  # Wagtail editor icon


class NewsArticlePage(Page):
    header_message = models.CharField(max_length=250)

    article_title = models.CharField(max_length=120,
                    help_text="maximum of 120 characters" )
    article_subtitle = models.CharField(max_length=200,
                    help_text="maximum of 200 characters")

    article_thumbnail_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.PROTECT,
        related_name='+',
        help_text="Thumbnail image for the article. Recommended dimension: 1140x570 pixels"
    )

    date = models.DateField(auto_now_add=True)
    article_body = StreamField(
        [
            ('paragraph', RichTextBlock(template='site_app/blocks/paragraph.html')),
            ('h2', CharBlock(max_length=200, help_text="level 2 headings",  template='site_app/blocks/two_headings.html'  )),
            ('h3', CharBlock( max_length=200, help_text="level 3 headings",  template='site_app/blocks/three_headings.html' )),
            ('image', ImageBlock(template='site_app/blocks/image_full.html' )),
            ('embeded_media', EmbedBlock(
                max_width=700, max_height=400, max_length=200,
                help_text="embed media files like videos, social media posts/shares etc.",
                template='site_app/blocks/embed_media.html') ),
            ('paragraph_beside_image', ImageTextBlock( help_text="image beside paragraph")),
            ('two_images', TwoImagesBlock(help_text="two images side by side")),
            ('paragraph_beside_media', EmbedTextBlock(help_text="paragraph beside embeded media") ),

        ],
        block_counts={
            'paragraph': {'min_num': 1},
            'h2': {'max_num': 3},
        },
        use_json_field=True,
        blank=True,
        null=True,
    )


    content_panels = Page.content_panels + [
        FieldPanel('header_message'),
        FieldPanel('article_title'),
        FieldPanel('article_subtitle'),
        FieldPanel('article_thumbnail_img'),
        FieldPanel('article_body'),

    ]

    def clean(self):
        super().clean()
        if self.article_thumbnail_img == None:
            raise ValidationError("thumbnail image is required")