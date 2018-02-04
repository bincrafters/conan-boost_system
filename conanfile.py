#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostSystemConan(ConanFile):
    name = "boost_system"
    version = "1.65.1"
    url = "https://github.com/bincrafters/conan-boost_system"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    lib_short_names = ["system"]
    is_header_only = False

    options = {"shared": [True, False]}
    default_options = "shared=False"

    requires = (
        "boost_package_tools/1.65.1@bincrafters/testing",
        "boost_config/1.65.1@bincrafters/testing",
        "boost_assert/1.65.1@bincrafters/testing",
        "boost_core/1.65.1@bincrafters/testing",
        "boost_predef/1.65.1@bincrafters/testing",
        "boost_winapi/1.65.1@bincrafters/testing"
    )

    def package_id_additional(self):
        boost_deps_only = [dep_name for dep_name in self.info.requires.pkg_names if dep_name.startswith("boost_")]
       
        for dep_name in boost_deps_only:
            self.info.requires[dep_name].full_version_mode()
        
    # BEGIN

    description = "Please visit http://www.boost.org/doc/libs/1_65_1"
    license = "BSL-1.0"
    short_paths = True
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    build_requires = "boost_generator/1.65.1@bincrafters/testing"

    def package_id(self):
        getattr(self, "package_id_additional", lambda:None)()

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



    # END
