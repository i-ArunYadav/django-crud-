from django.shortcuts import render
from .models import Products,Items
# Create your views here.
def product(request):

	pro = Products.objects.all()
	
	
	return render(request,'demo.html',context ={'form':pro})

def items(request,pk=1):
	itm = Items.objects.filter(product = pk)
	return render(request, 'demo.html',context={'fm':itm})


def totalsum(request):
	if request.method == 'POST':
		id_list = request.POST.getlist("something")
		x = [i for i in id_list if i != ""]
		id_lis = request.POST.getlist("pricething")
		print(')))))))))))))))',id_list)
		print(')))))))))',id_lis)

		a= []
		b= []
	
		for i in id_list:
			a.append(int(i))
		for i in id_lis:
			b.append(int(i))

		total = 0
		for i in range(len(a)):
			total= total+a[i]*b[i]
		return render(request, 'totalsum.html', context = {'form': total})
