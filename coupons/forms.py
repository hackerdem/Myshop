from django import forms

class CouponApplyForm(forms.Form):
    code=forms.CharField()
    def clean(self):
        cleaned_data=super(CouponApplyForm,self).clean()
        code=cleaned_data.get('code')