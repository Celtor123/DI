import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class e(Gtk.Window):
 def __init__(self):
        Gtk.Window.__init__(self,title="Lista de CLientes")
        print("w")

a=e()
a.connect("destroy",Gtk.main_quit)
a.show_all()
Gtk.main()