Name:           cln
Version:        1.1.9
Release:        1
Summary:        Class Library for Numbers

Group:          System Environment/Libraries
License:        GPL
URL:            http://www.ginac.de/CLN/
Source0:        ftp://ftpthep.physik.uni-mainz.de/pub/gnu/%{name}-%{version}.tar.bz2
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
Requires:       %{name} = %{version}-%{release}

%description devel
A collection of C++ math classes and functions, which are designed for
memory and speed efficiency, and enable type safety and algebraic
syntax.

This package is necessary if you wish to develop software based on
the CLN library.

%prep
%setup -q

%build
%configure
make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall
mkdir -p ${RPM_BUILD_ROOT}%{_docdir}/%{name}-devel-%{version}
mv ${RPM_BUILD_ROOT}%{_datadir}/dvi/cln.dvi ${RPM_BUILD_ROOT}%{_datadir}/html ${RPM_BUILD_ROOT}%{_docdir}/%{name}-devel-%{version}

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
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/cln.pc
%{_includedir}/cln/
%{_infodir}/*.info*
%{_mandir}/man1/cln-config.1*
%{_bindir}/cln-config
%{_datadir}/aclocal/cln.m4

%changelog
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
