Summary:	Python library to access freedesktop.org standards
Name:		pyxdg
Version:	0.28
Release:	3
Group:		System/Libraries
License:	LGPLv2
Url:		https://www.freedesktop.org/Software/pyxdg
Source0:	https://github.com/takluyver/pyxdg/archive/rel-%{version}/%{name}-rel-%{version}.tar.gz
Buildarch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(pip)

%description
PyXDG is a python library to access freedesktop.org standards. 
Currently supported are:
	* Base Directory Specification Version 0.6 
	* Menu Specification Version 1.0 
	* Desktop Entry Specification Version 1.0 
	* Icon Theme Specification Version 0.8 
	* Recent File Spec 0.2 
	* Shared-MIME-Database Specification 0.13 

%package -n python-xdg
Summary:	Python library to access freedesktop.org standards
Group:		System/Libraries
# both pkgs improperly named
%rename		python-pyxdg
%rename		pyxdg
%rename		python3-xdg

%description -n python-xdg
PyXDG is a python library to access freedesktop.org standards. 
Currently supported are:
	* Base Directory Specification Version 0.6 
	* Menu Specification Version 1.0 
	* Desktop Entry Specification Version 1.0 
	* Icon Theme Specification Version 0.8 
	* Recent File Spec 0.2 
	* Shared-MIME-Database Specification 0.13 

%prep
%autosetup -p1 -n pyxdg-rel-%{version}

%build
%py_build

%install
%py_install

%files -n python-xdg
%doc AUTHORS COPYING ChangeLog README TODO
%{python3_sitelib}/xdg
%{python3_sitelib}/pyxdg-*.egg-info
