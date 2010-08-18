from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail, object_list
from django.views.generic.date_based import archive_index
from django.views.generic.simple import direct_to_template

from package.models import Package
from package.views import add_package, edit_package, add_example, edit_example, ajax_package_list, update_package

urlpatterns = patterns("",
    url(
        regex   = r"^$",
        view    = object_list,
        name    = "packages",
        kwargs  = dict(
            queryset=Package.objects.select_related(),        
            )            
    ),
    
    url(
        regex   = r"^latest/$",
        view    = archive_index,
        name    = "latest_packages",
        kwargs  = dict(
            queryset=Package.objects.select_related(),     
            date_field='created'   
            )            
    ),
    
    
    url(
        regex   = '^add/$',
        view    = add_package,
        name    = 'add_package',
    ),    

    url(
        regex = '^(?P<slug>[-\w]+)/edit/$',
        view    = edit_package,
        name    = 'edit_package', 
    ),    
    
    url(
        regex = '^(?P<slug>[-\w]+)/fetch-data/$',
        view    = update_package,
        name    = 'fetch_package_data', 
    ),    

    url(
        regex = '^(?P<slug>[-\w]+)/example/add/$',
        view    = add_example,
        name    = 'add_example', 
    ),    
    
    url(
        regex = '^(?P<slug>[-\w]+)/example/(?P<id>\d+)/edit/$',
        view    = edit_example,
        name    = 'edit_example', 
    ),    
    
    url(
        regex = '^p/(?P<slug>[-\w]+)/$',
        view    = object_detail,
        name    = 'package',
        kwargs=dict(
            queryset=Package.objects.select_related(),
            template_name='package/package.html',
            )    
    ),    
    
    url(
        regex = '^ajax_package_list/$',
        view    = ajax_package_list,
        name    = 'ajax_package_list',
    ),        
        
)
