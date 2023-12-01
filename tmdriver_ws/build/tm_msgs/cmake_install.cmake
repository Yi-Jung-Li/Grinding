# Install script for directory: /home/biorola/tmdriver_ws/src/tm_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/biorola/tmdriver_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tm_msgs/msg" TYPE FILE FILES
    "/home/biorola/tmdriver_ws/src/tm_msgs/msg/FeedbackState.msg"
    "/home/biorola/tmdriver_ws/src/tm_msgs/msg/SvrResponse.msg"
    "/home/biorola/tmdriver_ws/src/tm_msgs/msg/SctResponse.msg"
    "/home/biorola/tmdriver_ws/src/tm_msgs/msg/StaResponse.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tm_msgs/srv" TYPE FILE FILES
    "/home/biorola/tmdriver_ws/src/tm_msgs/srv/ConnectTM.srv"
    "/home/biorola/tmdriver_ws/src/tm_msgs/srv/WriteItem.srv"
    "/home/biorola/tmdriver_ws/src/tm_msgs/srv/AskItem.srv"
    "/home/biorola/tmdriver_ws/src/tm_msgs/srv/SendScript.srv"
    "/home/biorola/tmdriver_ws/src/tm_msgs/srv/SetEvent.srv"
    "/home/biorola/tmdriver_ws/src/tm_msgs/srv/SetIO.srv"
    "/home/biorola/tmdriver_ws/src/tm_msgs/srv/SetPositions.srv"
    "/home/biorola/tmdriver_ws/src/tm_msgs/srv/AskSta.srv"
    "/home/biorola/tmdriver_ws/src/tm_msgs/srv/robot_state.srv"
    "/home/biorola/tmdriver_ws/src/tm_msgs/srv/robot_motion.srv"
    "/home/biorola/tmdriver_ws/src/tm_msgs/srv/Ask_img.srv"
    "/home/biorola/tmdriver_ws/src/tm_msgs/srv/Ask_img_AD.srv"
    "/home/biorola/tmdriver_ws/src/tm_msgs/srv/defect_detect.srv"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tm_msgs/cmake" TYPE FILE FILES "/home/biorola/tmdriver_ws/build/tm_msgs/catkin_generated/installspace/tm_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/biorola/tmdriver_ws/devel/include/tm_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/biorola/tmdriver_ws/devel/share/roseus/ros/tm_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/biorola/tmdriver_ws/devel/share/common-lisp/ros/tm_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/biorola/tmdriver_ws/devel/share/gennodejs/ros/tm_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/biorola/tmdriver_ws/devel/lib/python2.7/dist-packages/tm_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/biorola/tmdriver_ws/devel/lib/python2.7/dist-packages/tm_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/biorola/tmdriver_ws/build/tm_msgs/catkin_generated/installspace/tm_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tm_msgs/cmake" TYPE FILE FILES "/home/biorola/tmdriver_ws/build/tm_msgs/catkin_generated/installspace/tm_msgs-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tm_msgs/cmake" TYPE FILE FILES
    "/home/biorola/tmdriver_ws/build/tm_msgs/catkin_generated/installspace/tm_msgsConfig.cmake"
    "/home/biorola/tmdriver_ws/build/tm_msgs/catkin_generated/installspace/tm_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tm_msgs" TYPE FILE FILES "/home/biorola/tmdriver_ws/src/tm_msgs/package.xml")
endif()
