"""
To render html web pages
"""

from django.http import HttpResponse
import random
from articles.models import Article
from django.template.loader import render_to_string, get_template



def home_view(request, *args, **kwargs):
    # take in a request (Django sends request)
    # return html as a response ( We pick to retrun the response)


    num = random.randint(1,5)
    name = 'Louis'
    article_obj = Article.objects.get(id=num)
    article_queryset = Article.objects.all()
    


    context = {
        "object_list":article_queryset,
        "object":article_obj,
        "title":article_obj.title,
        "id": article_obj.id,
        "content":article_obj.content
    }


    #Django Templates
    #method 2
    # tmpl = get_template("home-view.html")
    # tmpl_string = tmpl.render(context=context)

    HTML_STRING = render_to_string("home-view.html",context=context)
    # HTML_STRING = """
    # # <h1>{title} - id:{id}</h1>
    # # <p>{content}!<p> 
    # """.format(**context)




    return HttpResponse(HTML_STRING)