from django.db import models
from django.shortcuts import render

from streams import blocks
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel,PageChooserPanel,StreamFieldPanel,InlinePanel,MultiFieldPanel
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField,StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePage, route

class HomePageCarouselImages (Orderable):
    page = ParentalKey("home.HomePage", related_name = "Image_Carousel") 
    carosuel_images = models.ForeignKey (
        "wagtailimages.Image",
        null = True,
        blank =False,
        on_delete =models.SET_NULL,
        related_name="+"
    )
    panels = [ 
        ImageChooserPanel("carosuel_images")
    ]
class HomePage(RoutablePage, Page):
    templates = "templates/home/home_page.html"

    banner_title = models.CharField(max_length = 100, blank= False, null= True)
    banner_subtitle = RichTextField (features = ["bold", "italic"])
    banner_image = models.ForeignKey (
        "wagtailimages.Image",
        null = True,
        blank =False,
        on_delete =models.SET_NULL,
        related_name="+"
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null = True,
        blank = True,
        on_delete =models.SET_NULL,
        related_name="+"
    )
    max_count=1
    content = StreamField(
        [
            ("CTABlock", blocks.CTABlok()),
        ],
        null= True,
        blank= True
    )
    content_panels = Page.content_panels + [
        MultiFieldPanel ([
            FieldPanel ("banner_title"),
            FieldPanel ("banner_subtitle"),
            ImageChooserPanel ("banner_image"),
            PageChooserPanel("banner_cta"),
        ],heading = "Banner Options"),
        StreamFieldPanel("content"),
        MultiFieldPanel([
            InlinePanel("Image_Carousel", max_num=5,min_num=1,label= "Add Image"),
        ],heading = "Carosel Images")
    ]
    class Meta: 
        verbose_name = " Home Page "
        verbose_name_plural = "Home Pages"

    @route(r'^subscribe/$')
    def the_subscribe_page (self, request,*args,**kwargs):
        context = self.get_context (request,*args, **kwargs)
        context ['a_special_test'] = "Hello World!!!"
        return render (request, "home/subscribe.html",context)
