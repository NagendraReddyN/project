from django.contrib import admin
from.models import Child,Base2,Child2,Post,ProxyPost
class ChildAdmin(admin.ModelAdmin):
    list_display = ['prdid', 'prdname', 'price', 'category']
    
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    
admin.site.register(Child,ChildAdmin)
admin.site.register(Base2)
admin.site.register(Child2)
admin.site.register(Post,PostAdmin)
admin.site.register(ProxyPost)