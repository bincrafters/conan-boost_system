#!/usr/bin/env python
# -*- coding: utf-8 -*-
<<<<<<< HEAD

from conans import ConanFile, tools
=======
>>>>>>> testing/1.67.0

from conans import python_requires

<<<<<<< HEAD
class BoostSystemConan(ConanFile):
    name = "Boost.System"
    version = "1.65.1"
    url = "https://github.com/bincrafters/conan-boost-system"
    lib_short_names = ["system"]
    is_header_only = False
    options = {"shared": [True, False]}
    default_options = "shared=False"

    requires = (
        "boost_package_tools/1.65.1@bincrafters/testing", 
        "Boost.Config/1.65.1@bincrafters/testing", 
        "Boost.Assert/1.65.1@bincrafters/testing", 
        "Boost.Core/1.65.1@bincrafters/testing", 
        "Boost.Predef/1.65.1@bincrafters/testing", 
        "Boost.Winapi/1.65.1@bincrafters/testing"
    )


    # BEGIN TEMPLATE
    
    description = "Please visit http://www.boost.org/doc/libs/1_65_1"
    license = "BSL"
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing"
    short_paths = True
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"

    def source(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.source(self)
        getattr(self, "source_additional", lambda:None)()

    def build(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.build(self)
        getattr(self, "build_additional", lambda:None)()
        
    def package(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package(self)
        getattr(self, "package_additional", lambda:None)()
        
    def package_info(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package_info(self)
        getattr(self, "package_info_additional", lambda:None)()
            
    # END TEMPLATE
=======

base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostSystemConan(base.BoostBaseConan):
    name = "boost_system"
    url = "https://github.com/bincrafters/conan-boost_system"
    lib_short_names = ["system"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_predef",
        "boost_winapi"
    ]
>>>>>>> testing/1.67.0
