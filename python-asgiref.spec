%global module asgiref

Name:		python-asgiref
Version:	3.11.1
Release:	1
Summary:	ASGI specs, helper code, and adapters
# This is BSD + bundled async-timeout ASL 2.0
License:	BSD-3-Clause AND ASL 2.0
URL:		https://github.com/django/asgiref
# PyPI tarball doesn't have tests
Source0:	%{url}/archive/%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
Requires:	python%{pyver}dist(typing-extensions) >= 4

%{?python_provide:%python_provide python-%{module}}

%description
ASGI is a standard for Python asynchronous web apps and servers to communicate
with each other, and positioned as an asynchronous successor to WSGI.  This
package includes ASGI base libraries, such as:

* Sync-to-async and async-to-sync function wrappers, asgiref.sync
* Server base classes, asgiref.server
* A WSGI-to-ASGI adapter, in asgiref.wsgi

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}*.*-info
