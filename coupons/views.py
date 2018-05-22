from django.shortcuts import render

from django.shortcuts import render,redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Coupon
from .forms import CouponApplyForm

@require_POST
def coupon_apply(request):
    now=timezone.now()
    form=CouponApplyForm(request.POST)
    #print(form)
    if form.is_valid():
        print('form is valid')
        code=form.cleaned_data['code']
        print(code,'code')
        try:
            #----- CHECK VALID FIELDS FOR TIMEZONE DIFFREERNCE-----##########
            """valid_from__gte=now, @@@@@@@@@@@@@@@ there is a problem on time formating logic not working@@@@@@@@@2
                                      valid_to__lte=now,"""
            coupon=Coupon.objects.get(code__iexact=code,
                                      
                                      active=True,
                                    )
            print(coupon)
            request.session['coupon_id']=coupon.id  
        except Coupon.DoesNotExist:
            request.session['coupon_id']=None
    print(request.session['coupon_id'])
    return redirect('cart:cart_detail')