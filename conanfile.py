from conans import ConanFile, tools, os
import re


class BoostSystemConan(ConanFile):
    name = "Boost.System"
    version = "1.64.0"
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    short_paths = True
    options = {
        "shared": [True, False] }
    default_options = \
        "shared=False"
    url = "https://github.com/bincrafters/conan-boost-system"
    source_url = "https://github.com/boostorg/system"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["system"]
    build_requires = "Boost.Generator/0.0.1@bincrafters/testing"
    requires = "Boost.Config/1.64.0@bincrafters/testing", \
        "Boost.Assert/1.64.0@bincrafters/testing", \
        "Boost.Core/1.64.0@bincrafters/testing", \
        "Boost.Predef/1.64.0@bincrafters/testing", \
        "Boost.Winapi/1.64.0@bincrafters/testing"
                      
    def source(self):
        for lib_short_name in self.lib_short_names:
            archive = "boost-" + self.version \
                if re.match("[0-9]+[.][0-9]+[.][0-9]+", self.version) \
                else self.version
            tools.get("https://github.com/boostorg/{0}/archive/{1}.tar.gz"
                .format(lib_short_name, archive))
            os.rename(lib_short_name+"-"+archive, lib_short_name)

    def build(self):
        self.run(self.deps_user_info['Boost.Generator'].b2_command)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

        self.copy(pattern="*", dst="lib", src="stage/lib")

    def package_info(self):
        self.user_info.lib_short_names = (",").join(self.lib_short_names)
        self.cpp_info.libs = self.collect_libs()
        self.cpp_info.defines.append("BOOST_ALL_NO_LIB=1")
