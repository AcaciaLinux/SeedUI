import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GObject

class forward_back_component(Gtk.CenterBox):

    def __init__(self, parent_component, **kargs):
        super().__init__(**kargs)

        back_button = Gtk.Button(label="Back")
        back_button.connect("clicked", parent_component.move_backward)
        self.set_start_widget(back_button)

        forward_button = Gtk.Button(label="Continue")
        forward_button.connect("clicked", parent_component.move_forward)
        self.set_end_widget(forward_button)





