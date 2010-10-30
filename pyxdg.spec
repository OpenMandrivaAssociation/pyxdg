%define name      pyxdg
%define version 0.19
%define release %mkrel 2

Name:             %{name}
Summary:          Python library to access freedesktop.org standards
Version:          %{version}
Release:          %{release}
Buildarch:        noarch
Source0:          http://www.freedesktop.org/~lanius/%{name}-%{version}.tar.gz
URL:              http://www.freedesktop.org/Software/pyxdg
Group:            System/Libraries
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:          LGPLv2
BuildRequires:    python-devel

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
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO
