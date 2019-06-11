import gi
import sqlite3 as db

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Spacer, Table, TableStyle)
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors




# controles de sqlLite
conexion = db.connect("Proxecto.db")
micursor = conexion.cursor()
micursor.execute("""CREATE TABLE IF NOT EXISTS CLIENTE (
NOME VARCHAR(15) PRIMARY KEY,
APELIDO VARCHAR(50),
CARNET VARCHAR(7),
NÚMERO_DO_SEGURO INTEGER,
DNI VARCHAR(9) UNIQUE,
INCIDENCIAS VARCHAR(70))"""
         )
micursor.execute("INSERT INTO CLIENTE (NOME,APELIDO,CARNET,NÚMERO_DO_SEGURO,DNI,INCIDENCIAS) VALUES ('A','Ta','Cw',56,'Re','Er')")
#cursor.execute("DELETE FROM CLIENTE WHERE NOME='A'")

#cursor.execute("drop table CLIENTE")

class cliente(Gtk.Window):
    lista = []
    def __init__(self):
        Gtk.Window.__init__(self,title="Lista de CLientes")

        botona=Gtk.Button("Eliminar")
        botonb=Gtk.Button("Consultar")
        botonc=Gtk.Button("Añadir")
        botond = Gtk.Button("Imprimir")
        botona.connect("clicked",self.boton_1_selected)
        botonb.connect("clicked", self.boton_2_selected)
        botonc.connect("clicked", self.boton_3_selected)
        botond.connect("clicked", self.boton_4_selected)
        ventana = Gtk.Box(spacing=30)
        ventana.add(botona)
        ventana.add(botonb)
        ventana.add(botonc)
        ventana.add(botond)
        caixaventana2 = Gtk.Box(spacing=30)

        caixasuperior = Gtk.Box(spacing=30)
        caixasuperior.add(ventana)
        layout = Gtk.Box()
        caixaventana2.add(layout)
        caixasuperior.add(caixaventana2)
        self.add(caixasuperior)
        micursor.execute("SELECT * FROM CLIENTE")
        resultado=micursor.fetchall()
        People=[("a","f","g",4,"e","r"),("a","f","g",40,"e","r"),("a","f","g",4,"e","r")]
        # convert data to list_store
        list_store = Gtk.ListStore(str,str,str,int,str,str)


        for item in resultado:
           a=list(item)
           list_store.append(a)
        people_tree = Gtk.TreeView(list_store)

        for i, col_title in enumerate(["nome", "apelido", "carnet","Número do seguro","Dni","Incidencias"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)
            #hacer posible la ordenacion
            column.set_sort_column_id(i)
            people_tree.append_column(column)
            #selección al seleccionar
        selected_row=people_tree.get_selection()
        selected_row.connect("changed",self.item_selected)
        layout.pack_start(people_tree, True, True, 2)

    def boton_1_selected(self,button):
           print(self.lista)

    def boton_2_selected(self, button):
        print("c")

    def boton_3_selected(self, button):
            print("añadir")

    def boton_4_selected(self, button):
        print("d")
    def item_selected(self,selection):
         model,row=selection.get_selected()
         if row is not None:
             micursor.execute("SELECT * FROM CLIENTE")
             resultado = micursor.fetchall()
             for item in resultado:
                 a = list(item)
                 print(a)
                 self.lista.append(a)

mi = cliente()
mi.connect("destroy", Gtk.main_quit)
mi.show_all()
Gtk.main()

#Realizar unha aplicación con formularios que ten que funcionar sobre o entorno gráfico de ubuntu (Gtk3). A aplicación ten que ter polo menos 3 formularios.
# Teremos un formulario de entrada que permita o usuario elixir entre, Xestión de Clientes e Xestión de Produtos/Servizos, permitindo a posibilidade de saír.
# No formulario de xestión de clientes dará a posibilidade de Insertar, Consultar e Borrar un cliente. Os datos persoais a gardar serán os habituais (non menos de 6).
#No programa hai que inserir algún Treeview e algún ComboBox. Tamén ter en conta os criterios de usabilidade para deseñara a aplicación.
#Teremos que crear unha base de datos e conectarnos a ela. Propoño usar o método que indica o manual de Python Para Todos no seu capítulo 11 (pag.117),
# SQLite en modo local (si alguén quere utilizar outra base de datos, non hai problema).
#O proxecto ten que xerar polo menos dous informes realizados con Reportlab. Os informes terá que xeralos a aplicación dende o programa cos datos da base de datos.
# O tipo de informe poderá ser un listado, factura, ficha cliente, etc.