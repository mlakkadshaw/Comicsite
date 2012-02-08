from django.contrib import admin
from comics.comic.models import Author, Comic 

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name', 'email','id')
	search_fields = ('name',)

class ComicAdmin(admin.ModelAdmin):
	list_display = ('name', 'comic_image','description','id')
	filter_horizontal = ('authors',)

admin.site.register(Author,AuthorAdmin)
admin.site.register(Comic, ComicAdmin)