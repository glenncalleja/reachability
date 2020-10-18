"""A simple Opening hours manager which allows you to specify
the Opening Hours in a simple way, and display them in
a human-friendly readable way.

Also provides a way to check if a certain time falls inside the
specified Opening Hours.
"""

__version__ = "0.0.5"
__appname__ = "human_friendly_opening_hours"
__author__ = "Glenn Calleja Frendo <glenncal@gmail.com>"
__licence__ = "AGPLv3"

from .reachability import ReachabilityObserver, Reachability
