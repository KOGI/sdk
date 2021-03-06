# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

# This file contains all C++ sources for the dart:_builtin library and
# some of the C++ sources for the dart:io library.  The rest are in
# io_impl_sources.gypi.
{
  'sources': [
    'crypto.cc',
    'crypto.h',
    'crypto_android.cc',
    'crypto_fuchsia.cc',
    'crypto_linux.cc',
    'crypto_macos.cc',
    'crypto_test.cc',
    'crypto_win.cc',
    'builtin_common.cc',
    'dartutils.cc',
    'dartutils.h',
    'directory.cc',
    'directory.h',
    'directory_android.cc',
    'directory_fuchsia.cc',
    'directory_linux.cc',
    'directory_macos.cc',
    'directory_test.cc',
    'directory_unsupported.cc',
    'directory_win.cc',
    'eventhandler_test.cc',
    'extensions.h',
    'extensions.cc',
    'extensions_android.cc',
    'extensions_fuchsia.cc',
    'extensions_linux.cc',
    'extensions_macos.cc',
    'extensions_win.cc',
    'fdutils.h',
    'fdutils_android.cc',
    'fdutils_linux.cc',
    'fdutils_macos.cc',
    'file.cc',
    'file.h',
    'file_android.cc',
    'file_fuchsia.cc',
    'file_linux.cc',
    'file_macos.cc',
    'file_support.cc',
    'file_unsupported.cc',
    'file_test.cc',
    'file_win.cc',
    'hashmap_test.cc',
    'io_buffer.cc',
    'io_buffer.h',
    'isolate_data.h',
    'loader.cc',
    'loader.h',
    'lockers.h',
    'thread.h',
    'thread_android.cc',
    'thread_android.h',
    'thread_fuchsia.cc',
    'thread_fuchsia.h',
    'thread_linux.cc',
    'thread_linux.h',
    'thread_macos.cc',
    'thread_macos.h',
    'thread_win.cc',
    'thread_win.h',
    'utils.h',
    'utils_android.cc',
    'utils_fuchsia.cc',
    'utils_linux.cc',
    'utils_macos.cc',
    'utils_win.cc',
    'utils_win.h',
  ],
}
