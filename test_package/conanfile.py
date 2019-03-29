from pathlib import Path
from conans import ConanFile, CMake
import os


class DummyTestConan(ConanFile):
    settings = "os"
    generators = "cmake_paths"
    
    def build(self):
        self.cmake = CMake(self)
        self.cmake.definitions["CMAKE_PROJECT_test_dummy_INCLUDE"]=os.path.join(os.getcwd(),"conan_paths.cmake")
        self.cmake.configure()
        self.cmake.build()


    def test(self):
        pass

