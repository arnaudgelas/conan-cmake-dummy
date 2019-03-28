from conans import ConanFile, CMake


class DummyConan(ConanFile):
    name = "dummy"
    version = "1.0"
    topics = ("cmake")
    generators = "cmake_find_package"
    exports_sources = ["CMakeLists.txt", "dummy-config.cmake", "my-super-cmake-file.cmake"]

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()

        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.builddirs = ["", "lib/cmake"]
