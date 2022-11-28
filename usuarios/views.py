from django.shortcuts import render
from usuarios.models import usuario
from django.contrib import messages

# Create your views here.

def index(request):
    
    if(request.method == 'POST'):
        users= usuario.objects.filter(user = request.POST['user'])#Es lo mismo que select * from mensajes_mensaje where id = pk;
        print(users,"post")
        context = {
            'object_list' : users,
        }
        print(context)
        return render(request,'usuarios/index.html', context)
    
    users = usuario.objects.all() #Obtengo todos los registros de la tabla usuario
    context = {
        'object_list' : users
    }
    print(context)
    return render(request,'usuarios/index.html', context)

def deleteUser(request, pk ):
    usuario.objects.get(pk=pk).delete()
    messages.success(request,"°Successful user delete")
    return index(request)

def addUser(request):
    if request.method == 'POST':
        #print("Esta funcionando con post")
        user = request.POST['user']
        name = request.POST['name']
        sex = request.POST['sex']

        usuario.objects.create(
            user = user,
            name= name,
            sex = sex
        )
        #Guardo los cambios
        messages.success(request,"°Successful user add")
        return index(request)
    return render(request, 'usuarios/addUser.html')

def updateUser(request, pk):

    getuser = usuario.objects.get(pk = pk) #Es lo mismo que select * from mensajes_mensaje where id = pk;
    contexto = {
        'user': getuser.user,
        'name': getuser.name,
        'sex': getuser.sex
    }

    #Cuando se haga un método post

    if request.method == 'POST':
        #print("Esta funcionando con post")
        user = request.POST['user']
        name = request.POST['name']
        sex = request.POST['sex']

        getuser.user = user

        getuser.name = name

        getuser.sex = sex

        getuser.save() #Guardo los cambios
        messages.success(request,"°Successful user update")
        return index(request)

    return render(request, 'usuarios/updateUser.html', contexto)