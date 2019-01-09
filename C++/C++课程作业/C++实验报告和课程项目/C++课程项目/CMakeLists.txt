cmake_minimum_required(VERSION 3.10)
project(StudentSystem)

set(CMAKE_CXX_STANDARD 11)

add_executable(StudentSystem main.cpp Dorm_info.cpp Dorm_info.hpp exprtk.hpp search.cpp search.hpp Student_info.cpp Student_info.hpp Student_new.cpp Student_new.hpp)