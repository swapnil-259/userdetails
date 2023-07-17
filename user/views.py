from django.http import JsonResponse
from .models import Register_user, todo
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpRequest
from django.utils import timezone
import json

def registeruser(request):
    if request.method == 'POST':
        user_data = json.loads(request.body) 
        First_Name = user_data['First_Name']
        Last_Name =user_data['Last_Name']
        Email = user_data['Email']
        Gender = user_data['Gender']
        Address = user_data['Address']
        Stay = user_data['Stay']
        Password = user_data['Password']
        Confirm_pass = user_data['Confirm_pass']
        hashed_password = make_password(Password)
        hashed_Confirmpass = make_password(Confirm_pass)
        if Password!= Confirm_pass:
            return JsonResponse({'message':'password and confirm password should be same'})
        duplicate_email = Register_user.objects.filter(Email=Email).first()
        if duplicate_email:
            return JsonResponse({'message':'Email is already exist'})
        else:
         user= Register_user(
               First_Name=First_Name,
               Last_Name=Last_Name,
               Email=Email,
               Gender=Gender,
               Address=Address,
               Stay=Stay,
               Password=hashed_Confirmpass
           )
       
        user.save()
        return JsonResponse({'message':'connected'})
  
def loginuser(request):
   if request.method == 'POST':
         logindata = json.loads(request.body)
         LogEmail = logindata['LogEmail']
         LogPassword = logindata['LogPassword']
         loghashed_password = make_password(LogPassword)
        #  user = User_Register.objects.get(Email=LogEmail)

        
         user = Register_user.objects.filter(Email=LogEmail).first()
         if user is None:
             return JsonResponse({'message':'email do not exist'})
         else:
           if check_password(LogPassword, user.Password):
                 
                    user.Status = "LI"
                    idname = user.id
                    user.save()
                    return JsonResponse({'message':'logged in','user_id':idname})
           else:
                 return JsonResponse({'message':'incorrect password'})
         
def logoutuser(request):
     if request.method =='POST':
          logoutdata = json.loads(request.body)
          LogoutEmail =  logoutdata['LogoutEmail']

          user = Register_user.objects.filter(Email=LogoutEmail).first()
          if user is None:
               return JsonResponse({'message':'email do not exist'})

          else:
             if user.Status=="LI":
               user.Status ="LO"
               user.save()
               return JsonResponse({'message':'User logged out'})
             else:
               return JsonResponse({'message':'user not logged in '})

def createtask(request:HttpRequest):
    if request.method == 'POST':
        add_task = json.loads(request.body)
        Data = add_task.get("Data")
        user_id = add_task.get("user_id")
        # if user_id =="":
        #  user3 = 'Blank'
        # else:
        user = Register_user.objects.filter(id = user_id).first()
        if user is None:
            return JsonResponse({'message':'First logged in please'}) 
        else: 
            if user is not None:
            
             add_task_in_db  = todo(
                Task = Data,
                Identity_id = user.id,
              )
             add_task_in_db.save()
             return JsonResponse({'message':'Task added','task_no':add_task_in_db.Entryno})
            
    elif request.method == 'GET':
        #  give_task = request.query_params.getlist
        #  query_params = request.GET
         user_id =  request.GET.get("user_id")
        #  user_id = '7'
         user = Register_user.objects.filter(id = user_id).first()
         if user:
          tasks = todo.objects.filter(Identity_id =user_id, DeleteTask = '0').values('Entryno','Task')
          tasklist = list(tasks)
          return JsonResponse(tasklist, safe=False)
         else:
             return JsonResponse({'message':'user do not exist'})
         

    elif request.method =='PUT':
            change_data = json.loads(request.body)
            # user_id = change_data.get("user_id")
            updatetask=change_data.get("Edit")
            edit_Task_no = change_data.get("Task_no")
            cmplt_task_no = change_data.get("cmplt_task_no")
          
            # user = Register_user.objects.filter(id = user_id).first()
            # if user:
            if updatetask != "":
                task_edt = todo.objects.filter(Entryno = edit_Task_no)
                if task_edt:
                     task_edt.update(Task = updatetask, UpdateTask = True, Updatetime = timezone.now())
                     return JsonResponse({'message':'task updated!!'})
                else:
                    return JsonResponse({'message':'task not found'})
                
            elif cmplt_task_no != "":
                task_cmplt = todo.objects.filter(Entryno = cmplt_task_no)
                if task_cmplt:
                    task_cmplt.update(CompleteTask = True, Completetime = timezone.now())
                    return JsonResponse({'message':'task completed!!'})
                else:
                 return JsonResponse({'message':'task not found'})
            else:
                return JsonResponse({'message':'please enter task number'})
            # else :
                # return JsonResponse({'message':'user do not logged in'})
    elif request.method =='DELETE':
           
            # delete_data = json.loads(request.body)
            # user_id = delete_data.get("user_id")
            dlt_task_no = request.GET.get("dlt_task_no")
            # tasks = Register_user.objects.filter(id = user_id).first()
            # if tasks:
            if dlt_task_no !="":
               task_dlt = todo.objects.filter(Entryno = dlt_task_no)
               if task_dlt:
                  task_dlt.update(DeleteTask = True, Deletetime = timezone.now())
                  return JsonResponse({'message':'task deleted'})
               
               else:
                 return JsonResponse({'message':'task  not found'})
            else:
                 return JsonResponse({'message':'please enter task number'})
            # else:
                # return JsonResponse({'message':'user do not exist'})