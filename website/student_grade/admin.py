from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export import resources, widgets
from .models import Student, Character, Response, Error, History


class ImportStudentModel(ImportExportModelAdmin):
    list_display = ('id', 'student', 'grade', 'gender')


class ImportCharacterModel(ImportExportModelAdmin):
    list_display = ('id', 'character', 'regularity', 'complexity')


class ImportResponseModel(resources.ModelResource):
    # widget=widgets.ForeignKeyWidget(<table>, <column>)
    student = Field(attribute='student', column_name='student', widget=widgets.ForeignKeyWidget(Student, 'student'))
    character = Field(attribute='character', column_name='character', widget=widgets.ForeignKeyWidget(Character, 'character'))
    correct = Field(attribute='correct', column_name='correct')
    id = Field(attribute='id', column_name='id')

    class Meta:
        model = Response
        export_order = ('id', 'student', 'character', 'correct')
        report_skipped = True


class ResponseModelAdmin(ImportExportModelAdmin):
    resource_class = ImportResponseModel
    list_display = ('id', 'student', 'character', 'correct')


class ImportErrorModel(resources.ModelResource):
    id = Field(attribute='id', column_name='id')
    student = Field(attribute='student', column_name='student', widget=widgets.ForeignKeyWidget(Student, 'student'))
    character = Field(attribute='character', column_name='character',  widget=widgets.ForeignKeyWidget(Character, 'character'))
    error_class = Field(attribute='error_class', column_name='error_class')
    error_number = Field(attribute='error_number', column_name='error_number')
    error_unit = Field(attribute='error_unit', column_name='error_unit')
    error_type = Field(attribute='error_type', column_name='error_type')
    remark = Field(attribute='remark', column_name='remark')

    class Meta:
        model = Error
        export_order = ('id', 'student', 'character', 'error_class', 'error_number', 'error_unit', 'error_type', 'remark')
        report_skipped = True


class ErrorModelAdmin(ImportExportModelAdmin):
    resource_class = ImportErrorModel
    list_display = ('id', 'error_class', 'error_number', 'error_unit', 'error_type', 'remark', 'student')
    list_filter = ('student',)


class AdminHistory(admin.ModelAdmin):
    list_display = ('user_ip', 'action', 'country_ip', 'city_ip', 'visit_date')
    list_filter = ('visit_date', 'action')
    search_fields = ('action', 'city_ip', 'country_ip')


admin.site.register(Student, ImportStudentModel)
admin.site.register(Character, ImportCharacterModel)
admin.site.register(Response, ResponseModelAdmin)
admin.site.register(Error, ErrorModelAdmin)
admin.site.register(History, AdminHistory)
