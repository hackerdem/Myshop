from django.shortcuts import render,get_object_or_404
from .models import Product,Size,Color,Room,Category,Image,Wishlist
from cart.forms import CartAddProductForm
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from cart.cart import Cart
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import ProductAddWishlistForm
from .forms import SearchForm
from haystack.query import SearchQuerySet


#404 error handling
###########################
def handler404(request, exception, template_name='404.html'):
    response=render_to_response('404.html',{},context_instance=RequestContext(request))
    response.status_code=404
    return response

@require_POST
def product_liked(request):
    print("I AM HERE")
    product_id=request.POST.get('id')
    if not request.user.is_authenticated:
        pass # change object attribute later
    else:
        action=request.POST.get('action')
        if product_id and action:
            try:
                product=Product.objects.get(id=product_id)
                if action=='like':
                    product.users_like.add(request.user)
                else:
                    product.users_like.remove(remove.user)
                return JsonResponse({'status':'ok'})
            except:
                pass
        return JsonResponse({'status':'ko'})

def size_color_room_filter(request,slug):
    
    products=Product.objects.order_by('-{}'.format(slug))
    products,paginator,features=pagination(request,products)
    return render(request,'shop/product/list.html',
                        {'products':products,
                        'paginator':paginator,
                        'features':features,
                        })
def product_list_by_feature(request,name,slug):
    cart=Cart(request)
    products=Product.objects.filter(**{slug:name.capitalize()}).order_by('-stock')
    products,paginator,features=pagination(request,products)
    return render(request,'shop/product/list.html',
                        {'products':products,
                        'paginator':paginator,
                        'features':features,
                        })
def product_list(request):
    cart=Cart(request)
    products=Product.objects.filter(available=True).order_by('-stock')
    products,paginator,features=pagination(request,products)
    return render(request,'shop/product/list.html',
                        {'products':products,
                        'paginator':paginator,
                        'features':features,
                        })
def product_most_viewed(request):
    products=Product.objects.filter(available=True).order_by('-number_of_click')
    products,paginator,features=pagination(request,products)
    return render(request,'shop/product/list.html',
                        {'products':products,
                        'paginator':paginator,
                        'features':features,
                        })
# FEATURED willl be added urls and function
def product_latest(request):
    products=Product.objects.order_by('-created')
    products,paginator,features=pagination(request,products)
    return render(request,'shop/product/list.html',
                        {'products':products,
                        'paginator':paginator,
                        'features':features,
                        })
def collection_shop_list(request):
    products=Product.objects.filter(available=True).order_by('-stock')
    products,paginator,features=pagination(request,products)

    return render(request,'shop/product/shop_list.html',
                        {'products':products,
                        'paginator':paginator,
                        'features':features,
                        })
def pagination(request,products):
    colors=Color.objects.all()
    sizes=Size.objects.all()
    rooms=Room.objects.all()
    category=Category.objects.all()
    paginator=Paginator(products,8)
    page=request.GET.get('page')
    features={'color':colors,'room':rooms,'size':sizes,'category':category}
    try:
        products=paginator.page(page)
    except PageNotAnInteger:
        products=paginator.page(1)
    except EmptyPage: 
        products=paginator.page(paginator.num_pages)
    return products,paginator,features


    

def product_detail(request,id,slug):
    
    product=get_object_or_404(Product,id=id,slug=slug,available=True)
    product.number_of_click=product.number_of_click+1
    product.save()
    cart_product_form=CartAddProductForm()
    return render(request,'shop/product/product_detail.html',{'product':product,'cart_product_form':cart_product_form})
"""@require_POST   
def product_liked_by_user(request):
    product_id=request.POST.get('id')
    action=request.POST.get('action')
    if product_id and action:
        try:
            product=Product.objects.get(id=product_id)
            if action=='like':
                product."""
@require_POST
def add_to_wishlist(request,product_id):
    if request.user.is_authenticated:
        existing_object=Wishlist.objects.filter(userid=request.user.id,productid=product_id)
        if not existing_object :
            new_wishlist_object=Wishlist()

            new_wishlist_object.save()
            new_wishlist_object.userid.add(request.user)
            new_wishlist_object.productid.add(product_id)

        else:
            existing_object.delete()
        return HttpResponse(status=204)

    else:
        return HttpResponse(status=204) #processed but returning content is unnecessary
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def post_search(request):
        form=SearchForm()
        if query in request.GET:
            form=SearchForm(request.GET)
            if form.is_valid():
                cd=form.cleaned_data
                results=SearchQuerySet().models(Product).filter(content=cd['query']).load_all()
                total_results=results.count()
        return render(request,
                    'shop/templates/search/search.html',
                    {'form':form,
                    'cd':cd,
                    'results':results,
                    'total_Results':total_results})

