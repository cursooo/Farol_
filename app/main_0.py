from nicegui import ui

@ui.page('/')
def principal() ->None:
    with ui.row():
        ui.label('Visca Barça')
    ui.label("HI")
    ui.button('Xique-Xique')

    ui.query('body').classes('bg-amber-100')

ui.run(title= "Minha primeira pagina web",
        language='Pt-BR', favicon='../img/logo_farol_na_quebrada.jpg'
)