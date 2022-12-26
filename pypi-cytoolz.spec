#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cytoolz
Version  : 0.12.1
Release  : 13
URL      : https://files.pythonhosted.org/packages/da/89/66bac516a236af8375dd7af2b3032a210e222395670758da4b2439b37e40/cytoolz-0.12.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/da/89/66bac516a236af8375dd7af2b3032a210e222395670758da4b2439b37e40/cytoolz-0.12.1.tar.gz
Summary  : Cython implementation of Toolz: High performance functional utilities
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-cytoolz-filemap = %{version}-%{release}
Requires: pypi-cytoolz-lib = %{version}-%{release}
Requires: pypi-cytoolz-license = %{version}-%{release}
Requires: pypi-cytoolz-python = %{version}-%{release}
Requires: pypi-cytoolz-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cython)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(toolz)
BuildRequires : pypi(wheel)

%description
=======
        
        |Build Status| |Version Status|
        
        Cython implementation of the

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
%setup -q -n cytoolz-0.12.1
cd %{_builddir}/cytoolz-0.12.1
pushd ..
cp -a cytoolz-0.12.1 buildavx2
cp -a cytoolz-0.12.1 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672080735
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cytoolz
cp %{_builddir}/cytoolz-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-cytoolz/7c3eaacb1ccf909587afcc407329b7a8e091827d
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
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
/usr/share/package-licenses/pypi-cytoolz/7c3eaacb1ccf909587afcc407329b7a8e091827d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
