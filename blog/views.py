import datetime

from django.views.generic import TemplateView
from blog.models import Blog, Author
from django.http import Http404

author = Author(
    name='Harvard milan',
    image='/static/img/blog/author.png'
)

blogs = [
    Blog(
        pk=1,
        image='/static/img/blog/single_blog_1.png',
        title='Google inks pact for new 35-storey office',
        preview='Second divided from form fish beast made every of seas all gathered us saying he our',
        category='Travel, Lifestyle',
        text='''<p class="excert">
                        MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                        should have to spend money on boot camp when you can get the MCSE study materials yourself at a
                        fraction of the camp price. However, who has the willpower
                     </p>
                     <p>
                        MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                        should have to spend money on boot camp when you can get the MCSE study materials yourself at a
                        fraction of the camp price. However, who has the willpower to actually sit through a
                        self-imposed MCSE training. who has the willpower to actually
                     </p>
                     <div class="quote-wrapper">
                        <div class="quotes">
                           MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                           should have to spend money on boot camp when you can get the MCSE study materials yourself at
                           a fraction of the camp price. However, who has the willpower to actually sit through a
                           self-imposed MCSE training.
                        </div>
                     </div>
                     <p>
                        MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                        should have to spend money on boot camp when you can get the MCSE study materials yourself at a
                        fraction of the camp price. However, who has the willpower
                     </p>
                     <p>
                        MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                        should have to spend money on boot camp when you can get the MCSE study materials yourself at a
                        fraction of the camp price. However, who has the willpower to actually sit through a
                        self-imposed MCSE training. who has the willpower to actually
                     </p>''',
        author=author,
        date=datetime.date(year=2023, month=1, day=1)
    ),
    Blog(
        pk=2,
        image='/static/img/blog/single_blog_2.png',
        title='Google inks pact for new 35-storey office',
        preview='Second divided from form fish beast made every of seas all gathered us saying he our',
        category='Travel, Lifestyle',
        text='''<p class="excert">
                    MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                    should have to spend money on boot camp when you can get the MCSE study materials yourself at a
                    fraction of the camp price. However, who has the willpower
                 </p>
                 <p>
                    MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                    should have to spend money on boot camp when you can get the MCSE study materials yourself at a
                    fraction of the camp price. However, who has the willpower to actually sit through a
                    self-imposed MCSE training. who has the willpower to actually
                 </p>
                 <div class="quote-wrapper">
                    <div class="quotes">
                       MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                       should have to spend money on boot camp when you can get the MCSE study materials yourself at
                       a fraction of the camp price. However, who has the willpower to actually sit through a
                       self-imposed MCSE training.
                    </div>
                 </div>
                 <p>
                    MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                    should have to spend money on boot camp when you can get the MCSE study materials yourself at a
                    fraction of the camp price. However, who has the willpower
                 </p>
                 <p>
                    MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                    should have to spend money on boot camp when you can get the MCSE study materials yourself at a
                    fraction of the camp price. However, who has the willpower to actually sit through a
                    self-imposed MCSE training. who has the willpower to actually
                 </p>''',
        author=author,
        date=datetime.date(year=2023, month=1, day=15)
    ),
    Blog(
        pk=3,
        image='/static/img/blog/single_blog_3.png',
        title='Google inks pact for new 35-storey office',
        preview='Second divided from form fish beast made every of seas all gathered us saying he our',
        category='Travel, Lifestyle',
        text='''<p class="excert">
                    MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                    should have to spend money on boot camp when you can get the MCSE study materials yourself at a
                    fraction of the camp price. However, who has the willpower
                 </p>
                 <p>
                    MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                    should have to spend money on boot camp when you can get the MCSE study materials yourself at a
                    fraction of the camp price. However, who has the willpower to actually sit through a
                    self-imposed MCSE training. who has the willpower to actually
                 </p>
                 <div class="quote-wrapper">
                    <div class="quotes">
                       MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                       should have to spend money on boot camp when you can get the MCSE study materials yourself at
                       a fraction of the camp price. However, who has the willpower to actually sit through a
                       self-imposed MCSE training.
                    </div>
                 </div>
                 <p>
                    MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                    should have to spend money on boot camp when you can get the MCSE study materials yourself at a
                    fraction of the camp price. However, who has the willpower
                 </p>
                 <p>
                    MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                    should have to spend money on boot camp when you can get the MCSE study materials yourself at a
                    fraction of the camp price. However, who has the willpower to actually sit through a
                    self-imposed MCSE training. who has the willpower to actually
                 </p>''',
        author=author,
        date=datetime.date(year=2023, month=1, day=20)
    ),
    Blog(
        pk=4,
        image='/static/img/blog/single_blog_4.png',
        title='Google inks pact for new 35-storey office',
        preview='Second divided from form fish beast made every of seas all gathered us saying he our',
        category='Travel, Lifestyle',
        text='''<p class="excert">
                    MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                    should have to spend money on boot camp when you can get the MCSE study materials yourself at a
                    fraction of the camp price. However, who has the willpower
                 </p>
                 <p>
                    MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                    should have to spend money on boot camp when you can get the MCSE study materials yourself at a
                    fraction of the camp price. However, who has the willpower to actually sit through a
                    self-imposed MCSE training. who has the willpower to actually
                 </p>
                 <div class="quote-wrapper">
                    <div class="quotes">
                       MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                       should have to spend money on boot camp when you can get the MCSE study materials yourself at
                       a fraction of the camp price. However, who has the willpower to actually sit through a
                       self-imposed MCSE training.
                    </div>
                 </div>
                 <p>
                    MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                    should have to spend money on boot camp when you can get the MCSE study materials yourself at a
                    fraction of the camp price. However, who has the willpower
                 </p>
                 <p>
                    MCSE boot camps have its supporters and its detractors. Some people do not understand why you
                    should have to spend money on boot camp when you can get the MCSE study materials yourself at a
                    fraction of the camp price. However, who has the willpower to actually sit through a
                    self-imposed MCSE training. who has the willpower to actually
                 </p>''',
        author=author,
        date=datetime.date(year=2023, month=3, day=1)
    )
]


class BlogView(TemplateView):
    template_name = 'blog.html'
    extra_context = {
        'bradcam': 'blog',
        'blogs': blogs
    }


class BlogSingleView(TemplateView):
    template_name = 'single-blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        if pk:
            try:
                blog = next(filter(lambda bl: bl.pk == pk, blogs))
                context['blog'] = blog
                context['bradcam'] = blog.title
            except StopIteration:
                raise Http404

        return context
