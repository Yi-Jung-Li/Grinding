cmake_minimum_required(VERSION 2.8.3)
project(tmr_description)

find_package(catkin REQUIRED)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES tmr_description
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(DIRECTORY meshes DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(DIRECTORY urdf DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(DIRECTORY xacro DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})


catkin_python_setup()

#install(
#  DIRECTORY scripts/
#  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
#  USE_SOURCE_PERMISSIONS
#)

catkin_install_python(PROGRAMS
  scripts/modify_urdf.py
  scripts/modify_xacro.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
