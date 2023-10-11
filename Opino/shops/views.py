from django.shortcuts import render, get_object_or_404
from .models import Post, Category, City, Country

# vista del home 
def home(request):
    countries = Country.objects.all()
    return render(request, "home.html", {'countries': countries})


def city_category(request, city_id, categoria_id):
    # Obtener la ciudad y la categoría específicas
    city = get_object_or_404(City, id=city_id)
    category = get_object_or_404(Category, id=categoria_id)

    # Filtrar los posts por ciudad y categoría
    posts = Post.objects.filter(ciudad_id_id=city, categoria_id=category)

    # Obtener todas las ciudades y categorías para mostrar en la plantilla
    cities = City.objects.all()
    categories = Category.objects.all()

    return render(request, "category.html", {'city': city, 
                                                  'category': category, 
                                                  'posts': posts, 
                                                  'cities': cities, 
                                                  'categories': categories})



# vista de cities
def city(request, country_id):
        country = get_object_or_404(Country, id=country_id)
          # Filtrar los posts por el país seleccionado
        posts_in_country = Post.objects.filter(pais=country)

        # Obtener las ciudades a partir de los posts
        cities = list(set(post.ciudad_id for post in posts_in_country))
       
        return render(request, "cities.html", {'country': country, 'cities': cities})



    

# vista de categorias
def choose_category(request, city_id):
    # Obtener la ciudad específica
    city = get_object_or_404(City, id=city_id)

    # Obtener todas las categorías disponibles
    categories = Category.objects.all()

    return render(request, "choose_category.html", {'city': city, 'categories': categories})



# vista del comercio individual 
def detail_post(request, post_slug, *args, **kwargs):
    post = get_object_or_404(Post, slug=post_slug)  # filtrando por slug
    return render(request, "post.html", {'post':post})


def contact(request):
    return render(request, "contact.html", {})



def privacy_policies(request):
    return render(request, "pdp.html", {})


def search(request):
    
    query = request.GET.get('q')  # Obtiene la consulta desde el formulario

    if query:
        # Realiza la búsqueda en tu modelo utilizando la consulta
        results = Post.objects.filter(nombre__icontains=query)
    else:
        results = []  # Si no hay consulta, muestra una lista vacía

    return render(request, 'search.html', {'results': results})