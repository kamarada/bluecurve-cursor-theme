#
# spec file for package bluecurve-cursor-theme
#
# Copyright (c) 2014 Kamarada Project, Aracaju, Brazil.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://github.com/kamarada
#


%define tarname bluecurve-icon-theme-8.0.2
Name:           bluecurve-cursor-theme
Version:        8.0.2
Release:        1
Summary:        Bluecurve cursor theme
License:        GPL-2.0+
Group:          System/X11/Icons
Source0:        %{tarname}.tar.bz2
Source1:        LICENSE
Url:            http://fedorahosted.org/bluecurve
BuildRequires:  perl(XML::Parser)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch


%description
This package contains Bluecurve style cursors.


%prep
%setup -q -n %{tarname}
cp -a %{SOURCE0} COPYING


%build
%configure 
make


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# These are empty
rm -f ChangeLog NEWS README

# Leave us just with the cursor theme
cd $RPM_BUILD_ROOT%{_datadir}/icons/Bluecurve/
rm -rf index.theme 16x16 20x20 24x24 32x32 36x36 48x48 64x64 96x96


%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(-, root, root)
%doc AUTHORS COPYING
%dir %{_datadir}/icons/Bluecurve
%{_datadir}/icons/Bluecurve/Bluecurve.cursortheme
%{_datadir}/icons/Bluecurve/cursors
%{_datadir}/icons/Bluecurve-inverse
%{_datadir}/icons/LBluecurve
%{_datadir}/icons/LBluecurve-inverse


%changelog
* Fri Jul 25 2014 Kamarada Linux <kamaradalinux@gmail.com>
- Initial import from Fedora 20 repository, version 8.0.2
