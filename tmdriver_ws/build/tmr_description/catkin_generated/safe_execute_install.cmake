execute_process(COMMAND "/home/biorola/tmdriver_ws/build/tmr_description/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/biorola/tmdriver_ws/build/tmr_description/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
