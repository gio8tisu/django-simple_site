import random

from django.http import HttpResponse
from django.template import loader


IMAGES = {  # {title: image}
    "Italian Trulli": "pic_trulli.jpg",
    "Girl in a jacket": "img_girl.jpg",
    "Flowers in Chania": "img_chania.jpg",
}


def index(request):
    title = random.choice(list(IMAGES.keys()))
    image = IMAGES[title]

    template = loader.get_template("index.html")
    context = {"title": title, "image": image}
    return HttpResponse(template.render(context, request))
