import flet as ft

"""
Flet es un framework capaz de construir aplicaciones web, de escritorio y moviles en Python, sin la necesidad de saber
frontend.
Se pueden crear interfaces de usuario con CONTROLES que estan basados en Flutter de Google.
Los controles se deben anadir a Page (primer y principal control) o dentro de otros controles. Controles anidados pueden
ser representados como un arbol, donde Page es la raiz.
"""


def app_ejemplo(pagina: ft.Page):
    """
    Pequena funcion para demostrar el funcionamiento y la sencillez de Flet
    :param pagina: Flet.Page
    """
    # Los controles son clases comunes de Python
    texto = ft.Text(value='Hola mundo!', color='green')
    # Para mostrar el control, anadirlo a la lista de Page
    pagina.controls.append(texto)
    # Enviar los cambios a la aplicacion de escritorio o web
    pagina.update()


# Algunos controles son contenedores de otros controles, como Page o Row
# Row permite agregar controles en una fila
fila = ft.Row([ft.Text('A'), ft.Text('B'), ft.Text('C')])

# La propiedad VISIBLE es True por defecto. Indica que el control se renderiza en la pagina. Si el control
# se establece en False, no se renderizara, no se podra seleccionar ni podra emitir eventos.
# Ademas, todos tienen la propiedad DISABLED la cual es False por defecto. Su uso es comun en TextField, Dropdown,
# Checkbox y demas.
# Estas propiedades pueden ser seteadas en controles padre para propagarse a sus hijos.

# BOTON
boton = ft.ElevatedButton('Soy un boton', visible=False)


# CHECKBOX
def checkbox(pagina: ft.Page):
    """
    Funcion para mostrar el funcionamiento de un control Checkbox
    :param pagina: Flet.Page
    """
    def cambio(e):
        """
        Actualiza el texto y la pagina
        """
        texto.value = f'Aprendiste Flet? {'Si' if check.value else 'No'}'
        pagina.update()

    texto = ft.Text()
    check = ft.Checkbox(label='Que hacer: aprender a usar Flet', value=False, on_change=cambio)
    pagina.add(check, texto)


# DROPDOWN
def dropdown(pagina: ft.Page):
    """
    Funcion para mostrar el funcionamiento de un control Dropdown
    :param pagina: Flet.Page
    :return:
    """
    def boton_click(e):
        """
        Actualiza el texto y la pagina
        """
        texto.value = f'El valor es {color_dropdown.value.lower()}'
        pagina.update()

    texto = ft.Text()
    boton_enviar = ft.ElevatedButton(text='Enviar', on_click=boton_click)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[ft.dropdown.Option('Rojo'), ft.dropdown.Option('Verde'), ft.dropdown.Option('Azul')]
    )
    pagina.add(color_dropdown, boton_enviar, texto)


# Para crear un control personalizado, lo ideal es realizarlo a partir de un control ya existente a
# traves de una clase personalizada
class BotonPers(ft.ElevatedButton):
    def __init__(self, texto: str, comando):
        super().__init__()
        self.bgcolor = ft.colors.ORANGE_300
        self.color = ft.colors.DEEP_ORANGE_300
        self.text = texto
        self.on_click = comando


# Crearemos aqui un contenedor de controles. Puede utilizarse COLUMN, ROW, STACK o incluso VIEW para combinar
# distintos controles
class Tarea(ft.Row):
    def __init__(self, texto: str):
        super().__init__()
        self.txt_visible = ft.Text(texto)
        self.txt_editar = ft.TextField(texto, visible=False)
        self.boton_editar = ft.IconButton(icon=ft.icons.EDIT, on_click=self.editar)
        self.boton_guardar = ft.IconButton(icon=ft.icons.SAVE, on_click=self.guardar, visible=False)
        self.controls = [  # Controles dentro de la Row personalizada
            ft.Checkbox(),
            self.txt_visible,
            self.txt_editar,
            self.boton_editar,
            self.boton_guardar
        ]
        # Para que un control este apartado de los controles exteriores, marcar atributo isolated = False
        # Esto permite que, por ejemplo, cuando se llame al metodo .update() en el contenedor (en este caso ft.page),
        # esta Row no se actualice.
        self.isolated = True
        # Como buena practica, se recomienda que cada control personalizado que ejecute .update() dentro de sus metodos
        # sea apartado con ISOLATED = True

    def editar(self, e):
        self.boton_editar.visible = False
        self.boton_guardar.visible = True
        self.txt_visible.visible = False
        self.txt_editar.visible = True
        self.update()

    def guardar(self, e):
        self.boton_editar.visible = True
        self.boton_guardar.visible = False
        self.txt_visible.visible = True
        self.txt_editar.visible = False
        self.txt_visible.value = self.txt_editar.value
        self.update()

    def build(self):
        """
        Este metodo se ejecuta cuando el control se crea y se asigna a self.page.
        Podriamos sobreescribir este metodo para implementar una logica que no puede ejecutarse en el constructor por
        requerir acceso a self.page. Por ejemplo, elegir el icono correspondiente dependiendo de self.page.platform
        """
        super().build()

    def did_mount(self):
        """
        Este metodo se ejecuta despues de que se anada a la pagina (page) y tenga asignada una UID.
        Sobreescribir este metodo para implementar una logica que requiera ser ejecutada luego de que el control
        se anada a la pagina. Por ejemplo, para actualizarse a traves de una API
        """
        super().did_mount()

    def will_unmount(self):
        """
        Metodo que se ejecuta cuando el control va a ser removido de la pagina (page).
        Sobreescribir este metodo para ejecutar limpieza
        """
        super().will_unmount()

    def before_update(self):
        """
        Metodo que se ejecuta cada vez que este control se actualiza
        No ejecutar aqui .UPDATE() !
        """
        super().before_update()


# Testeo de la nueva ROW personalizada en una funcion
def tareas(pagina: ft.Page):
    pagina.add(Tarea(texto='Lavar la ropa'), Tarea(texto='Cocinar la cena'))


# El framework Flet permite crear aplicaciones adaptativas, lo que significa que nuestra aplicacion se vera bien en
# cualquier plataforma que la ejecute, sin que hagan falta distintas aplicaciones para distintos dispositivos.
def app_adaptativa(pagina: ft.Page):
    pagina.adaptive = True  # Con este parametro establecido en True es suficiente
    pagina.appbar = ft.AppBar(
        leading=ft.TextButton('Nuevo', style=ft.ButtonStyle(padding=0)),
        title=ft.Text('AppBar adaptativa'),
        actions=[ft.IconButton(ft.cupertino_icons.ADD, style=ft.ButtonStyle(padding=0))],
        bgcolor=ft.colors.with_opacity(0.04, ft.cupertino_colors.SYSTEM_BACKGROUND)
    )
    pagina.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(label='Explorar', icon=ft.icons.EXPLORE),
            ft.NavigationDestination(label='Desplazarse', icon=ft.icons.COMMUTE),
            ft.NavigationDestination(label='Marcador', icon=ft.icons.BOOKMARK_BORDER, selected_icon=ft.icons.BOOKMARK)
        ],
        border=ft.Border(top=ft.BorderSide(color=ft.cupertino_colors.SYSTEM_GREY2, width=0))
    )

    pagina.add(ft.SafeArea(ft.Column(controls=[
        ft.Checkbox(label='Modo oscuro', value=False),
        ft.Text('Primer campo: '),
        ft.TextField(keyboard_type=ft.KeyboardType.TEXT),
        ft.Text('Segundo campo: '),
        ft.TextField(keyboard_type=ft.KeyboardType.TEXT),
        ft.Switch('Un switch'),
        ft.FilledButton(content=ft.Text('Boton adaptativo')),
        ft.Text('Linea de texto 1'),
        ft.Text('Linea de texto 2'),
        ft.Text('Linea de texto 3')
    ])))


def rutas_simple(pagina: ft.Page):
    """
    Ya que la navegacion dentro de nuestra app es escencial, con Flet podemos configurar diferentes rutas
    para diferentes partes de la aplicacion. Esto es especificamente util en aplicacion web.
    La ruta por defecto comienza con una barra, por ejemplo, https://localhost/
    """
    # Puede obtenerse la ruta con la propiedad ft.Page.route
    pagina.add(ft.Text(f'Ruta inicial: {pagina.route}'))

    def cambio_ruta(e: ft.RouteChangeEvent):
        """
        Cada vez que la ruta cambie, se anadira un nuevo texto
        """
        pagina.add(ft.Text(f'Nueva ruta: {e.route}'))

    def tienda(e):
        """
        Ir a la tienda: https://localhost/tienda
        """
        pagina.route = '/tienda'
        pagina.update()

    pagina.on_route_change = cambio_ruta
    pagina.add(ft.ElevatedButton('Ir a la tienda', on_click=tienda))


def rutas_complejo(pagina: ft.Page):
    """
    Para una navegacion eficaz, es necesario que haya un solo lugar en el programa donde se ejecuten todas las vistas
    o "VIEWS" dependiendo de la ruta actual. Con este ejemplo, se podra navegar a traves de los botones renderizados,
    y tambien con los botones del navegador para ir atras, adelante, o incluso cambiando la URL
    :param pagina: Flet.Page
    """
    pagina.title = 'Ejemplo de rutas'

    def cambio_ruta(ruta: str):
        pagina.views.clear()
        pagina.views.append(
            ft.View('/', controls=[
                ft.AppBar(title=ft.Text('Aplicacion Flet'), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.ElevatedButton('Ir a tienda', on_click=lambda _: pagina.go('/tienda'))  # Ir a la tienda
            ])
        )
        if pagina.route == '/tienda':
            pagina.views.append(ft.View('/tienda', controls=[
                ft.AppBar(title=ft.Text('Tienda'), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.ElevatedButton('Ir al inicio', on_click=lambda _: pagina.go('/'))  # Volver al inicio
            ]))

        pagina.update()

    def remover_view(v):
        pagina.views.pop()
        view_superior = pagina.views[-1]
        pagina.go(view_superior.route)

    pagina.on_route_change = cambio_ruta
    pagina.on_view_pop = remover_view
    pagina.go(pagina.route)


# Aplicacion de ejemplo mas compleja
def aplicacion(pagina: ft.Page):
    """
    Funcion de ejemplo para una aplicacion de contador, con un boton '-', texto, y '+'
    :param pagina: Flet.Page
    """
    pagina.title = "Ejemplo de contador"  # Titulo de la pagina
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER  # Alineacion al centro

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)  # Cuadro de texto

    def minus_click(e):  # Funcion a ejecutar por el boton "-"
        txt_number.value = str(int(txt_number.value) - 1)
        pagina.update()

    def plus_click(e):  # Funcion a ejecutar por el boton "+"
        txt_number.value = str(int(txt_number.value) + 1)
        pagina.update()

    pagina.add(
        ft.Row(  # Se anade una fila a la pagina
            [  # Dentro de la fila se anade lo siguiente
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),  # Boton con icono "-"
                txt_number,  # Cuadro de texto
                ft.IconButton(ft.icons.ADD, on_click=plus_click),  # Boton con icono "+"
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Alineacion al centro
        )
    )


ft.app(rutas_complejo, view=ft.AppView.WEB_BROWSER)  # Ejecutar app (equivalente a mainloop de TK)

"""
Con Flet instalado, se puede ejecutar la aplicacion con el siguiente comando:
flet run {nombre_del_archivo}.py

Para correrlo como una aplicacion web (abrirlo en navegador con puerto aleatorio):
flet run --web {nombre_del_archivo}.py

Por defecto, Flet observara cualquier cambio que se le haga al archivo corriendo y recargara la app cuando
este cambie y se guarde, pero no comprobara cambios en otros archivos.
Para observar todos los archivos de un directorio:
flet run -d {nombre_del_archivo}.py
"""