from conans import ConanFile, CMake, tools
import os
from glob import glob


class EigenExtensionsConan(ConanFile):
    name = "eigen-extensions"
    version = "0.13.2"
    license = "MIT"
    author = "Benjamin Navarro <navarro.benjamin13@gmail.com>"
    url = "https://github.com/BenjaminNavarro/conan-eigen-extensions"
    description = "Conan recipe for the eigen-extensions PID package "
    topics = ("C++", "Eigen", "Linear Algebra")
    requires = "eigen/3.3.7@conan/stable"
    generators = "cmake"

    def source(self):
        tools.get(
            "https://gite.lirmm.fr/rob-miscellaneous/eigen-extensions/-/archive/v{0}/eigen-extensions-v{0}.tar.gz".format(self.version))
        os.rename(glob("eigen-extensions-*")[0], "eigen-extensions")

    def package(self):
        self.copy("eigen-extensions/include/Eigen/Eigen/*.h",
                  dst="include/Eigen", keep_path=False)
        self.copy("eigen-extensions/license.txt", keep_path=False)

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        self.cpp_info.defines = ["EIGEN_DENSEBASE_PLUGIN=<Eigen/dense_base_extensions.h>",
                                 "EIGEN_QUATERNIONBASE_PLUGIN=<Eigen/quaternion_base_extensions.h>"]
