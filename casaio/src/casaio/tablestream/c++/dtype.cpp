// This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

#include "dtype.h"

dtype_t::dtype_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, dtype_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = this;
    _read();
}

void dtype_t::_read() {
}

dtype_t::~dtype_t() {
    _clean_up();
}

void dtype_t::_clean_up() {
}

dtype_t::float4_t::float4_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, dtype_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    _read();
}

void dtype_t::float4_t::_read() {
    m_value = m__io->read_f4be();
}

dtype_t::float4_t::~float4_t() {
    _clean_up();
}

void dtype_t::float4_t::_clean_up() {
}

dtype_t::int8_t::int8_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, dtype_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    _read();
}

void dtype_t::int8_t::_read() {
    m_value = m__io->read_s8be();
}

dtype_t::int8_t::~int8_t() {
    _clean_up();
}

void dtype_t::int8_t::_clean_up() {
}

dtype_t::uint8_t::uint8_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, dtype_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    _read();
}

void dtype_t::uint8_t::_read() {
    m_value = m__io->read_u8be();
}

dtype_t::uint8_t::~uint8_t() {
    _clean_up();
}

void dtype_t::uint8_t::_clean_up() {
}

dtype_t::uint2_t::uint2_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, dtype_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    _read();
}

void dtype_t::uint2_t::_read() {
    m_value = m__io->read_u2be();
}

dtype_t::uint2_t::~uint2_t() {
    _clean_up();
}

void dtype_t::uint2_t::_clean_up() {
}

dtype_t::bool1_t::bool1_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, dtype_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    _read();
}

void dtype_t::bool1_t::_read() {
    m_value = m__io->read_bits_int_be(1);
}

dtype_t::bool1_t::~bool1_t() {
    _clean_up();
}

void dtype_t::bool1_t::_clean_up() {
}

dtype_t::string_t::string_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, dtype_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    _read();
}

void dtype_t::string_t::_read() {
    m_length = m__io->read_u4be();
    m_value = kaitai::kstream::bytes_to_str(m__io->read_bytes(length()), std::string("ASCII"));
}

dtype_t::string_t::~string_t() {
    _clean_up();
}

void dtype_t::string_t::_clean_up() {
}

dtype_t::float8_t::float8_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, dtype_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    _read();
}

void dtype_t::float8_t::_read() {
    m_value = m__io->read_f8be();
}

dtype_t::float8_t::~float8_t() {
    _clean_up();
}

void dtype_t::float8_t::_clean_up() {
}

dtype_t::complex8_t::complex8_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, dtype_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    _read();
}

void dtype_t::complex8_t::_read() {
    m_real = m__io->read_f4be();
    m_imaginary = m__io->read_f4be();
}

dtype_t::complex8_t::~complex8_t() {
    _clean_up();
}

void dtype_t::complex8_t::_clean_up() {
}

dtype_t::int1_t::int1_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, dtype_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    _read();
}

void dtype_t::int1_t::_read() {
    m_value = m__io->read_s1();
}

dtype_t::int1_t::~int1_t() {
    _clean_up();
}

void dtype_t::int1_t::_clean_up() {
}

dtype_t::int4_t::int4_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, dtype_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    _read();
}

void dtype_t::int4_t::_read() {
    m_value = m__io->read_s4be();
}

dtype_t::int4_t::~int4_t() {
    _clean_up();
}

void dtype_t::int4_t::_clean_up() {
}

dtype_t::int2_t::int2_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, dtype_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    _read();
}

void dtype_t::int2_t::_read() {
    m_value = m__io->read_s2be();
}

dtype_t::int2_t::~int2_t() {
    _clean_up();
}

void dtype_t::int2_t::_clean_up() {
}

dtype_t::uint4_t::uint4_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, dtype_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    _read();
}

void dtype_t::uint4_t::_read() {
    m_value = m__io->read_u4be();
}

dtype_t::uint4_t::~uint4_t() {
    _clean_up();
}

void dtype_t::uint4_t::_clean_up() {
}

dtype_t::uint1_t::uint1_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, dtype_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    _read();
}

void dtype_t::uint1_t::_read() {
    m_value = m__io->read_u1();
}

dtype_t::uint1_t::~uint1_t() {
    _clean_up();
}

void dtype_t::uint1_t::_clean_up() {
}

dtype_t::complex16_t::complex16_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent, dtype_t* p__root) : kaitai::kstruct(p__io) {
    m__parent = p__parent;
    m__root = p__root;
    _read();
}

void dtype_t::complex16_t::_read() {
    m_real = m__io->read_f8be();
    m_imaginary = m__io->read_f8be();
}

dtype_t::complex16_t::~complex16_t() {
    _clean_up();
}

void dtype_t::complex16_t::_clean_up() {
}
