Summary:	Python library to access freedesktop.org standards
Name:		pyxdg
Version:	0.19
Release:	4
Group:		System/Libraries
License:	LGPLv2
Url:		http://www.freedesktop.org/Software/pyxdg
Source0:	http://www.freedesktop.org/~lanius/%{name}-%{version}.tar.gz
Buildarch:	noarch
BuildRequires:	pkgconfig(python)

%description
PyXDG is a python library to access freedesktop.org standards. 
Currently supported are:
	* Base Directory Specification Version 0.6 
	* Menu Specification Version 1.0 
	* Desktop Entry Specification Version 1.0 
	* Icon Theme Specification Version 0.8 
	* Recent File Spec 0.2 
	* Shared-MIME-Database Specification 0.13 

%prep
%setup -q

%build
python setup.py build

%install
PYTHONDONTWRITEBYTECODE= python setup.py install \
	--root=%{buildroot} \
	--record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc AUTHORS COPYING ChangeLog README TODO

