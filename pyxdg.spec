Summary:	Python library to access freedesktop.org standards
Name:		pyxdg
Version:	0.27
Release:	1
Group:		System/Libraries
License:	LGPLv2
Url:		http://www.freedesktop.org/Software/pyxdg
Source0:	https://github.com/takluyver/pyxdg/archive/rel-%{version}/%{name}-rel-%{version}.tar.gz
Buildarch:	noarch
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
BuildRequires:  python2dist(setuptools)

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

%package -n python2-xdg
Summary:	Python3 library to access freedesktop.org standards
Group:		System/Libraries

%description -n python2-xdg
PyXDG is a python 2 library to access freedesktop.org standards. 

%prep
%setup -qn pyxdg-rel-%{version}
mkdir ../py3build
cp -a . ../py3build
mv ../py3build .
find py3build -name '*.py' | xargs sed -i '1s|^#!python|#!python3|'

%build
%__python2 setup.py build
pushd py3build
%__python3 setup.py build
popd

%install
pushd py3build
PYTHONDONTWRITEBYTECODE= %__python3 setup.py install \
	--root=%{buildroot}
popd
PYTHONDONTWRITEBYTECODE= %__python2 setup.py install \
	--root=%{buildroot}
	

%files -n python-xdg
%doc AUTHORS COPYING ChangeLog README TODO
%{python3_sitelib}/xdg
%{python3_sitelib}/pyxdg-*.egg-info

%files -n python2-xdg
%doc AUTHORS COPYING ChangeLog README TODO
%{python2_sitelib}/xdg
%{python2_sitelib}/pyxdg-*.egg-info
