#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cytoolz
Version  : 0.11.2
Release  : 5
URL      : https://files.pythonhosted.org/packages/b7/a9/9437d8e6a8ba420cb52832a4895614c61bf574bfb3978d5b0806b8ab95be/cytoolz-0.11.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/b7/a9/9437d8e6a8ba420cb52832a4895614c61bf574bfb3978d5b0806b8ab95be/cytoolz-0.11.2.tar.gz
Summary  : Cython implementation of Toolz: High performance functional utilities
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-cytoolz-filemap = %{version}-%{release}
Requires: pypi-cytoolz-lib = %{version}-%{release}
Requires: pypi-cytoolz-license = %{version}-%{release}
Requires: pypi-cytoolz-python = %{version}-%{release}
Requires: pypi-cytoolz-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(toolz)

%description
CyToolz
=======
|Build Status| |Version Status|
Cython implementation of the
|literal toolz|_ `package, <https://pypi.python.org/pypi/toolz/>`__ which
provides high performance utility functions for iterables, functions,
and dictionaries.

%package filemap
Summary: filemap components for the pypi-cytoolz package.
Group: Default

%description filemap
filemap components for the pypi-cytoolz package.


%package lib
Summary: lib components for the pypi-cytoolz package.
Group: Libraries
Requires: pypi-cytoolz-license = %{version}-%{release}
Requires: pypi-cytoolz-filemap = %{version}-%{release}

%description lib
lib components for the pypi-cytoolz package.


%package license
Summary: license components for the pypi-cytoolz package.
Group: Default

%description license
license components for the pypi-cytoolz package.


%package python
Summary: python components for the pypi-cytoolz package.
Group: Default
Requires: pypi-cytoolz-python3 = %{version}-%{release}

%description python
python components for the pypi-cytoolz package.


%package python3
Summary: python3 components for the pypi-cytoolz package.
Group: Default
Requires: pypi-cytoolz-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(cytoolz)
Requires: pypi(toolz)

%description python3
python3 components for the pypi-cytoolz package.


%prep
%setup -q -n cytoolz-0.11.2
cd %{_builddir}/cytoolz-0.11.2
pushd ..
cp -a cytoolz-0.11.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656372972
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cytoolz
cp %{_builddir}/cytoolz-0.11.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-cytoolz/84a923202781778b1726c702c36c25eb8660e50b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-cytoolz

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cytoolz/84a923202781778b1726c702c36c25eb8660e50b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
