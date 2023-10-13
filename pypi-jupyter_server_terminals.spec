#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jupyter_server_terminals
Version  : 0.4.3
Release  : 3
URL      : https://files.pythonhosted.org/packages/7b/91/5d21682a41496a4150d120eea74b2b4c6b3dc2401d3aebe1e5cbd87e1889/jupyter_server_terminals-0.4.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/7b/91/5d21682a41496a4150d120eea74b2b4c6b3dc2401d3aebe1e5cbd87e1889/jupyter_server_terminals-0.4.3.tar.gz
Summary  : A Jupyter Server Extension Providing Terminals.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-jupyter_server_terminals-license = %{version}-%{release}
Requires: pypi-jupyter_server_terminals-python = %{version}-%{release}
Requires: pypi-jupyter_server_terminals-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Jupyter Server Terminals
[![Build Status](https://github.com/jupyter-server/jupyter_server_terminals/actions/workflows/test.yml/badge.svg?query=branch%3Amain++)](https://github.com/jupyter-server/jupyter_server_terminals/actions?query=branch%3Amain++)
[![codecov](https://codecov.io/gh/jupyter-server/jupyter_server_terminals/branch/main/graph/badge.svg?token=6OPBSEMMUG)](https://codecov.io/gh/jupyter-server/jupyter_server_terminals)
[![Documentation Status](https://readthedocs.org/projects/jupyter-server-terminals/badge/?version=latest)](http://jupyter-server-terminals.readthedocs.io/en/latest/?badge=latest)

%package license
Summary: license components for the pypi-jupyter_server_terminals package.
Group: Default

%description license
license components for the pypi-jupyter_server_terminals package.


%package python
Summary: python components for the pypi-jupyter_server_terminals package.
Group: Default
Requires: pypi-jupyter_server_terminals-python3 = %{version}-%{release}

%description python
python components for the pypi-jupyter_server_terminals package.


%package python3
Summary: python3 components for the pypi-jupyter_server_terminals package.
Group: Default
Requires: python3-core
Provides: pypi(jupyter_server_terminals)
Requires: pypi(terminado)

%description python3
python3 components for the pypi-jupyter_server_terminals package.


%prep
%setup -q -n jupyter_server_terminals-0.4.3
cd %{_builddir}/jupyter_server_terminals-0.4.3
pushd ..
cp -a jupyter_server_terminals-0.4.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672328398
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyter_server_terminals
cp %{_builddir}/jupyter_server_terminals-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jupyter_server_terminals/4a5864c452ca0637282cf814d0dd3cd6b368edd7 || :
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
## Remove excluded files
rm -f %{buildroot}*/usr/etc/jupyter/jupyter_server_config.d/jupyter_server_terminals.json
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupyter_server_terminals/4a5864c452ca0637282cf814d0dd3cd6b368edd7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
