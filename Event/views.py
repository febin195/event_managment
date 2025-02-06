from django.shortcuts import render
from django.views.generic import View
from Event.forms import EventForm
from Event.models import EventModel

class AddEvent(View):
    def get(self,request):
        form=EventForm()
        return render(request,'add.html',{'form':form})
    

    def post(self,request):
        form=EventForm(request.POST)

        if form.is_valid():
            EventModel.objects.create(**form.cleaned_data)
        form=EventForm()    
        return render(request,'add.html',{'form':form})
    



class EventDetails(View):
    def get(self,request):
        data=EventModel.objects.all()
        return render(request,'Event_info.html',{'data':data})    
    


class EventUpdate(View):
    def get(self,request,**kwargs):
        id=kwargs.get('pk') 
        data=EventModel.objects.get(id=id)

        form=EventForm(instance=data)
        return render(request,'update.html',{'form':form})

    def post(self,request,**kwargs):
        id=kwargs.get('pk') 
        data=EventModel.objects.get(id=id)

        form=EventForm(request.POST,instance=data)

        if form.is_valid():
            form.save()

        return render(request,'Event_info.html')




class EventDelete(View):
     def get(self,request,**kwargs):
        id=kwargs.get('pk') 
        EventModel.objects.get(id=id).delete()
        return render(request,'Event_info.html')



