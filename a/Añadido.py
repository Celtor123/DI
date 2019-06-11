import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import sqlite3 as db


conexion = db.connect("Proxecto.db")
micursor = conexion.cursor()


class añadido(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Añade un cliente")
        label=Gtk.Label("was")
        self.add(label)
        #print(Cliente.cliente.lista)
#añadido().connect("destroy",Gtk.main_quit)
añadido().show_all()
Gtk.main_quit()
Gtk.main()