
from rest_framework.views import APIView
from .serializers import FoodSerializers
from .serializers import CropFooderializers
from django.http.response import JsonResponse
from .models import Food
from .models import Crops
from django.http.response import Http404
from rest_framework.response import Response

# Create your views here.
class FoodView(APIView):
    

    def get_food(self,pk):
        try:
            food = Crops.objects.get(CropId=pk)
            return food
        except Crops.DoesNotExist():
            raise Http404
        
    def get(self,response,pk=None):
        if pk:
            data = self.get_food(pk)
            ser = CropFooderializers(data)
        else:
            data = Crops.objects.all()
            ser = CropFooderializers(data,many = True)
        return Response(ser.data)
    
    def post(self,request):
        data = request.data
        ser = CropFooderializers(data=data)

        if ser.is_valid():
            ser.save()
            return JsonResponse("Food added successfully",safe=False)
        return JsonResponse("Failed to create",safe=False)
    
    def put(self,request,pk=None):
        foodtoup = Crops.objects.get(CropId=pk)
        ser = CropFooderializers(instance=foodtoup,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return JsonResponse("Food updated",safe=False)
        return JsonResponse("Failed",safe=False)
    
    def delete(self,request,pk=None):
        foodtodel = Crops.objects.get(CropId=pk)
        foodtodel.delete()
        return JsonResponse("deleted successfully",safe=False)


            


