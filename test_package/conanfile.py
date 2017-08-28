from conans import ConanFile, CMake
import pprint
import glob
import os.path
import random

class TestLib(ConanFile):
    settings = "os", "arch", "compiler"
    generators = "cmake"
    
    def build(self):
        include_path = self.deps_cpp_info.include_paths[0]
        self.header = os.path.relpath(
            random.choice(glob.glob(os.path.join(include_path,"boost","*","*.h*"))),
            include_path).replace("\\","/")
        pprint.pprint(self.header)
    
    def test(self):
        pprint.pprint(self.requires)
        cmake = CMake(self)
        cmake.definitions['HEADER'] = self.header
        cmake.configure(source_dir=self.conanfile_directory, build_dir="./")
        cmake.build()
