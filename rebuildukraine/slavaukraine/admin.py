# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person
#from .models import Enterprise

from .models import Country
from .models import City
from .models import Expertise
from .models import Specialization
from .models import Proposal
from .models import Favorites
from .models import Registration

# Register your models here.
admin.site.register(Person)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Expertise)
admin.site.register(Specialization)
#admin.site.register(Enterprise)
admin.site.register(Proposal)
admin.site.register(Favorites)
admin.site.register(Registration)

class PersonAdmin(UserAdmin):
    list_display = ('email', 'last_login', 'is_admin','is_staff','is_enterprise','is_person')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter =()
    fieldsets = ()

admin.site.unregister(Person)
admin.site.register(Person, PersonAdmin)

class EnterpriseAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin','is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

#admin.site.unregister(Enterprise)
#admin.site.register(Enterprise, EnterpriseAdmin)