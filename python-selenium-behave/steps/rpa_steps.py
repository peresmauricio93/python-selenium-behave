from behave import given, when, then
from functions.rpa_functions import RpaFunctions


rpaFun = RpaFunctions()
users = []


@given(u'que eu acesso ao site rpa challenge')
def acess_page(context):
    rpaFun.acess_page()


@then(u'clico em start para comecar o teste')
def button_start(context):
    rpaFun.button_start()


@when(u'preencho todos os dados do excel em seus respectivos campos')
def input_all(context):
    rpaFun.delete_archives()
    rpaFun.read_excel(users)
    rpaFun.preencher_tudo(users)


@then(u'valido a tela de congratulations')
def validate_congratulations(context):
    rpaFun.validate_congratulations()
