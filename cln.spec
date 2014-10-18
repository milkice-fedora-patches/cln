Name:           cln
Version:        1.3.4
Release:        1%{?dist}
Summary:        Class Library for Numbers
License:        GPLv2+
URL:            http://www.ginac.de/CLN/
Source0:        http://www.ginac.de/CLN/%{name}-%{version}.tar.bz2
Patch2:         cln-add-aarch64.patch
BuildRequires:  gmp-devel
BuildRequires:  texi2html
%if 0%{?fedora} && 0%{?fedora} > 20
BuildRequires:  perl(Unicode::EastAsianWidth)
%endif
BuildRequires:  texinfo-tex
Requires(post): /sbin/install-info
Requires(preun):/sbin/install-info

%description
A collection of C++ math classes and functions, which are designed for
memory and speed efficiency, and enable type safety and algebraic
syntax.

%package        devel
Summary:        Development files for programs using the CLN library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description    devel
A collection of C++ math classes and functions, which are designed for
memory and speed efficiency, and enable type safety and algebraic
syntax.

This package is necessary if you wish to develop software based on
the CLN library.

%ifarch %{arm}
%global XFLAGS %{optflags} -DNO_ASM
%else
%global XFLAGS %{optflags}
%endif

%prep
%setup -q
#patch2 -p1 -b .aarch64

%build
%configure --disable-static CXXFLAGS="%{XFLAGS}" CFLAGS="%{XFLAGS}"
make %{?_smp_mflags}
make pdf
make html

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print
rm -f %{buildroot}%{_infodir}/dir
rm -rf %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1/pi.*

%check
make %{_smp_mflags} check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel
/sbin/install-info --section="Math" %{_infodir}/cln.info.gz %{_infodir}/dir 2>/dev/null || :

%preun devel
if [ "$1" = 0 ]; then
  /sbin/install-info --delete %{_infodir}/cln.info.gz %{_infodir}/dir 2>/dev/null || :
fi

%files
%doc COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/cln.pc
%{_includedir}/cln/
%{_infodir}/*.info*
%doc doc/cln.pdf doc/cln.html

%changelog
* Wed Oct 15 2014 Christopher Meng <rpm@cicku.me> - 1.3.4-1
- Update to 1.3.4

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1.3.3-2
- Add AArch64 definitions.

* Wed Aug 14 2013 Deji Akingunola <dakingun@gmail.com> - 1.3.3-1
- New upstream version

* Tue Aug 06 2013 Deji Akingunola <dakingun@gmail.com> - 1.3.2-8
- Package the devel documents in unversioned docdir (BZ #993702)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4.1
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.3.2-2.1
- rebuild with new gmp without compat lib

* Wed Oct 19 2011 Deji Akingunola <dakingun@gmail.com> - 1.3.2-2
- Also add -DNO_ASM to CFLAGS for arm archs.
 
* Mon Oct 10 2011 Peter Schiffer <pschiffe@redhat.com> - 1.3.2-1.1
- rebuild with new gmp

* Sun Oct 09 2011 Deji Akingunola <dakingun@gmail.com> - 1.3.2-1
- New upstream version
- Add -DNO_ASM flag for arm archs.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 29 2009 Deji Akingunola <dakingun@gmail.com> - 1.3.1-1
- New upstream version
- Apply patch by Jitesh Shah to fix build on arm

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 02 2009 Deji Akingunola <dakingun@gmail.com> - 1.3.0-1
- Update to latest upstream release 1.3.0

* Thu May 28 2009 Dan Horak <dan[at]danny.cz> - 1.2.2-5
- fix build on s390x
- run the test-suite during build

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

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

* Mon Nov  5 2001 Christian Bauer <Christian.Bauer@uni-mainz.de>
  Added Packager
