# Seed
#
# Copyright (c) The AcaciaLinux contributors, 2023
# Visit https://AcaciaLinux.org/

import blog
from components import StackComponent

def main():
    blog.info("Starting up..")

    blog.info("Bootstraping GTK-Window..")
    StackComponent.bootstrap_component()


if(__name__ == "__main__"):
    try:
        main()
    except KeyboardInterrupt:
        blog.info("Exiting on KeyboardInterrupt.")