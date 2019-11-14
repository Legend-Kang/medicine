from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo, pillinformation
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from pill_detection import pilldetect



# Create your views here.

def base(request):

    return render(request, 'base.html')

class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo']
    template_name = 'upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            print(form)
            print(self)
            return redirect('photo:output')
        else:
            return self.render_to_response({'form':form})



def Output(request):

    pillinfo = pilldetect.main()

    pill = pillinformation.objects.filter(shape=pillinfo[0] , char=pillinfo[1], color=pillinfo[2])

    return render(request, 'output.html', {'pill': pill})



# class PhotoDeleteView(DeleteView):
#     model = Photo
#     success_url = '/'
#     template_name = 'delete.html'
#
# class PhotoUpdateView(UpdateView):
#     model = Photo
#     fields = ['photo']
#     template_name = 'update.html'


