# Seed
#
# Copyright (c) The AcaciaLinux contributors, 2023
# Visit https://AcaciaLinux.org/

from components import WelcomeComponent
from components import NetworkComponent
from components import SetsComponent
from components import UserComponent
from components import PartitionComponent
from components import InstallComponent

import blog
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gdk

class StackWindow(Gtk.ApplicationWindow):

    def __init__(self, **kargs):
        self.steps = [ ]

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
        self.steps.append(self.stack.add_titled(WelcomeComponent.welcome_component(self, orientation=Gtk.Orientation.VERTICAL), "welcome", "Welcome"))
        self.steps.append(self.stack.add_titled(NetworkComponent.network_component(self, orientation=Gtk.Orientation.VERTICAL), "network", "Network Setup"))
        self.steps.append(self.stack.add_titled(SetsComponent.sets_component(self, orientation=Gtk.Orientation.VERTICAL), "sets", "Sets"))
        self.steps.append(self.stack.add_titled(UserComponent.user_component(self, orientation=Gtk.Orientation.VERTICAL), "user", "Configuration"))
        self.steps.append(self.stack.add_titled(PartitionComponent.partition_component(self, orientation=Gtk.Orientation.VERTICAL), "partition", "Disk Setup"))
        self.steps.append(self.stack.add_titled(InstallComponent.install_component(self, orientation=Gtk.Orientation.VERTICAL), "install", "Install"))


        #checkbutton.bind_property("active", page1, "needs-attention", GObject.BindingFlags.DEFAULT)

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_sensitive(False)

        style_provider = Gtk.CssProvider()

        #stylesheet
        data = """
        .stack-switcher button:checked {
            color: green;
        }

        .stack-switcher button {
            color: DimGrey;
        }
        """
        style_provider.load_from_data(data, len(data))

        #Add a style provider for the default display
        Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), style_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        stack_switcher.set_css_classes(['stack-switcher'])
        stack_switcher.set_stack(self.stack)
        header.set_title_widget(stack_switcher)
    
    def move_forward(self, _button):
        current_stack_name = self.stack.get_visible_child_name()
        current_stack = None

        for s in self.steps:
            if(s.get_name() == current_stack_name):
                current_stack = s
                break
        
        if(current_stack in self.steps):
            current_stack_index = self.steps.index(current_stack)
            next_index = current_stack_index + 1

            if(len(self.steps) > next_index):
                self.stack.set_visible_child_name(self.steps[next_index].get_name())
            else:
                return
            
        else:
            blog.error("Couldn't find Stackpage.")


    def move_backward(self, _button):
        current_stack_name = self.stack.get_visible_child_name()
        current_stack = None

        for s in self.steps:
            if(s.get_name() == current_stack_name):
                current_stack = s
                break
        
        if(current_stack in self.steps):
            current_stack_index = self.steps.index(current_stack)
            prev_index = current_stack_index - 1

            if(current_stack_index != 0):
                self.stack.set_visible_child_name(self.steps[prev_index].get_name())
            else:
                return
            
        else:
            blog.error("Couldn't find Stackpage.")

def on_activate(app):
    win = StackWindow(application=app)
    win.present()

def on_shutdown(app):
    blog.info("Shutting down.")

def bootstrap_component():
    app = Gtk.Application(application_id="org.AcaciaLinux.SeedUI")
    app.connect("activate", on_activate)
    app.connect("shutdown", on_shutdown)
    app.run(None)