from django.shortcuts import render

from .models import Pizza, PizzaChoice


def index_page(request):
    context = {
        'index_nav_active': 'active',
        'pizzaChose': PizzaChoice.objects.filter(client_ip=get_client_ip(request)).count(), # Does user selects some pizza for order?
    }
    return render(request, "pizza_app/index.html", context)


def about_page(request):
    context = {
        'about_nav_active': 'active',
        'pizzaChose': PizzaChoice.objects.filter(client_ip=get_client_ip(request)).count(),  # Does user selects some pizza for order?
    }
    return render(request, "pizza_app/about.html", context)


def store_page(request):
    context = {
        'store_nav_active': 'active',
        'pizzaChose': PizzaChoice.objects.filter(client_ip=get_client_ip(request)).count(),  # Does user selects some pizza for order?
    }
    return render(request, "pizza_app/store.html", context)


def product_page(request):    
    context = {
        'pizzas': Pizza.objects.all(),
        'product_nav_active': 'active',
        'pizzaChose': PizzaChoice.objects.filter(client_ip=get_client_ip(request)).count(),  # Does user selects some pizza for order?
    }
    return render(request, "pizza_app/products.html", context)

def order_page(request):
    # Does user selects some pizza for order?
    pizza_chose = PizzaChoice.objects.filter(client_ip=get_client_ip(request))
    context = {
        'pizzaChoses': pizza_chose,
        'order_nav_active': 'active',
    }
    return render(request, "pizza_app/order.html", context)
    

def pizza_choice(request):
    """ Ajax request for choosing pizza to make order """
    # Post data grab
    pizza_id  = request.POST['pizzaID']
    size      = request.POST['pizzaSize']
    quantity  = request.POST['pizzaQuantity']
    client_ip = get_client_ip(request)
    print(pizza_id, quantity, size, client_ip)
    
    pizza = Pizza.objects.get(id=pizza_id)
    size_wise_price = {
        'regular': pizza.current_regular_pizza_price,
        'big'    : pizza.current_big_pizza_price,
        'small'  : pizza.current_small_pizza_price,
    }
    name = pizza.name
    price = (int(quantity)*int(size_wise_price[size]))
    equation = "{} X {} = {}.00".format(quantity, size_wise_price[size], price)
    
    try:
        temporary_select = PizzaChoice(name=name,
                            size = size,
                            quantity = quantity,
                            equation = equation,
                            price = price,
                            client_ip = client_ip,)
        temporary_select.save()
    except:
       print("Error occurs while submitting data.")
    context = {
        'order_nav_active': 'active',
        'pizzaChose': PizzaChoice.objects.filter(client_ip=get_client_ip(request)).count(),
    }
    return render(request, "pizza_app/order.html", context)

    
def get_client_ip(request):
    """ User's ip address grabing for processing order """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

    
def remove_pizza_chose(request):
    """ Removing pizza from cart """
    cart_id  = request.POST['id']
    client_ip = get_client_ip(request)
    
    pizza = PizzaChoice.objects.get(client_ip=client_ip, id=cart_id)
    try:
        pizza.delete()
        print("Delete Seccessful.")
    except:
        print("Delete unseccessful.")
    
    return render(request, "pizza_app/order.html")
    
    
    
    
    
    
    
    
    
    
    
    
    