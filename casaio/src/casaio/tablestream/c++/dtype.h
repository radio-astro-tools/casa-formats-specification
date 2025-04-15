#pragma once

// This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

#include "kaitai/kaitaistruct.h"
#include <stdint.h>
#include <memory>

#if KAITAI_STRUCT_VERSION < 9000L
#error "Incompatible Kaitai Struct C++/STL API: version 0.9 or later is required"
#endif

/**
 * User defined version of base numerical data types. This will allow for the
 * compilation of languages like c++ and rust
 */

class dtype_t : public kaitai::kstruct {

public:
    class float4_t;
    class int8_t;
    class uint8_t;
    class uint2_t;
    class bool1_t;
    class string_t;
    class float8_t;
    class complex8_t;
    class int1_t;
    class int4_t;
    class int2_t;
    class uint4_t;
    class uint1_t;
    class complex16_t;

    dtype_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, dtype_t* p__root = nullptr);

private:
    void _read();
    void _clean_up();

public:
    ~dtype_t();

    class float4_t : public kaitai::kstruct {

    public:

        float4_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, dtype_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~float4_t();

    private:
        float m_value;
        dtype_t* m__root;
        kaitai::kstruct* m__parent;

    public:
        float value() const { return m_value; }
        dtype_t* _root() const { return m__root; }
        kaitai::kstruct* _parent() const { return m__parent; }
    };

    class int8_t : public kaitai::kstruct {

    public:

        int8_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, dtype_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~int8_t();

    private:
        int64_t m_value;
        dtype_t* m__root;
        kaitai::kstruct* m__parent;

    public:
        int64_t value() const { return m_value; }
        dtype_t* _root() const { return m__root; }
        kaitai::kstruct* _parent() const { return m__parent; }
    };

    class uint8_t : public kaitai::kstruct {

    public:

        uint8_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, dtype_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~uint8_t();

    private:
        uint64_t m_value;
        dtype_t* m__root;
        kaitai::kstruct* m__parent;

    public:
        uint64_t value() const { return m_value; }
        dtype_t* _root() const { return m__root; }
        kaitai::kstruct* _parent() const { return m__parent; }
    };

    class uint2_t : public kaitai::kstruct {

    public:

        uint2_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, dtype_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~uint2_t();

    private:
        uint16_t m_value;
        dtype_t* m__root;
        kaitai::kstruct* m__parent;

    public:
        uint16_t value() const { return m_value; }
        dtype_t* _root() const { return m__root; }
        kaitai::kstruct* _parent() const { return m__parent; }
    };

    class bool1_t : public kaitai::kstruct {

    public:

        bool1_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, dtype_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~bool1_t();

    private:
        bool m_value;
        dtype_t* m__root;
        kaitai::kstruct* m__parent;

    public:
        bool value() const { return m_value; }
        dtype_t* _root() const { return m__root; }
        kaitai::kstruct* _parent() const { return m__parent; }
    };

    class string_t : public kaitai::kstruct {

    public:

        string_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, dtype_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~string_t();

    private:
        uint32_t m_length;
        std::string m_value;
        dtype_t* m__root;
        kaitai::kstruct* m__parent;

    public:
        uint32_t length() const { return m_length; }
        std::string value() const { return m_value; }
        dtype_t* _root() const { return m__root; }
        kaitai::kstruct* _parent() const { return m__parent; }
    };

    class float8_t : public kaitai::kstruct {

    public:

        float8_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, dtype_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~float8_t();

    private:
        double m_value;
        dtype_t* m__root;
        kaitai::kstruct* m__parent;

    public:
        double value() const { return m_value; }
        dtype_t* _root() const { return m__root; }
        kaitai::kstruct* _parent() const { return m__parent; }
    };

    class complex8_t : public kaitai::kstruct {

    public:

        complex8_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, dtype_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~complex8_t();

    private:
        float m_real;
        float m_imaginary;
        dtype_t* m__root;
        kaitai::kstruct* m__parent;

    public:
        float real() const { return m_real; }
        float imaginary() const { return m_imaginary; }
        dtype_t* _root() const { return m__root; }
        kaitai::kstruct* _parent() const { return m__parent; }
    };

    class int1_t : public kaitai::kstruct {

    public:

        int1_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, dtype_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~int1_t();

    private:
        int8_t m_value;
        dtype_t* m__root;
        kaitai::kstruct* m__parent;

    public:
        int8_t value() const { return m_value; }
        dtype_t* _root() const { return m__root; }
        kaitai::kstruct* _parent() const { return m__parent; }
    };

    class int4_t : public kaitai::kstruct {

    public:

        int4_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, dtype_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~int4_t();

    private:
        int32_t m_value;
        dtype_t* m__root;
        kaitai::kstruct* m__parent;

    public:
        int32_t value() const { return m_value; }
        dtype_t* _root() const { return m__root; }
        kaitai::kstruct* _parent() const { return m__parent; }
    };

    class int2_t : public kaitai::kstruct {

    public:

        int2_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, dtype_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~int2_t();

    private:
        int16_t m_value;
        dtype_t* m__root;
        kaitai::kstruct* m__parent;

    public:
        int16_t value() const { return m_value; }
        dtype_t* _root() const { return m__root; }
        kaitai::kstruct* _parent() const { return m__parent; }
    };

    class uint4_t : public kaitai::kstruct {

    public:

        uint4_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, dtype_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~uint4_t();

    private:
        uint32_t m_value;
        dtype_t* m__root;
        kaitai::kstruct* m__parent;

    public:
        uint32_t value() const { return m_value; }
        dtype_t* _root() const { return m__root; }
        kaitai::kstruct* _parent() const { return m__parent; }
    };

    class uint1_t : public kaitai::kstruct {

    public:

        uint1_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, dtype_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~uint1_t();

    private:
        uint8_t m_value;
        dtype_t* m__root;
        kaitai::kstruct* m__parent;

    public:
        uint8_t value() const { return m_value; }
        dtype_t* _root() const { return m__root; }
        kaitai::kstruct* _parent() const { return m__parent; }
    };

    class complex16_t : public kaitai::kstruct {

    public:

        complex16_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = nullptr, dtype_t* p__root = nullptr);

    private:
        void _read();
        void _clean_up();

    public:
        ~complex16_t();

    private:
        double m_real;
        double m_imaginary;
        dtype_t* m__root;
        kaitai::kstruct* m__parent;

    public:
        double real() const { return m_real; }
        double imaginary() const { return m_imaginary; }
        dtype_t* _root() const { return m__root; }
        kaitai::kstruct* _parent() const { return m__parent; }
    };

private:
    dtype_t* m__root;
    kaitai::kstruct* m__parent;

public:
    dtype_t* _root() const { return m__root; }
    kaitai::kstruct* _parent() const { return m__parent; }
};
