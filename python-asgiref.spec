%global srcname asgiref

Name:		python-%{srcname}
Version:	3.8.1
Release:	1
Summary:	ASGI specs, helper code, and adapters
# This is BSD + bundled async-timeout ASL 2.0
License:	BSD and ASL 2.0
URL:		https://github.com/django/asgiref
# PyPI tarball doesn't have tests
Source0:	%{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools

%{?python_provide:%python_provide python-%{srcname}}

%description
ASGI is a standard for Python asynchronous web apps and servers to communicate
with each other, and positioned as an asynchronous successor to WSGI.  This
package includes ASGI base libraries, such as:

* Sync-to-async and async-to-sync function wrappers, asgiref.sync
* Server base classes, asgiref.server
* A WSGI-to-ASGI adapter, in asgiref.wsgi

%prep
%autosetup -n %{srcname}-%{version}

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/%{srcname}
%{python_sitelib}/%{srcname}-%{version}-py*.egg-info
