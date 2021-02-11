cmake_minimum_required(VERSION 3.17)
project(cppthreading)

set(CMAKE_CXX_STANDARD 14)
# set(CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS} "-std=c++14 -pthread")

# find_package(Threads)

add_executable(cppthreading
        .idea/workspace.xml main.cpp main.cpp)

# target_link_libraries(cppthreading Threads::Threads ${CMAKE_THREAD_LIBS_INIT})