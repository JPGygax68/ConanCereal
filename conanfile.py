#====================================================================
# Conan package wrapper for the USCiLab cereal library.
#
# 2016-05-29 gygax@practicomp.ch
#
# This package wrapper is experimental, but please feel free to 
# report problems.
#====================================================================

from conans import ConanFile, CMake

class cerealConan(ConanFile):
  name = "cereal"
  version = "0.1"   # Note: this version number identifies the wrapper, NOT the cereal library!
  # Settings removed because the library is header-only and (to my knowledge) portable
  #settings = "os", "compiler", "build_type", "arch"
  #generators = "cmake"
  exports = "include/*"
  
  def source(self):
    self.run("git clone https://github.com/USCiLab/cereal.git")

  # cereal is header-only and thus does not need a build step  
  #def build(self):
  #  cmake = CMake(self.settings)
  #  self.run('cmake %s %s' % (self.conanfile_directory, cmake.command_line))
  #  self.run("cmake --build . %s" % cmake.build_config)

  def package(self):
    self.copy("*.hpp", dst="include", src="cereal/include")
