from django.contrib import admin
from polls.models import Choice, Poll


#class ChoiceInline(admin.StackedInline):
#    model = Choice
#    extra = 3






class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['question']}),
        ('Date Information',{'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
#    inlines = [ChoiceInline]


#fieldsets = [
#        (None,              {'fields': ['question']}),     lo tercero que tenia
#        ('Date Information',{'fields': ['pub_date']}),
#    ]



#    fields = ['pub_date', 'question'] lo segundo que tenia dentro de la clase

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)



# admin.site.register(Poll) lo primero que tenia
