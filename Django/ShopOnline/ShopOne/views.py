from django.db.models.aggregates import Count
from django.http import request
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import products,contact,checkout_info,shop_tracker
import  json


def navview(request):
    return render(request, "shop/Nav.html")


def imageview(request):
    rk = {"range": range(9), "num": 9}
    return render(request, "shop/img.html", rk)
    # return render(request, 'shop/img.html',{'data':data})

def contactview(request):
    if (request.method == "POST"):
        print(request)
        print("printed")
    else:
        print("Not request")
    return render(request,'shop/contact.html')
    
def aboutview(request):
    return render(request,'shop/about_us.html')

def feedbackview(request):
    if (request.method == "POST"):
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        print(name)
        print(email)
        print(desc)
        print("Feedback printed")

        add_db_contact = contact(contact_name=name,contact_email = email,contact_desc = desc)
        add_db_contact.save()
    else:
        print("Not request")
    return render(request,'shop/feedback.html')


def checkout_feedbackview(request):
    if (request.method == "POST"):
        checkout_json = request.POST.get("checkout_json")
        name = request.POST.get("checkout_name")
        email = request.POST.get("checkout_email")
        phone = request.POST.get("checkout_phone")
        address = request.POST.get("checkout_address")
        zip_code = request.POST.get("checkout_zip_code")
        print(name)
        print(email)
        print("Feedback printed")

        checkout = checkout_info(checkout_name=name,checkout_email = email,checkout_phone = phone,checkout_address=address,checkout_zip_code=zip_code,checkout_json =checkout_json )
        checkout.save()
        id = checkout.checkout_id
        info = {
        'name':name,
        'tracker_id':id,
        }


    else:
        print("Not request")
    return render(request,'shop/checkout_feedback.html',info)
    
def homeview(request):
    prods = products.objects.all()
    category_list = set()

    categories = products.objects.values('category')

    for i in categories:
        cat_val = i['category']
        category_list.add(cat_val)
    
    car_length = len(category_list)
    rk = {"product": prods, "range": range(car_length),'all_cats':category_list}
    return render(request, "shop/home.html", rk)


def pracview(request):
    prods = products.objects.all()
    category_list = set()

    categories = products.objects.values('category')

    for i in categories:
        cat_val = i['category']
        category_list.add(cat_val)
    
    car_length = len(category_list)
    rk = {"product": prods, "range": range(car_length),'all_cats':category_list}
    return render(request, "shop/prac.html", rk)

def productview(request,pr_id):
    product = products.objects.filter(product_id=pr_id)
    print(product)
    return render(request,"shop/product_view.html",{'product':product})


def cart_detailsview(request):
    prods = products.objects.all()

    return render(request,"shop/cart_details.html",{'product':prods})

def checkoutview(request):
    return render(request,"shop/checkout.html")


def orderview(request):
    checkout = checkout_info.objects.all()
    # print(checkout)
    for i in checkout:
        print(i.checkout_name)
        var = i.checkout_json
        print(i.checkout_json)

   

    return render(request,"shop/orders.html")


def trackerview(request):
    return render(request,'shop/tracker.html')


def tracker_responseview(request):
    myls = []
    mydesc = []
    if request.is_ajax():
        tr_id = request.POST.get('tr_id')
        tr_email = request.POST.get('tr_email')
        if tr_id != '' and tr_email != '':
            print(tr_id,tr_email)
            checkout = checkout_info.objects.all()
            for i in checkout:
                myls.append(i.checkout_email)
            print(myls)

            if tr_email in myls:
                tr_info = shop_tracker.objects.filter(tracker_id = tr_id) 
                if(tr_info):
                    for i in tr_info:
                        temp = [i.tracker_desc,i.tracker_date]
                        print(i.tracker_desc)
                        print(i.tracker_date)
                        # print(json.dumps(temp))
                        mydesc.append(temp)
                    msg = 1


                else:
                    print("Not valid email")
                    msg = 0
                    mydesc = ['Invalid Tracker Id Or email']


              
        response = {
            'msg':msg,
            'desc':mydesc
        }
        print(mydesc)
        return JsonResponse(response)














    # cats = []
    # print("categories list",cats)


    # category_wised_prods = []
    # print('category_wised_product list',category_wised_prods)


    # prods = products.objects.all()
    # categories = products.objects.values("category")
    # print('Main categories',categories)


    # for item in categories:
    #     cats.append(item["category"])

    # for i in cats:
    #     cat_prod = products.objects.filter(category=i)
    #     category_wised_prods.append(
    #         [
    #             cat_prod,
    #         ]
    #     )
        # print(count, "no ")
        # print(cat_prod)
        # print(count, "no")

    # length = len(cat_prod)
    # rk = {"product": category_wised_prods,'catg':cats}
    # rk = {"product": cat_prod, "range": range(length)}
    # return render(request, "shop/prac.html", rk)



# codes 
# def pracview(request):
#     cats = []
#     prods = products.objects.all()
#     categories = products.objects.values("category")
#     for item in categories:
#         print(item)
#         cats.append(item["category"])


#  -->categories = products.objects.values("category")
# it returns ,
# <QuerySet [{'category': 'Electronics'}, {'category': 'Food'}, {'category': 'Bike'}, {'category': 'Electronics'}, {'category': 'Electronics'}, {'category': 'Clothes'}, {'category': 'watch'}, {'category': 'Electronics'}]>
# but we need,only the categories,like electronics,food

# so we will loop in this querysset, 
# -->for item in categories:
# -->print(item)
# it will print this below
# {'category': 'Electronics'}
# {'category': 'Food'}
# {'category': 'Bike'}
# {'category': 'Electronics'}
# {'category': 'Electronics'}
# {'category': 'Clothes'}
# {'category': 'watch'}
# {'category': 'Electronics'}

# it returns  some key value pair
# as we named those dictionary as item,
# we will simply append the values of dictionary ,in a list

# like

# listt.append(item['category'])

