from django.shortcuts import redirect, render
from vehicle.models import Vehicle,Users
from django.views.generic import CreateView,FormView,ListView,UpdateView,View
from django.urls import reverse_lazy
from vehicle.forms import RegistrationForm,LoginForm,VehicleForm
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import user_passes_test  ##for authentication of dfferent users

# Create your views here.
def signin_required(fn):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            # messages.error("you must log in")
            return redirect("signin")
        else:
            return fn(request, *args, **kwargs)
    return wrapper

def suadmin_required(user):

    return user.is_authenticated and user.options in ('SA')

def admin_suadmin_required(user):

    return user.is_authenticated and user.options in ('SA','A')

decs=[signin_required,never_cache]
sdecs=[signin_required,never_cache,user_passes_test(suadmin_required)]
asdecs=[signin_required,never_cache,user_passes_test(admin_suadmin_required)]



class SignupView(CreateView):
    model = Users
    form_class=RegistrationForm
    template_name="register.html"
    success_url= reverse_lazy("signin")

class SigninView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self, request, *args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("home")
            else:
                return render(request,self.template_name,{"form":form})

#all users
@method_decorator(decs,name="dispatch")   
class IndexView(ListView):
    model=Vehicle
    form_class=VehicleForm
    template_name="home.html"
    context_object_name="vehicle"
    success_url=reverse_lazy("home")

    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        vehicle=Vehicle.objects.all()
        context['vehicle']=vehicle
        users=Users.objects.all()
        context['users']=users
        return context
    
@method_decorator(decs,name="dispatch")   
class VehicleRegistrationView(CreateView):
    template_name="vehicleregistration.html"
    form_class=VehicleForm
    model=Vehicle
    context_object_name="vehicle"
    success_url=reverse_lazy("home")

    def form_valid(self,form ):
        form.instance.user=self.request.user
        print("new vehicle added")
        return super().form_valid(form)

##admin and superadmin    
@method_decorator(asdecs,name="dispatch")
class VehicleUpdateView(UpdateView):
    model=Vehicle
    form_class=VehicleForm
    template_name="vehicleupdate.html"
    pk_url_kwarg="id"
    success_url=reverse_lazy("home")

#superadmin
@method_decorator(sdecs,name="dispatch")
class VehicleDeleteView(View):
    def get(self,request,*args,**kwargs):
        v_id=kwargs.get("id")
        obj=Vehicle.objects.filter(id=v_id)
        obj.delete()
        return redirect("home")

def signout_view(request, *args, **kwargs):
    logout(request)
    print("signout successfully")
    return redirect("signin")
    

    






