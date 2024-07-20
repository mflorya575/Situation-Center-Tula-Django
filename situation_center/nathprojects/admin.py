from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Hospital


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('year', 'deaths')
    list_editable = ('deaths',)
    list_per_page = 20  # Для удобства можно установить количество записей на страницу

    def get_changelist_form(self, request, **kwargs):
        """
        Это нужно для возможности редактирования полей прямо в списке объектов.
        """
        kwargs['form'] = self.get_form(request, **kwargs)
        return super().get_changelist_form(request, **kwargs)

    def save_model(self, request, obj, form, change):
        """
        Сохранение модели.
        """
        super().save_model(request, obj, form, change)
        if "_addanother" in request.POST:
            obj.pk = None

    def response_add(self, request, obj, post_url_continue=None):
        """
        После добавления новой записи, остаёмся на той же странице, чтобы добавить ещё.
        """
        if "_addanother" in request.POST:
            return self.response_add_same(request, obj)
        return super().response_add(request, obj, post_url_continue)

    def response_add_same(self, request, obj):
        """
        Настройка кнопки "Сохранить и добавить другой".
        """
        opts = self.model._meta
        return HttpResponseRedirect(
            reverse('admin:%s_%s_add' % (opts.app_label, opts.model_name))
        )
