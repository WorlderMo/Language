cmake_minimum_required(VERSION 3.10)
project(StudentSystem)

set(CMAKE_CXX_STANDARD 11)

add_executable(StudentSystem main.cpp Student_info.h exprtk.hpp Dorm_info.h)