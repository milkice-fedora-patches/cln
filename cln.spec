Name:           cln
Version:        1.2.2
Release:        3%{?dist}
Summary:        Class Library for Numbers

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.ginac.de/CLN/
Source0:        http://www.ginac.de/CLN/%{name}-%{version}.tar.bz2
Patch0:		cln-upstream_gcc44_fix.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
BuildRequires:  gmp-devel

%description
A collection of C++ math classes and functions, which are designed for
memory and speed efficiency, and enable type safety and algebraic
syntax.

%package devel
Summary:        Development files for programs using the CLN library
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release} gmp-devel pkgconfig

%description devel
A collection of C++ math classes and functions, which are designed for
memory and speed efficiency, and enable type safety and algebraic
syntax.

This package is necessary if you wish to develop software based on
the CLN library.

%prep
%setup -q
%patch0 -p1 -b .gcc44

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall
mkdir -p ${RPM_BUILD_ROOT}%{_docdir}/%{name}-devel-%{version}
mv ${RPM_BUILD_ROOT}%{_datadir}/dvi/cln.dvi ${RPM_BUILD_ROOT}%{_datadir}/html ${RPM_BUILD_ROOT}%{_docdir}/%{name}-devel-%{version}
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%clean
rm -rf ${RPM_BUILD_ROOT}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel
/sbin/install-info --section="Math" %{_infodir}/cln.info.gz %{_infodir}/dir 2>/dev/null || :

%preun devel
if [ "$1" = 0 ]; then
  /sbin/install-info --delete %{_infodir}/cln.info.gz %{_infodir}/dir 2>/dev/null || :
fi

%files
%defattr(-,root,root)
%doc COPYING ChangeLog FILES NEWS README TODO*
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_docdir}/%{name}-devel-%{version}
%{_libdir}/*.so
%{_libdir}/pkgconfig/cln.pc
%{_includedir}/cln/
%{_infodir}/*.info*
%exclude %{_libdir}/*.la

%changelog
* Wed Feb 04 2009 Deji Akingunola <dakingun@gmail.com> - 1.2.2-3
- Add upstream patch to build with gcc-4.4

* Fri Jan 16 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.2.2-2
- Bump to solve dependency for ginac-devel

* Tue Apr 29 2008 Quentin Spencer <qspencer@users.sf.net> 1.2.2-1
- Update to 1.2.2.

* Mon Feb 25 2008 Quentin Spencer <qspencer@users.sf.net> 1.2.0-1
- Update to 1.2.0.
- Update License tag.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.13-5
- Autorebuild for GCC 4.3

* Thu Sep 13 2007 Quentin Spencer <qspencer@users.sf.net> 1.1.13-4
- Add pkgconfig as a dependency of -devel.

* Tue Aug 21 2007 Quentin Spencer <qspencer@users.sf.net> 1.1.13-3
- Rebuild for F8.

* Mon Aug 28 2006 Quentin Spencer <qspencer@users.sf.net> 1.1.13-2
- Rebuild for FC-6.

* Thu Aug 17 2006 Quentin Spencer <qspencer@users.sf.net> 1.1.13-1
- New release.

* Mon Feb 13 2006 Quentin Spencer <qspencer@users.sf.net> 1.1.11-5
- Disable static build.
- Enable parallel build.

* Mon Feb 13 2006 Quentin Spencer <qspencer@users.sf.net> 1.1.11-4
- Rebuild for Fedora Extras 5.
- Remove /usr/share/info/dir after install.
- Exclude static libs.

* Mon Jan 16 2006 Quentin Spencer <qspencer@users.sf.net> 1.1.11-3
- Exclude /usr/share/info/dir from package (bug 178660).

* Mon Jan 16 2006 Quentin Spencer <qspencer@users.sf.net> 1.1.11-2
- Update source URL.

* Mon Jan 16 2006 Quentin Spencer <qspencer@users.sf.net> 1.1.11-1
- New upstream release.

* Mon Oct 31 2005 Quentin Spencer <qspencer@users.sf.net> 1.1.10-1
- New upstream release, incorporating previous patch.

* Mon Jun 20 2005 Quentin Spencer <qspencer@users.sf.net> 1.1.9-8
- Rebuild

* Mon Jun 13 2005 Quentin Spencer <qspencer@users.sf.net> 1.1.9-4
- Patched include/cln/string.h to correctly compile on gcc-c++-4.0.0-9

* Fri May 27 2005 Quentin Spencer <qspencer@users.sf.net> 1.1.9-3
- Added gmp-devel to Requires for devel

* Fri May 20 2005 Quentin Spencer <qspencer@users.sf.net> 1.1.9-2
- Added dist tag.

* Wed May 11 2005 Quentin Spencer <qspencer@users.sf.net> 1.1.9-1
- Excluded .la file

* Fri Apr 22 2005 Quentin Spencer <qspencer@users.sf.net> 1.1.9-1
- Added gmp-devel in BuildRequires, fixes in files
- Added release to name in Requires for devel

* Mon Mar 21 2005 Quentin Spencer <qspencer@users.sf.net> 1.1.9-1
- Adapted spec file for Fedora Extras

* Thu Nov 20 2003 Christian Bauer <Christian.Bauer@uni-mainz.de>
  Added pkg-config metadata file to devel package

* Wed Nov  6 2002 Christian Bauer <Christian.Bauer@uni-mainz.de>
  Added HTML and DVI docs to devel package

* Tue Nov  5 2001 Christian Bauer <Christian.Bauer@uni-mainz.de>
  Added Packager
