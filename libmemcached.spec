#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libmemcached
Version  : 1.0.18
Release  : 12
URL      : https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz
Source0  : https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz
Summary  : memcached C library and command line tools
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libmemcached-bin = %{version}-%{release}
Requires: libmemcached-lib = %{version}-%{release}
Requires: libmemcached-license = %{version}-%{release}
Requires: libmemcached-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : cyrus-sasl-dev
BuildRequires : flex
BuildRequires : mariadb-dev
BuildRequires : sed
BuildRequires : util-linux-dev
BuildRequires : valgrind
Patch1: 0001-fix-build.patch

%description
libmemcached, http://libmemcached.org/, is a C client library to the memcached server
(http://danga.com/memcached). It has been designed to be light on memory
usage, and provide full access to server side methods.

It also implements several command line tools:

memcat - Copy the value of a key to standard output.
memflush - Flush the contents of your servers.
memrm - Remove a key(s) from the serrver.
memstat - Dump the stats of your servers to standard output.
memslap - Generate testing loads on a memcached cluster.
memcp - Copy files to memcached servers.
memerror - Creates human readable messages from libmemecached error codes.
memcapable - Verify a memcached server for protocol behavior.
memexist - Check for the existance of a key.
memtouch - Update the expiration value of a key.

%package bin
Summary: bin components for the libmemcached package.
Group: Binaries
Requires: libmemcached-license = %{version}-%{release}

%description bin
bin components for the libmemcached package.


%package dev
Summary: dev components for the libmemcached package.
Group: Development
Requires: libmemcached-lib = %{version}-%{release}
Requires: libmemcached-bin = %{version}-%{release}
Provides: libmemcached-devel = %{version}-%{release}
Requires: libmemcached = %{version}-%{release}

%description dev
dev components for the libmemcached package.


%package lib
Summary: lib components for the libmemcached package.
Group: Libraries
Requires: libmemcached-license = %{version}-%{release}

%description lib
lib components for the libmemcached package.


%package license
Summary: license components for the libmemcached package.
Group: Default

%description license
license components for the libmemcached package.


%package man
Summary: man components for the libmemcached package.
Group: Default

%description man
man components for the libmemcached package.


%prep
%setup -q -n libmemcached-1.0.18
cd %{_builddir}/libmemcached-1.0.18
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583788463
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --disable-sasl
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1583788463
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libmemcached
cp %{_builddir}/libmemcached-1.0.18/COPYING %{buildroot}/usr/share/package-licenses/libmemcached/f18145fc8673eee689e685c226baa431f9b32eb9
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/memcapable
/usr/bin/memcat
/usr/bin/memcp
/usr/bin/memdump
/usr/bin/memerror
/usr/bin/memexist
/usr/bin/memflush
/usr/bin/memparse
/usr/bin/memping
/usr/bin/memrm
/usr/bin/memslap
/usr/bin/memstat
/usr/bin/memtouch

%files dev
%defattr(-,root,root,-)
/usr/include/libhashkit-1.0/algorithm.h
/usr/include/libhashkit-1.0/behavior.h
/usr/include/libhashkit-1.0/configure.h
/usr/include/libhashkit-1.0/digest.h
/usr/include/libhashkit-1.0/function.h
/usr/include/libhashkit-1.0/has.h
/usr/include/libhashkit-1.0/hashkit.h
/usr/include/libhashkit-1.0/hashkit.hpp
/usr/include/libhashkit-1.0/str_algorithm.h
/usr/include/libhashkit-1.0/strerror.h
/usr/include/libhashkit-1.0/string.h
/usr/include/libhashkit-1.0/types.h
/usr/include/libhashkit-1.0/visibility.h
/usr/include/libhashkit/hashkit.h
/usr/include/libmemcached-1.0/alloc.h
/usr/include/libmemcached-1.0/allocators.h
/usr/include/libmemcached-1.0/analyze.h
/usr/include/libmemcached-1.0/auto.h
/usr/include/libmemcached-1.0/basic_string.h
/usr/include/libmemcached-1.0/behavior.h
/usr/include/libmemcached-1.0/callback.h
/usr/include/libmemcached-1.0/callbacks.h
/usr/include/libmemcached-1.0/configure.h
/usr/include/libmemcached-1.0/defaults.h
/usr/include/libmemcached-1.0/delete.h
/usr/include/libmemcached-1.0/deprecated_types.h
/usr/include/libmemcached-1.0/dump.h
/usr/include/libmemcached-1.0/encoding_key.h
/usr/include/libmemcached-1.0/error.h
/usr/include/libmemcached-1.0/exception.hpp
/usr/include/libmemcached-1.0/exist.h
/usr/include/libmemcached-1.0/fetch.h
/usr/include/libmemcached-1.0/flush.h
/usr/include/libmemcached-1.0/flush_buffers.h
/usr/include/libmemcached-1.0/get.h
/usr/include/libmemcached-1.0/hash.h
/usr/include/libmemcached-1.0/limits.h
/usr/include/libmemcached-1.0/memcached.h
/usr/include/libmemcached-1.0/memcached.hpp
/usr/include/libmemcached-1.0/options.h
/usr/include/libmemcached-1.0/parse.h
/usr/include/libmemcached-1.0/platform.h
/usr/include/libmemcached-1.0/quit.h
/usr/include/libmemcached-1.0/result.h
/usr/include/libmemcached-1.0/return.h
/usr/include/libmemcached-1.0/sasl.h
/usr/include/libmemcached-1.0/server.h
/usr/include/libmemcached-1.0/server_list.h
/usr/include/libmemcached-1.0/stats.h
/usr/include/libmemcached-1.0/storage.h
/usr/include/libmemcached-1.0/strerror.h
/usr/include/libmemcached-1.0/struct/allocator.h
/usr/include/libmemcached-1.0/struct/analysis.h
/usr/include/libmemcached-1.0/struct/callback.h
/usr/include/libmemcached-1.0/struct/memcached.h
/usr/include/libmemcached-1.0/struct/result.h
/usr/include/libmemcached-1.0/struct/sasl.h
/usr/include/libmemcached-1.0/struct/server.h
/usr/include/libmemcached-1.0/struct/stat.h
/usr/include/libmemcached-1.0/struct/string.h
/usr/include/libmemcached-1.0/touch.h
/usr/include/libmemcached-1.0/triggers.h
/usr/include/libmemcached-1.0/types.h
/usr/include/libmemcached-1.0/types/behavior.h
/usr/include/libmemcached-1.0/types/callback.h
/usr/include/libmemcached-1.0/types/connection.h
/usr/include/libmemcached-1.0/types/hash.h
/usr/include/libmemcached-1.0/types/return.h
/usr/include/libmemcached-1.0/types/server_distribution.h
/usr/include/libmemcached-1.0/verbosity.h
/usr/include/libmemcached-1.0/version.h
/usr/include/libmemcached-1.0/visibility.h
/usr/include/libmemcached/memcached.h
/usr/include/libmemcached/memcached.hpp
/usr/include/libmemcached/util.h
/usr/include/libmemcachedutil-1.0/flush.h
/usr/include/libmemcachedutil-1.0/ostream.hpp
/usr/include/libmemcachedutil-1.0/pid.h
/usr/include/libmemcachedutil-1.0/ping.h
/usr/include/libmemcachedutil-1.0/pool.h
/usr/include/libmemcachedutil-1.0/util.h
/usr/include/libmemcachedutil-1.0/version.h
/usr/lib64/libhashkit.so
/usr/lib64/libmemcached.so
/usr/lib64/libmemcachedutil.so
/usr/lib64/pkgconfig/libmemcached.pc
/usr/share/aclocal/*.m4
/usr/share/man/man3/hashkit_clone.3
/usr/share/man/man3/hashkit_crc32.3
/usr/share/man/man3/hashkit_create.3
/usr/share/man/man3/hashkit_fnv1_32.3
/usr/share/man/man3/hashkit_fnv1_64.3
/usr/share/man/man3/hashkit_fnv1a_32.3
/usr/share/man/man3/hashkit_fnv1a_64.3
/usr/share/man/man3/hashkit_free.3
/usr/share/man/man3/hashkit_functions.3
/usr/share/man/man3/hashkit_hsieh.3
/usr/share/man/man3/hashkit_is_allocated.3
/usr/share/man/man3/hashkit_jenkins.3
/usr/share/man/man3/hashkit_md5.3
/usr/share/man/man3/hashkit_murmur.3
/usr/share/man/man3/hashkit_value.3
/usr/share/man/man3/libhashkit.3
/usr/share/man/man3/libmemcached.3
/usr/share/man/man3/libmemcached_check_configuration.3
/usr/share/man/man3/libmemcached_configuration.3
/usr/share/man/man3/libmemcached_examples.3
/usr/share/man/man3/libmemcachedutil.3
/usr/share/man/man3/memcached.3
/usr/share/man/man3/memcached_add.3
/usr/share/man/man3/memcached_add_by_key.3
/usr/share/man/man3/memcached_analyze.3
/usr/share/man/man3/memcached_append.3
/usr/share/man/man3/memcached_append_by_key.3
/usr/share/man/man3/memcached_behavior_get.3
/usr/share/man/man3/memcached_behavior_set.3
/usr/share/man/man3/memcached_callback_get.3
/usr/share/man/man3/memcached_callback_set.3
/usr/share/man/man3/memcached_cas.3
/usr/share/man/man3/memcached_cas_by_key.3
/usr/share/man/man3/memcached_clone.3
/usr/share/man/man3/memcached_create.3
/usr/share/man/man3/memcached_decrement.3
/usr/share/man/man3/memcached_decrement_with_initial.3
/usr/share/man/man3/memcached_delete.3
/usr/share/man/man3/memcached_delete_by_key.3
/usr/share/man/man3/memcached_destroy_sasl_auth_data.3
/usr/share/man/man3/memcached_dump.3
/usr/share/man/man3/memcached_exist.3
/usr/share/man/man3/memcached_exist_by_key.3
/usr/share/man/man3/memcached_fetch.3
/usr/share/man/man3/memcached_fetch_execute.3
/usr/share/man/man3/memcached_fetch_result.3
/usr/share/man/man3/memcached_flush_buffers.3
/usr/share/man/man3/memcached_free.3
/usr/share/man/man3/memcached_generate_hash.3
/usr/share/man/man3/memcached_generate_hash_value.3
/usr/share/man/man3/memcached_get.3
/usr/share/man/man3/memcached_get_by_key.3
/usr/share/man/man3/memcached_get_memory_allocators.3
/usr/share/man/man3/memcached_get_sasl_callbacks.3
/usr/share/man/man3/memcached_get_user_data.3
/usr/share/man/man3/memcached_increment.3
/usr/share/man/man3/memcached_increment_with_initial.3
/usr/share/man/man3/memcached_last_error_message.3
/usr/share/man/man3/memcached_lib_version.3
/usr/share/man/man3/memcached_mget.3
/usr/share/man/man3/memcached_mget_by_key.3
/usr/share/man/man3/memcached_mget_execute.3
/usr/share/man/man3/memcached_mget_execute_by_key.3
/usr/share/man/man3/memcached_pool.3
/usr/share/man/man3/memcached_pool_behavior_get.3
/usr/share/man/man3/memcached_pool_behavior_set.3
/usr/share/man/man3/memcached_pool_create.3
/usr/share/man/man3/memcached_pool_destroy.3
/usr/share/man/man3/memcached_pool_fetch.3
/usr/share/man/man3/memcached_pool_pop.3
/usr/share/man/man3/memcached_pool_push.3
/usr/share/man/man3/memcached_pool_release.3
/usr/share/man/man3/memcached_pool_st.3
/usr/share/man/man3/memcached_prepend.3
/usr/share/man/man3/memcached_prepend_by_key.3
/usr/share/man/man3/memcached_quit.3
/usr/share/man/man3/memcached_replace.3
/usr/share/man/man3/memcached_replace_by_key.3
/usr/share/man/man3/memcached_sasl_set_auth_data.3
/usr/share/man/man3/memcached_server_add.3
/usr/share/man/man3/memcached_server_count.3
/usr/share/man/man3/memcached_server_cursor.3
/usr/share/man/man3/memcached_server_list.3
/usr/share/man/man3/memcached_server_list_append.3
/usr/share/man/man3/memcached_server_list_count.3
/usr/share/man/man3/memcached_server_list_free.3
/usr/share/man/man3/memcached_server_push.3
/usr/share/man/man3/memcached_servers_parse.3
/usr/share/man/man3/memcached_set.3
/usr/share/man/man3/memcached_set_by_key.3
/usr/share/man/man3/memcached_set_memory_allocators.3
/usr/share/man/man3/memcached_set_sasl_callbacks.3
/usr/share/man/man3/memcached_set_user_data.3
/usr/share/man/man3/memcached_stat.3
/usr/share/man/man3/memcached_stat_execute.3
/usr/share/man/man3/memcached_stat_get_keys.3
/usr/share/man/man3/memcached_stat_get_value.3
/usr/share/man/man3/memcached_stat_servername.3
/usr/share/man/man3/memcached_strerror.3
/usr/share/man/man3/memcached_touch.3
/usr/share/man/man3/memcached_touch_by_key.3
/usr/share/man/man3/memcached_verbosity.3
/usr/share/man/man3/memcached_version.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libhashkit.so.2
/usr/lib64/libhashkit.so.2.0.0
/usr/lib64/libmemcached.so.11
/usr/lib64/libmemcached.so.11.0.0
/usr/lib64/libmemcachedutil.so.2
/usr/lib64/libmemcachedutil.so.2.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libmemcached/f18145fc8673eee689e685c226baa431f9b32eb9

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/memaslap.1
/usr/share/man/man1/memcapable.1
/usr/share/man/man1/memcat.1
/usr/share/man/man1/memcp.1
/usr/share/man/man1/memdump.1
/usr/share/man/man1/memerror.1
/usr/share/man/man1/memexist.1
/usr/share/man/man1/memflush.1
/usr/share/man/man1/memparse.1
/usr/share/man/man1/memping.1
/usr/share/man/man1/memrm.1
/usr/share/man/man1/memslap.1
/usr/share/man/man1/memstat.1
/usr/share/man/man1/memtouch.1
