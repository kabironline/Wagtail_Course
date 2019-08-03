from django.db import models

from streams import blocks

from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
# Create your models here.
class FlexPage (Page):
    template = "flex/flex_page.html"
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichTextBLock()),
            ("simple_richtext", blocks.SimpleRichTextBLock()),
            ("cards", blocks.CardBlock()),
            ("CTABlock", blocks.CTABlok()),
            ("Button_Block", blocks.ButtonBlock()),
        ],
        null= True,
        blank= True
    )
    subtitle = models.CharField (max_length = 100, null = True,blank = True)

    content_panels = Page.content_panels + [
        FieldPanel ("subtitle"),
        StreamFieldPanel("content"),
    ]

    class Meta: 
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
