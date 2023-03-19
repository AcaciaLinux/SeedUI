import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GObject

from components import ForwardBackComponent

class install_component(Gtk.Box):

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
        title.set_markup("<span foreground=\"green\" size=\"xx-large\">Installing</span>")
        main_box.append(title)

        subtitle = Gtk.Label()
        subtitle.props.halign = Gtk.Align.START
        subtitle.set_markup("This will take some time. We'll restart once we are done.")
        main_box.append(subtitle)
        
        status_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        status_box.set_valign(Gtk.Align.END)

        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_size_request(500, 400)
        scrolledwindow.props.hexpand = True
        scrolledwindow.props.vexpand = True

        sample_data = """Writing partition table..
Running mkfs.ext4 /dev/sda3..
Running mkfs.vfat -F32 /dev/sda1..
Running mkswap /dev/sda2..
Installing base.lfpkg..
Installing libsond.lfpkg..
Installing sond.lfpkg..
Error: Ols zur sau"""

        textview = Gtk.TextView()

        textview.props.vexpand = True

        textview.get_buffer().set_text(sample_data)
        textview.props.editable = False
        textview.props.cursor_visible = False
        scrolledwindow.set_child(textview)

        scrolledwindow.set_margin_top(50)

        main_box.append(scrolledwindow)


        label = Gtk.Label()
        label.set_markup("69% completed")
        status_box.append(label)

        progressbar = Gtk.ProgressBar()
        progressbar.set_margin_bottom(20)
        progressbar.props.fraction = 0.69
        status_box.append(progressbar)


        #progress_box.append(ForwardBackComponent.forward_back_component(parent_component))

        self.prepend(main_box)
        self.append(status_box)