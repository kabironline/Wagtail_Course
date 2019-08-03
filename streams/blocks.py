from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock (blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="add your text")
    text = blocks.TextBlock(required=True, help_text="Some More Text!!")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title and Text"

class CardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)."""

    title = blocks.CharBlock(required=True, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
            ]
        )
    )

    class Meta:  # noqa
        template = "streams/Staff_cards.html"
        icon = "placeholder"
        label = "Staff Cards"



class RichTextBLock (blocks.RichTextBlock):
    class Meta :
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "full richtext"

class SimpleRichTextBLock (blocks.RichTextBlock):
    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            'bold',
            'italic',
            'link',
        ]
    class Meta :
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "simple richtext"

class  CTABlok (blocks.StructBlock):
    title       = blocks.CharBlock(required=True,max_length=60)
    text        = blocks.RichTextBlock(required= True, features= ['bold','italic'])
    button_page = blocks.PageChooserBlock(required= False)
    button_url  = blocks.URLBlock (required= False)
    button_text = blocks.CharBlock(required= True,default = 'learn more',max_length=40)
    
    class Meta :
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"

class LinkStructValue (blocks.StructValue):
    def url(self):
        page = self.get('button_page')
        external_url = self.get('button_url')
        if button_page :
            return button_page.url
        elif button_url :
            return button_url
class ButtonBlock (blocks.StructBlock):
    button_page = blocks.PageChooserBlock(required= False)
    button_url  = blocks.URLBlock (required= False)

    def get_context(self, request , *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context ['latest_post'] = BlogDetailPage.objects.live().publish()[:3]
        return context

    class Meta :
        template = "streams/button_block.html"
        icon = "placeholder"
        label = "Call to Action"
        value_class = LinkStructValue