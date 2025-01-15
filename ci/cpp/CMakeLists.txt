cmake_minimum_required(VERSION 3.26)
include(FetchContent)
project(test-cpp CXX)

# Version of the kaitai_struct_cpp_stl_runtime
# Should match that of the kaitai-struct-compiler
set(KSCSR_VERSION "0.10")

set(kaitai_struct_cpp_stl_runtime_BUILD_TESTS OFF CACHE INTERNAL
    "Disable tests in katai_struct_cpp_stl build" FORCE)

FetchContent_Declare(
  kaitai_struct_cpp_stl_runtime
  GIT_REPOSITORY https://github.com/kaitai-io/kaitai_struct_cpp_stl_runtime.git
  GIT_TAG        ${KSCSR_VERSION}
  GIT_SHALLOW    ON
  FIND_PACKAGE_ARGS
)

FetchContent_MakeAvailable(kaitai_struct_cpp_stl_runtime)

# Check kaitai-struct-compiler version
execute_process(
  COMMAND bash -c "kaitai-struct-compiler --version | awk '{ print $2 }'"
  OUTPUT_VARIABLE KSC_VERSION
)

if(NOT ${KSC_VERSION} STREQUAL ${KSCSR_VERSION})
  message(FATAL "kaitai-struct-compiler version ${KSC_VERSION} does not match kaitai_struct_cpp_stl_runtime-struct version ${KSCSR_VERSION}")
endif()

# Convenient link to the directory containing the ksy files
set(TEMPLATE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../../src/tablestream/templates)

# Generate the cpp files from the various ksy files
add_custom_command(OUTPUT dtype.cpp metadata.cpp VERBATIM
  DEPENDS ${TEMPLATE_DIR}/metadata.ksy
  COMMAND kaitai-struct-compiler -t cpp_stl --cpp-standard=11
          ${TEMPLATE_DIR}/metadata.ksy
)

add_custom_command(OUTPUT lock.cpp VERBATIM
  DEPENDS ${TEMPLATE_DIR}/lock.ksy
  COMMAND kaitai-struct-compiler -t cpp_stl --cpp-standard=11
          ${TEMPLATE_DIR}/lock.ksy
)

add_custom_command(OUTPUT standard_storage_manager.cpp VERBATIM
  DEPENDS ${TEMPLATE_DIR}/standard_storage_manager.ksy
  COMMAND kaitai-struct-compiler -t cpp_stl --cpp-standard=11
          ${TEMPLATE_DIR}/standard_storage_manager.ksy
)

add_executable(test-cpp
  dtype.cpp
  lock.cpp
  metadata.cpp
  standard_storage_manager.cpp
  test.cpp)

target_include_directories(test-cpp
  PRIVATE ${kaitai_struct_cpp_stl_runtime_SOURCE_DIR})
target_link_libraries(test-cpp
  PRIVATE kaitai_struct_cpp_stl_runtime)
# Allows compilation to go further, but these should be fixed
target_compile_options(test-cpp PRIVATE
    $<$<CXX_COMPILER_ID:GNU>:-fpermissive>
    $<$<CXX_COMPILER_ID:Clang>:-fpermissive>
)