import os, random, posixpath

from django import template
from django.conf import settings

register = template.Library()

def is_image_file(filename):
    """ Does 'filenam' appear to be an image file?"""
    img_types = [".jpg", ".png", ".gif", ".jpeg"]
    ext = os.path.splitext(filename)[1]
    return ext in img_types

@register.simple_tag
def random_image(path):
    """
    Select a random image file from the provided directory
    and return its href. `path` should be relative to MEDIA_ROOT.

    Usage:  <img src='{% random_image "images/whatever/" %}'>
    """
    SETTINGS_DIR = os.path.dirname(__file__)
    PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
    PROJECT_PATH = os.path.abspath(PROJECT_PATH)

    fullpath = PROJECT_PATH + settings.STATIC_URL + path

    filenames = [f for f in os.listdir(fullpath) if is_image_file(f)]
    pick = random.choice(filenames)
    return posixpath.join(settings.STATIC_URL, path, pick)
