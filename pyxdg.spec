%define name      pyxdg
%define version 0.19
%define release %mkrel 4

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


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.19-3mdv2011.0
+ Revision: 668053
- mass rebuild

* Sat Oct 30 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.19-2mdv2011.0
+ Revision: 590401
- rebuild for python-2.7
- remove py_requires macro and use python-devel (in accordance with latest changes
  in rpm-mandriva-setup)

* Mon Feb 22 2010 Emmanuel Andry <eandry@mandriva.org> 0.19-1mdv2010.1
+ Revision: 509781
- New version 0.19
- update description

* Sun Dec 27 2009 Frederik Himpe <fhimpe@mandriva.org> 0.18-1mdv2010.1
+ Revision: 482734
- update to new version 0.18

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.17-3mdv2010.0
+ Revision: 426794
- rebuild

* Thu Dec 25 2008 Adam Williamson <awilliamson@mandriva.org> 0.17-2mdv2009.1
+ Revision: 318743
- rebuild for python 2.6

* Wed Nov 26 2008 Funda Wang <fwang@mandriva.org> 0.17-1mdv2009.1
+ Revision: 307014
- New version 0.17

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.15-5mdv2008.1
+ Revision: 171070
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.15-4mdv2008.1
+ Revision: 126274
- kill re-definition of %%buildroot on Pixel's request


* Sat Dec 16 2006 Olivier Blin <oblin@mandriva.com> 0.15-4mdv2007.0
+ Revision: 98135
- remove dot in summary (and rebuild for new python)

  + Nicolas LÃ©cureuil <neoclust@mandriva.org>
    - import pyxdg-0.15-3mdk

* Tue Apr 11 2006 Michael Scherer <misc@mandriva.org> 0.15-3mdk
- remove requires on pythonlib, as this is not needed, and obsoletes
- add -q on package

* Tue Mar 21 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.15-2mdk
- Rebuild
- use mkrel

* Wed Mar 08 2006 Jerome Soyer <saispo@mandriva.org> 0.15-1mdk
- New release 0.15

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 0.5-3mdk
- Rebuild for new python

* Thu May 06 2004 Bruno VASTA <bruno.vasta@infodia.fr> 0.5-2mdk
- new method for file generation with python pyxdg-%%versionlog

* Tue May 04 2004 Bruno VASTA <bruno.vasta@infodia.fr> 0.5-1mdk
- Initial Mandrake rpm, created with pyxdg-0.15

