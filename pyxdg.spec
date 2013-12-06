Summary:	Python library to access freedesktop.org standards
Name:		pyxdg
Version:	0.19
Release:	7
Group:		System/Libraries
License:	LGPLv2
Url:		http://www.freedesktop.org/Software/pyxdg
Source0:	http://www.freedesktop.org/~lanius/%{name}-%{version}.tar.gz
Buildarch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(python3)

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

%description -n python-xdg
PyXDG is a python library to access freedesktop.org standards. 
Currently supported are:
	* Base Directory Specification Version 0.6 
	* Menu Specification Version 1.0 
	* Desktop Entry Specification Version 1.0 
	* Icon Theme Specification Version 0.8 
	* Recent File Spec 0.2 
	* Shared-MIME-Database Specification 0.13 

%package -n python3-xdg
Summary:	Python3 library to access freedesktop.org standards
Group:		System/Libraries

%description -n python3-xdg
PyXDG is a python3 library to access freedesktop.org standards. 

%prep
%setup -q
mkdir ../py3build
cp -a . ../py3build
mv ../py3build .
find py3build -name '*.py' | xargs sed -i '1s|^#!python|#!python3|'

%build
python setup.py build
pushd py3build
python3 setup.py build
popd

%install
PYTHONDONTWRITEBYTECODE= python setup.py install \
	--root=%{buildroot} \
	--record=INSTALLED_FILES
pushd py3build
PYTHONDONTWRITEBYTECODE= python3 setup.py install \
	--root=%{buildroot}
	

%files -n python-xdg -f INSTALLED_FILES
%doc AUTHORS COPYING ChangeLog README TODO

%files -n python3-xdg
%doc AUTHORS COPYING ChangeLog README TODO
%{python3_sitelib}/xdg
%{python3_sitelib}/pyxdg-*.egg-info

