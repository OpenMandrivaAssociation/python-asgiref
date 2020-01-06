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
Version:        3.2.2
Release:        1%{?dist}
Summary:        ASGI specs, helper code, and adapters
# This is BSD + bundled async-timeout ASL 2.0
License:        BSD and ASL 2.0
URL:            https://github.com/django/asgiref
# PyPI tarball doesn't have tests
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch


%description %{_description}


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-pytest >= 3.3
BuildRequires:  python3-pytest-asyncio
%endif
# https://github.com/django/asgiref/commit/9c6df6e02700092eb19adefff3552d44388f69b8
Provides:       bundled(python3dist(async-timeout)) == 3.0.1
%{?python_provide:%python_provide python3-%{pkgname}}


%description -n python3-%{pkgname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} --verbose tests
%endif


%files -n python3-%{pkgname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Sep 16 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.2-1
- Update to 3.2.2 (#1691128)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Carl George <carl@george.computer> - 2.3.2-1
- Initial package
