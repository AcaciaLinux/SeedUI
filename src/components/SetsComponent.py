import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GObject

from components import ForwardBackComponent

class sets_component(Gtk.Box):

    def __init__(self, parent_component, **kargs):
        super().__init__(**kargs)

        # Margin
        self.set_margin_bottom(10)
        self.set_margin_top(10)
        self.set_margin_end(10)
        self.set_margin_start(10)

        # Setup the main Contentbox
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        main_box.set_valign(Gtk.Align.START)
        main_box.set_vexpand(True)

        title = Gtk.Label()
        title.props.halign = Gtk.Align.START
        title.set_markup("<span foreground=\"green\" size=\"xx-large\">Sets</span>")
        main_box.append(title)

        subtitle = Gtk.Label()
        subtitle.props.halign = Gtk.Align.START
        subtitle.set_markup("Sets determine which packages will be installed.")
        main_box.append(subtitle)


        set_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)

        set_box.set_margin_top(20)
        
        sets = { "sway": "Sway is a tiling window manager.", 
                 "gnome": "Gnome Desktop",
                 "kde": "Plasma Desktop",
                 "networkmanager": "NetworkManager",
                 "audio": "Sound support", 
                 "system": "The base AcaciaLinux system"
                }

        for _set in sets:
            check = Gtk.CheckButton(label=_set)
            #check.connect("toggled", self.on_check_toggled)
            set_box.append(check)

            label = Gtk.Label()
            label.set_halign(Gtk.Align.START)
            label.set_markup(sets[_set])
            label.set_margin_bottom(20)
            set_box.append(label)

        main_box.append(set_box)




        # Setup the control box
        control_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        control_box.set_valign(Gtk.Align.END)
        control_box.append(ForwardBackComponent.forward_back_component(parent_component))

        self.prepend(main_box)
        self.append(control_box)