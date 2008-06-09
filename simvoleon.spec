
%define libname %mklibname simvoleon 40

Summary: Volume rendering library for Coin
Name: simvoleon
Version: 2.0.1
Release: %mkrel 3
License: GPL
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://www.coin3d.org
Source: http://ftp.coin3d.org/coin/src/all/SIMVoleon-%{version}.tar.bz2

# Backport from 2.0.0:
#  The 2.0.1 tarball lacks files.
Patch0: SIMVoleon-2.0.1-doxyfixes.diff
Patch1: SIMVoleon-2.0.1-simacros.diff
Patch2: SIMVoleon-2.0.1-libtool.diff
Patch3: SIMVoleon-2.0.1-gcc4.1.diff

BuildRequires: coin-devel
BuildRequires: doxygen
BuildRequires: mesaglu-devel

%description
SIM Voleon is a software development system, in the form of an add-on library
to Coin3D. SIM Voleon complements Coin's capabilities for polygon-based
rendering with visualization of volumetric data sets, by providing so-called
"volume rendering" technology.


%package -n %libname
Summary: Development files for SIMVoleon
Group: System/Libraries
Provides:  simvoleon = %{version}-%{release}

%description -n %libname
SIM Voleon is a software development system, in the form of an add-on library
to Coin3D. SIM Voleon complements Coin's capabilities for polygon-based
rendering with visualization of volumetric data sets, by providing so-called
"volume rendering" technology.


%package -n %libname-devel
Summary: Development files for SIMVoleon
Requires: %{libname} = %{version}
Requires: coin-devel >= 2.3.0
Provides:  simvoleon-devel = %{version}-%{release}
Group: Development/C++

%description -n %libname-devel
SIM Voleon is a software development system, in the form of an add-on library
to Coin3D. SIM Voleon complements Coin's capabilities for polygon-based
rendering with visualization of volumetric data sets, by providing so-called
"volume rendering" technology.


%prep
%setup -q -n SIMVoleon-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

chmod +x cfg/doxy4win.pl

%build
%configure \
	--includedir=%{_includedir} \
	--disable-dependency-tracking \
	--enable-man \
	--enable-html \
	htmldir=%{_datadir}/Coin2/SIMVoleon
%make

%install
rm -rf $RPM_BUILD_ROOT
# make DESTDIR=$RPM_BUILD_ROOT install
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README NEWS
%{_libdir}/libSimVoleon*.so.*

%files -n %libname-devel
%defattr(-,root,root,-)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/libSimVoleon.*a
%{_libdir}/libSimVoleon*.so
%{_datadir}/aclocal/simvoleon.m4
%{_datadir}/Coin/conf
%doc %{_datadir}/Coin2/*

