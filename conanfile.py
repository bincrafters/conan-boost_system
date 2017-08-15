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
    lib_short_name = "system"
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
        boost_build = self.deps_cpp_info["Boost.Build"]
        b2_bin_name = "b2.exe" if self.settings.os == "Windows" else "b2"
        b2_bin_dir_name = boost_build.bindirs[0]
        b2_full_path = os.path.join(boost_build.rootpath, b2_bin_dir_name, b2_bin_name)

        toolsets = {
          'gcc': 'gcc',
          'Visual Studio': 'msvc',
          'clang': 'clang',
          'apple-clang': 'darwin'}

        b2_toolset = toolsets[str(self.settings.compiler)]
        
        self.run(b2_full_path + " -j4 -a --hash=yes toolset=" + b2_toolset)

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="include", src=include_dir)
        self.copy(pattern="*", dst="lib", src="stage/lib")

    def package_info(self):
        self.cpp_info.libs = self.collect_libs()
