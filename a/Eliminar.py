import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Añadido(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Añade un cliente")
        label=Gtk.Label("was")
        self.add(label)
Añadido.connect("destroy",Gtk.main_quit)
Añadido().show_all()
Gtk.main_quit()
Gtk.main()