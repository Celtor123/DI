import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from a import Cliente

class Main(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Ventana Principal")


        opcion1 = Gtk.Button("Gestión de coches")
        opcion2 = Gtk.Button("Gestión de clientes")
        fuera = Gtk.Button("Salir")
        bienvenido=Gtk.Label("Eliga la operación a realizar")

        caixaventana = Gtk.Box(spacing=3)
        caixaventana.set_orientation(Gtk.Orientation.VERTICAL)

        self.set_border_width(50)
        self.add(caixaventana)

        caixaSuperior = Gtk.Box()
        caixaSuperior.add(bienvenido)
        caixaSuperior.set_border_width(20)
        caixaventana.add(caixaSuperior)
        caixamedia = Gtk.Box(spacing=40)
        caixamedia.set_border_width(20)
        caixaventana.add(caixamedia)
        caixaInferior=Gtk.Box()
        caixaInferior.set_border_width(20)
        caixaventana.add(caixaInferior)

        caixamedia.add(opcion1)
        caixamedia.add(opcion2)

        caixaInferior.add(fuera)

        opcion1.connect("clicked", self.on_btn_coches)
        opcion2.connect("clicked", self.on_btn_clientes)
        fuera.connect("clicked", self.on_btn_salir)

    def on_btn_coches(self, button):
        print("a")

    def on_btn_clientes (self, button):

        Cliente.cliente().show_all()

    def on_btn_salir (self, button):
        Gtk.main_quit()

Main().connect("destroy", Gtk.main_quit)
Main().show_all()
Gtk.main_quit()
Gtk.main()