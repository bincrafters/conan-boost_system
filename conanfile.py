#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/testing")

class BoostSystemConan(base.BoostBaseConan):
    name = "boost_system"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_system"
    lib_short_names = ["system"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    b2_requires = [
        "boost_config",
        "boost_winapi"
    ]
