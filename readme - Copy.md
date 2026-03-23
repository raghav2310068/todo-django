# Advantages of django:
    1. open source so every problem can be solved by a numbe of contributers
    2. get admin pannel already built so need to build again and again
    3. admin panel is well structured 
    4. permission and authentication
    5. DRY (dont repeat yourself) avoid unnecessary line of code
    6. Scaling can be handel by django 
    7. good documentation with example code

# creating a django project :
    START WITH THE : 
    " django-admin startproject project_name "

## run django project 
    " python manage.py run server " 

# file structure 
    1. manage.py --> very important, command line utility that allow us to interact with project in many ways for example:
        a. to run deployment server we use " python manage.py run server "
        b. creating a new app we use " python manage.py startapp app_name "
        c. to create a super user we use " python manage.py createsuperuser "
        # NEVER EDIT django.py UNTIL YOU BECOME A DJANGO EXPERT
    
    2. db.sqlite3 --> usually replaced with mysql and postgres
    3. __init__.py --> we dont have to do anything with this file . we import a model from one module to another module happens because of this __init__.py file
    4. wsgi.py --> helps in dealing with the web server gateway interface it can thought of how a interface interact with servr
    5. asgi.py:-  asynchrounous gateway interface we are not changing anything here 
    6. urls.py -> contains all the endpoints that we have for our webpage if a user comes with this url redirect to that page
    7. setting.py --> 

# IMPORTANT POINTS TO REMEMBER :
    1. secret key should not be visible to anybody
    2. in settings.py debug should be set to false when we deploy 
    3. allowed host me domain name 
    4. whenever an app is created in the project we must register it in the installed app section in settings.py
    5. template is responsible for rendering the template 
    6. whatever css javascript and images we use are in static so we have to add it 
    
# in order to add static file that are css javascript and images we use few settings in the settings.py that are :
    1. STATIC_ROOT=BASE_DIR/static
    2. STATICFILES_DIRS=[]

# data base ke lie 
    1. sbse phele nya app bnao using "python .\manage.py startapp employee"
    2. isme ke model.py file m class bnao and model.model inherit kro and then jo bnana h bna lo 
    3. run "python manage.py makemigrations"
    4. run "python manage.py migrate
    5. fir us app ke admin m jake register krna hota h

# media file ke lie 
    urls.py ke ander 
        <!-- 
        from django.conf import settings 
        from django.conf.urls.static import static
        -->
        and last me "+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        "
    
    settings.py ke ander
        <!--
        # media files configuration 
        MEDIA_URL="/media/"
        MEDIA_ROOT=BASE_DIR/"media"
        -->

# backend se text ko frontend p bhejne k lie 
    1. model.object.all()
    2. context dictonary bnao 
        <!--
        context={
            "model_name":model_name
        }
          -->
    3. function ke ander call krdo
    4. fir html file ke ander jake u can use template tags to use for if while commands 
    

# list display can be used to add other data in the admin pannel and is done inside app/admin.py under a class 
    <
    class TaskAdmin(admin.ModelAdmin):
    list_display=["task","is_complete","created_at","updated_at"]
    search_fields=["task"]
    list_filter=["is_complete","created_at","updated_at"]
    >

<!-- {%csrf_token%} SHOULD BE ADDED JUST BEFORE JUST AFTER POST OPEN TAG WITH POST REQUST SO THAT WE CAN PREVENT FORGERY -->