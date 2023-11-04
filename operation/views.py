from django.shortcuts import render

from django.views.generic import View
from operation.forms import OperationForm

# Create your views here.
class AddView(View):
    def get(self,request,*args,**kwargs):
        form=OperationForm()
        return render(request,"add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=OperationForm(request.POST)
        if form.is_valid():
            
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            res=n1+n2
            return render(request,"add.html",{"result":res,"form":form})
        else:
             return render(request,"add.html",{"form":form})