from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Member, ComitePoste, ComiteMembership, SurName, AcademicYear


class SurNameInline(admin.TabularInline):
    model = SurName
    extra = 0
    fields = ['value', 'is_prefered']


class ComiteMembershipInline(admin.TabularInline):
    model = ComiteMembership
    extra = 0
    fields = ['year', 'postes', 'paid']
    filter_horizontal = ['postes']


class MemberInline(admin.StackedInline):
    model = Member
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [
        MemberInline,
    ]


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['admin_image', 'username', 'firstname', 'lastname']
    inlines = [
        SurNameInline,
        ComiteMembershipInline
    ]
    search_fields = ['user__first_name']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(ComitePoste)
class ComitePosteAdmin(admin.ModelAdmin):
    pass


@admin.register(ComiteMembership)
class ComiteMembershipAdmin(admin.ModelAdmin):
    list_display = ['year', 'member']
    list_filter = ['year']
    raw_id_fields = ['member']
    filter_horizontal = ['postes']

admin.site.register(AcademicYear)
