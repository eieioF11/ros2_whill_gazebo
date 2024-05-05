cmake_minimum_required(VERSION 3.5)
project(ros2_whill_gazebo)

if(NOT CMAKE_CXX_STANDARD)
    set(CMAKE_CXX_STANDARD 17)
endif()

find_package(ament_cmake_auto REQUIRED)

ament_auto_find_build_dependencies()

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

install(DIRECTORY
  launch
  world
  xacro
  DESTINATION share/${PROJECT_NAME}/
)

ament_auto_package()