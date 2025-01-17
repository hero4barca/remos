# Generated by Django 5.1.4 on 2025-01-17 13:26

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0021_alter_newsarticlepage_article_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticlepage',
            name='article_body',
            field=wagtail.fields.StreamField([('paragraph', 0), ('h2', 1), ('h3', 2), ('image', 3), ('embeded_media', 4), ('paragraph_with_image', 8)], blank=True, block_lookup={0: ('wagtail.blocks.RichTextBlock', (), {'template': 'site_app/blocks/paragraph.html'}), 1: ('wagtail.blocks.CharBlock', (), {'help_text': 'level 2 headings', 'max_length': 200, 'template': 'site_app/blocks/two_headings.html'}), 2: ('wagtail.blocks.CharBlock', (), {'help_text': 'level 3 headings', 'max_length': 200, 'template': 'site_app/blocks/three_headings.html'}), 3: ('wagtail.images.blocks.ImageBlock', [], {'template': 'site_app/blocks/image_full.html'}), 4: ('wagtail.embeds.blocks.EmbedBlock', (), {'help_text': 'embed media files like videos, social media posts/shares etc.', 'max_height': 400, 'max_length': 200, 'max_width': 700, 'template': 'site_app/blocks/embed_media.html'}), 5: ('wagtail.blocks.RichTextBlock', (), {'help_text': 'Add the text for this section', 'required': True}), 6: ('wagtail.images.blocks.ImageChooserBlock', (), {'help_text': 'Choose an image for this section', 'required': True}), 7: ('wagtail.blocks.BooleanBlock', (), {'default': True, 'help_text': 'Check this box to position the text on the left and the image on the right. Uncheck to reverse.', 'required': False}), 8: ('wagtail.blocks.StructBlock', [[('text', 5), ('image', 6), ('text_on_left', 7)]], {})}, null=True),
        ),
    ]
