# what it's called on pypi
%global srcname asgiref
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global _description \
ASGI is a standard for Python asynchronous web apps and servers to communicate\
with each other, and positioned as an asynchronous successor to WSGI.  This\
package includes ASGI base libraries, such as:\
\
* Sync-to-async and async-to-sync function wrappers, asgiref.sync\
* Server base classes, asgiref.server\
* A WSGI-to-ASGI adapter, in asgiref.wsgi

%bcond_without tests


Name:           python-%{pkgname}
Version:        3.2.3
Release:        1
Summary:        ASGI specs, helper code, and adapters
# This is BSD + bundled async-timeout ASL 2.0
License:        BSD and ASL 2.0
URL:            https://github.com/django/asgiref
# PyPI tarball doesn't have tests
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description %{_description}

%package -n python-%{pkgname}
Summary:        %{summary}
BuildRequires:  python-devel
BuildRequires:  python-setuptools
%if %{with tests}
BuildRequires:  python-pytest >= 3.3
BuildRequires:  python-pytest-asyncio
%endif
# https://github.com/django/asgiref/commit/9c6df6e02700092eb19adefff3552d44388f69b8
Provides:       bundled(python3dist(async-timeout)) == 3.0.1
%{?python_provide:%python_provide python-%{pkgname}}

%description -n python3-%{pkgname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py_build

%install
%py_install

%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python_sitelib} py.test-%{python_version} --verbose tests
%endif

%files -n python-%{pkgname}
%license LICENSE
%doc README.rst
%{python_sitelib}/%{libname}
%{python_sitelib}/%{eggname}-%{version}-py%{python_version}.egg-info
