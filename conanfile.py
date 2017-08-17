from conans import ConanFile, os


class BoostSystemConan(ConanFile):
    name = "Boost.System"
    version = "1.64.0"
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
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
        self.run("git clone --depth=1 --branch=boost-{0} {1}.git"
                 .format(self.version, self.source_url))

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
