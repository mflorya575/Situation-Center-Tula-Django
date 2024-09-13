from django.contrib import admin
from .models import *


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Demographics)
class DemographicsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Road)
class RoadAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Science)
class ScienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Ecology)
class EcologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Turism)
class TurismAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(World)
class WorldAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Labour)
class LabourAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Atom)
class AtomAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Econom)
class EconomAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Mainline)
class MainlineAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Agro)
class AgroAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Trading)
class TradingAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Uslugi)
class UslugiAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Investing)
class InvestingAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(FinPr)
class FinPrAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ProdPrice)
class ProdPriceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Joblessness)
class JoblessnessAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(JobMarket)
class JobMarketAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(SmallMediumCompany)
class SmallMediumCompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Population)
class PopulationAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(LevelHealth)
class LevelHealthAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(SecureNature)
class SecureNatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CapitalAssets)
class CapitalAssetsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(SHLRR)
class SHLRRAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(InfoTechnology)
class InfoTechnologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ForeignTrading)
class ForeignTradingAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(VRP)
class VRPAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(IndustrialProd)
class IndustrialProdAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'csv_file')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
