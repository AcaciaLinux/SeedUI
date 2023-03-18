# Seed
#
# Copyright (c) The AcaciaLinux contributors, 2023
# Visit https://AcaciaLinux.org/

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GObject

#TEMP:
import inspect

class welcome_component(Gtk.Box):

    def __init__(self, parent_component, **kargs):
        super().__init__(**kargs)

        #self.set_margin_top(10)
        self.set_margin_bottom(50)

        # image
        picture = Gtk.Picture.new_for_filename("assets/tree.png")
        self.append(picture)

        # title
        title = Gtk.Label()
        title.set_markup("<span size=\"xx-large\">Welcome to <span foreground=\"green\">AcaciaLinux!</span></span>")
        self.append(title)

        # subtext
        subtext = Gtk.Label()
        subtext.set_markup("The Installer will guide you through initial setup.")
        self.append(subtext)

        button_box = Gtk.Box()
        button = Gtk.Button.new_with_label("Get Started")
        button.connect("clicked", self.get_started_button(parent_component))
        
        # properly align the button
        button_box.props.margin_top = 24
        button_box.props.halign = Gtk.Align.CENTER
        
        button_box.append(button)

        self.append(button_box)

    #
    # Function handler for "Getting Started" Button
    #
    def get_started_button(self, parent_component):
        def get_started_button_func(self):
            parent_component.stack.set_visible_child_name("network")

        return get_started_button_func



    