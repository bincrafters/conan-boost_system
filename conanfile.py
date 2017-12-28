from conans import ConanFile, tools

class BoostSystemConan(ConanFile):
    name = "Boost.System"
    version = "1.65.1"

    options = {"shared": [True, False]}
    default_options = "shared=False"

    requires = (
        "Boost.Config/1.65.1@bincrafters/testing", 
        "Boost.Assert/1.65.1@bincrafters/testing", 
        "Boost.Core/1.65.1@bincrafters/testing", 
        "Boost.Predef/1.65.1@bincrafters/testing", 
        "Boost.Winapi/1.65.1@bincrafters/testing"
    )

    lib_short_names = ["system"]
    is_header_only = False

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost-system"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1"
    license = "www.boost.org/users/license.html"
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing"
    short_paths = True
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"

    def package_id(self):
        #TODO: Ask what to put here
        pass
        
    def source(self):
        with tools.pythonpath(self):
            import boost_conan_methods  # pylint: disable=F0401
            boost_conan_methods.source(self)

    def build(self):
        with tools.pythonpath(self):
            import boost_conan_methods  # pylint: disable=F0401
            boost_conan_methods.build(self)
            
    def package(self):
        with tools.pythonpath(self):
            import boost_conan_methods  # pylint: disable=F0401
            boost_conan_methods.package(self)
            
    def package_info(self):
        with tools.pythonpath(self):
            import boost_conan_methods  # pylint: disable=F0401
            boost_conan_methods.package_info(self)
    
    # END
