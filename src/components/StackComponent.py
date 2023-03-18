# Seed
#
# Copyright (c) The AcaciaLinux contributors, 2023
# Visit https://AcaciaLinux.org/

from components import WelcomeComponent
from components import NetworkComponent
from components import SetsComponent
from components import UserComponent
from components import PartitionComponent

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GObject

class StackWindow(Gtk.ApplicationWindow):

    def __init__(self, **kargs):
        super().__init__(**kargs, title="AcaciaLinux Installer")

        # Prefer light theme, since the tree looks horrible
        # in a dark theme
        settings = Gtk.Settings.get_default()
        settings.set_property("gtk-theme-name", "Light")

        # Request 900x700 size from compositor
        self.set_default_size(900, 700)

        # Setup TitleBar
        header = Gtk.HeaderBar()
        self.set_titlebar(header)

        # Setup Gtk.Stack
        self.stack = Gtk.Stack()
        self.stack.props.transition_type = Gtk.StackTransitionType.SLIDE_LEFT_RIGHT
        self.stack.props.transition_duration = 500

        # Window"s only child is self.stack
        self.set_child(self.stack)

        # Stacks children are "Steps"
        welcome_step = self.stack.add_titled(WelcomeComponent.welcome_component(self, orientation=Gtk.Orientation.VERTICAL), "welcome", "Welcome")
        network_step = self.stack.add_titled(NetworkComponent.network_component(self, orientation=Gtk.Orientation.VERTICAL), "network", "Network Setup")
        sets_step = self.stack.add_titled(SetsComponent.sets_component(self, orientation=Gtk.Orientation.VERTICAL), "sets", "Sets")
        sets_step = self.stack.add_titled(UserComponent.user_component(self, orientation=Gtk.Orientation.VERTICAL), "user", "Configuration")
        partition_step = self.stack.add_titled(PartitionComponent.partition_component(self, orientation=Gtk.Orientation.VERTICAL), "partition", "Disk Setup")


        #checkbutton.bind_property("active", page1, "needs-attention", GObject.BindingFlags.DEFAULT)

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(self.stack)
        header.set_title_widget(stack_switcher)
    
    def switch_test(self, _button):
        self.stack.set_visible_child_name("check")

def on_activate(app):
    win = StackWindow(application=app)
    win.present()

def bootstrap_component():
    app = Gtk.Application(application_id="org.AcaciaLinux.SeedUI")
    app.connect("activate", on_activate)
    app.run(None)