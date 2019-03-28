from pathlib import Path
from conans import ConanFile, CMake


class DummyTestConan(ConanFile):
    settings = "os"
    generators = "cmake_find_package"

    def build(self):
        self.cmake = CMake(self)

        prefix = []
        if "CMAKE_PREFIX_PATH" in self.cmake.definitions:
            prefix = self.cmake.definitions["CMAKE_PREFIX_PATH"].split(";")
            
        self.output.info("CMAKE_PREFIX_PATH == " + prefix)
        prefix += [dep_build_path for dep in self.deps_cpp_info.deps for dep_build_path in self.deps_cpp_info[dep].build_paths]
        self.cmake.definitions["CMAKE_PREFIX_PATH"] = ";".join([str(Path(x).as_posix()) for x in prefix])
        
        self.output.info ("CMAKE_PREFIX_PATH == " + self.cmake.definitions["CMAKE_PREFIX_PATH"])
        self.output.info ("cmake configure parameters: " + self.cmake.command_line)

        self.cmake.configure()
        self.cmake.build()


    def test(self):
        pass

