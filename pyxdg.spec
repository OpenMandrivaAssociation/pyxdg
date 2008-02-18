#%define installdir /usr/lib/python2.3/site-packages/xdg
%define name      pyxdg
%define version 0.15
%define release %mkrel 4

Name:             %{name}
Summary:          Python library to access freedesktop.org standards
Version:          %{version}
Release:          %{release}
Buildarch:        noarch
Source0:          %{name}-%{version}.tar.bz2
URL:              http://www.freedesktop.org/Software/pyxdg
Group:            System/Libraries
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:          LGPL
Requires:         python >= 2.3 
BuildRequires:    python-devel

%description
PyXDG is a python library to access freedesktop.org standards. 
Currently supported are:

	* Base Directory Specification Version 0.6 

	* Menu Specification Version 1.0-draft1 

	* Desktop Entry Specification Version 0.9.4 

	* Icon Theme Specification Version 0.8 

	* Recent File Spec 0.2 

	* Shared-MIME-Database Specification 0.13 



%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO


