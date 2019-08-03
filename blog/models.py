from django.db import models
from django.shortcuts import render

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import MultiFieldPanel
from wagtail.core.models import Page , Orderable
from wagtail.admin.edit_handlers import FieldPanel,PageChooserPanel,StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.core.fields import RichTextField,StreamField
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.snippets.models import register_snippet
from streams import blocks
# Create your models here.

class BlogAuthorOrderable (Orderable):
    page = ParentalKey ("blog.BlogdetailPage", related_name = "Blog_Author")
    author = models.ForeignKey (
        "blog.BlogAuthor",
        on_delete = models.CASCADE,
    )
    panels = [
        SnippetChooserPanel("author")
    ]

class BlogAuthor (models.Model):
    name = models.CharField(max_length = 100)
    website = models.URLField (blank = True,null = False)
    image = models.ForeignKey (
        "wagtailimages.Image",
        on_delete = models.SET_NULL,
        null= True,
        blank = False,
        related_name="+",
    )
    panels = [
        MultiFieldPanel ([
            FieldPanel ("name"),
            ImageChooserPanel("image")
        ],heading = "Name and Image"),
    MultiFieldPanel (
        [
            FieldPanel("website")
        ],heading = "Links"
    ),
    ]
    def __str__ (self):
        return self.name
    class Meta : 
        verbose_name :"Blog Author"
        verbose_name_plural :"Blog Authors"

register_snippet (BlogAuthor)

class BlogListPage (RoutablePageMixin,Page) :
    template = "blog/blog_listing_page.html"
    custom_title = models.CharField(blank = False, null = False, max_length = 100,help_text = "Overwrites the default text")
    
    def get_context (self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context ["posts"] = BlogDetailpage.objects.live().public()
        
        return context
    content_panels = Page.content_panels + [
        FieldPanel ("custom_title")
    ]

    @route (r'^latest/$')
    def latest_blog_posts (self, request,*args,**kwargs):
        context = self.get_context (request,*args,**kwargs)
        context["latest_post"] = BlogDetailpage.objects.live().public()[:2]
        return render(request, 'blog/latest_posts.html',context)
    
    def get_sitemap_urls(self, request):
        sitemap = super().get_sitemap_urls(request)
        sitemap.append (
            {
                "location": self.full_url+self.reverse_subpage("latest_blog_post"),
                "lastmod" : (self.last_published_at or self.latest_revision_created_at) 
            }
        )
        return sitemap

    
class BlogDetailpage (Page) :
    template = "blog/blog_detail_page.html"
    custom_title = models.CharField(blank = False, null = False, max_length = 100,help_text = "Overwrites the default text") 
    blog_image = models.ForeignKey ("wagtailimages.Image",blank= False,null = True,related_name="+",on_delete = models.SET_NULL)
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichTextBLock()),
            ("simple_richtext", blocks.SimpleRichTextBLock()),
            ("cards", blocks.CardBlock()),
            ("CTABlock", blocks.CTABlok()),
        ],
        null= True,
        blank= True,
    )
    content_panels = Page.content_panels + [
        FieldPanel ("custom_title"),
        ImageChooserPanel ("blog_image"),
        StreamFieldPanel ("content")
    ]