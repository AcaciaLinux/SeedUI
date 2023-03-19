import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GObject, GdkPixbuf

from components import ForwardBackComponent

class user_component(Gtk.Box):

    def __init__(self, parent_component, **kargs):
        super().__init__(**kargs)

        # Margin
        self.set_margin_bottom(10)
        self.set_margin_top(10)
        self.set_margin_end(10)
        self.set_margin_start(10)

        # Setup the main Contentbox
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        main_box.set_vexpand(True)

        title = Gtk.Label()
        title.props.halign = Gtk.Align.START
        title.set_markup("<span foreground=\"green\" size=\"xx-large\">Configuration</span>")
        main_box.append(title)

        subtitle = Gtk.Label()
        subtitle.props.halign = Gtk.Align.START
        subtitle.set_markup("We need some more information.")
        main_box.append(subtitle)

        # image
        # Load the image file as a Pixbuf object
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size("assets/user.png", 256, 256)

        # Use the Pixbuf as desired, for example in a Gtk.Image widget
        image = Gtk.Image.new_from_pixbuf(pixbuf)
        image.set_size_request(128, 128)

        # Add the Image widget to the main window or box
        main_box.append(image)


        form_grid = Gtk.Grid()
        form_grid.props.halign = Gtk.Align.CENTER
        form_grid.set_margin_top(20)
        
        username = Gtk.Entry()
        username.props.placeholder_text = "Username"
        form_grid.attach(username, 0,0,2,1)

        fullname = Gtk.Entry()
        fullname.props.placeholder_text = "Full Name"
        fullname.props.margin_top = 24
        form_grid.attach_next_to(fullname, username, Gtk.PositionType.BOTTOM, 2, 1)

        password = Gtk.PasswordEntry()
        password.props.placeholder_text = "Password"
        password.props.show_peek_icon = True
        password.props.margin_top = 24
        form_grid.attach_next_to(password, fullname, Gtk.PositionType.BOTTOM, 1, 1)

        password_repeat = Gtk.PasswordEntry()
        password_repeat.props.placeholder_text = "Password Repeat"
        password_repeat.props.show_peek_icon = True
        password_repeat.props.margin_top = 24
        password_repeat.props.margin_start = 20
        form_grid.attach_next_to(password_repeat, password, Gtk.PositionType.RIGHT, 1, 1)

        hostname = Gtk.Entry()
        hostname.props.placeholder_text = "Hostname"
        hostname.props.margin_top = 24
        form_grid.attach_next_to(hostname, password, Gtk.PositionType.BOTTOM, 2, 1)
        
        main_box.append(form_grid)



        # Setup the control box
        control_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        control_box.set_valign(Gtk.Align.END)
        control_box.append(ForwardBackComponent.forward_back_component(parent_component))

        self.prepend(main_box)
        self.append(control_box)