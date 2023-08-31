#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import setuptools
from setuptools import setup, find_packages
from setuptools.command.install import install
import warnings
import os
import sys

#Set up the machinery to install custom fonts.
class MoveFonts(install):
    def run(self):
        """
        Performs the usual install process and then copies the True Type fonts 
        that come with jotaviz into matplotlib's True Type font directory, 
        and deletes the matplotlib fontList.cache 
        """
        #Perform the usual install process
        install.run(self)
        #Try to install custom fonts
        try:
            import os, shutil
            import matplotlib as mpl
            import jotaviz
            
            #Find where matplotlib stores its True Type fonts
            mpl_data_dir = os.path.dirname(mpl.matplotlib_fname())
            mpl_ttf_dir = os.path.join(mpl_data_dir, 'fonts', 'ttf')
            
            #Copy the font files to matplotlib's True Type font directory
            #(I originally tried to move the font files instead of copy them,
            #but it did not seem to work, so I gave up.)
            fonts_dir = os.path.join(os.path.dirname(jotaviz.__file__), 'fonts')
            for file_name in os.listdir(fonts_dir):
                if file_name[-4:] == '.ttf':
                    old_path = os.path.join(fonts_dir, file_name)
                    new_path = os.path.join(mpl_ttf_dir, file_name)
                    shutil.copyfile(old_path, new_path)
                    print("Copying " + old_path + " -> " + new_path)
            
            #Try to delete matplotlib's fontList cache
            mpl_cache_dir = mpl.get_cachedir()
            mpl_cache_dir_ls = os.listdir(mpl_cache_dir)
            font_list_cache_names = ["fontList.cache", "fontList.py3k.cache"]
            for font_list_cache_name in font_list_cache_names:
                if font_list_cache_name in mpl_cache_dir_ls:
                    fontList_path = os.path.join(mpl_cache_dir, font_list_cache_name)
                    os.remove(fontList_path)
                    print("Deleted the matplotlib " + font_list_cache_name)
        except:
            warnings.warn("WARNING: An issue occured while installing the custom fonts for jotaviz.")


if __name__ == "__main__":
    setuptools.setup(name="jotaviz", 
                     package_data = {"" : ["fonts/*.ttf"]}, 
                     cmdclass={"install" : MoveFonts})
