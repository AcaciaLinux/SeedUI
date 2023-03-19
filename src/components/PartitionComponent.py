import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GObject

from components import ForwardBackComponent

class partition_component(Gtk.Box):

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
        title.set_markup("<span foreground=\"green\" size=\"xx-large\">Disk Setup</span>")
        main_box.append(title)

        subtitle = Gtk.Label()
        subtitle.props.halign = Gtk.Align.START
        subtitle.set_markup("Partition your disk(s)")
        main_box.append(subtitle)

        # Setup the control box
        control_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        control_box.set_valign(Gtk.Align.END)
        control_box.append(ForwardBackComponent.forward_back_component(parent_component))

        self.prepend(main_box)
        self.append(control_box)
        