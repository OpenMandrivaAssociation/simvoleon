%define name		simvoleon
%define tarname		SIMVoleon
%define major		40
%define libname		%mklibname %{name} %{major}
%define libnamedev	%mklibname %{name} %{major} -d

Name:			%{name}
Version:		2.0.1
Release:		%mkrel 3
Summary:		Volume rendering library for Coin
License:		GPLv2
Group:			System/Libraries
URL:			http://www.coin3d.org
Source0:		http://ftp.coin3d.org/coin/src/all/%{tarname}-%{version}.tar.bz2

# Backport from 2.0.0:
# The 2.0.1 tarball lacks files.
Patch0:			SIMVoleon-2.0.1-doxyfixes.diff
Patch1:			SIMVoleon-2.0.1-simacros.diff
Patch2:			SIMVoleon-2.0.1-libtool.diff
Patch3:			SIMVoleon-2.0.1-gcc4.1.diff
Patch4:			simvoleon-2.0.1-mga-fix_here_doc-simvoleon-config.in.patch

BuildRequires:		pkgconfig(Coin)
BuildRequires:		pkgconfig(glu)
BuildRequires:		doxygen

%description
SIM Voleon is a software development system, in the form of an add-on library
to Coin3D. SIM Voleon complements Coin's capabilities for polygon-based
rendering with visualization of volumetric data sets, by providing so-called
"volume rendering" technology.

%package -n %{libname}
Summary:		Development files for SIMVoleon
Group:			System/Libraries
Provides:		%{name} = %{version}-%{release}

%description -n %{libname}
SIM Voleon is a software development system, in the form of an add-on library
to Coin3D. SIM Voleon complements Coin's capabilities for polygon-based
rendering with visualization of volumetric data sets, by providing so-called
"volume rendering" technology.

%package -n %{libnamedev}
Summary:		Development files for SIMVoleon
Requires:		%{libname} = %{version}-%{release}
Requires:		coin-devel
Provides:		%{name}-devel = %{version}-%{release}
Provides:		%{tarname}-devel = %{version}-%{release}
Group:			Development/C++

%description -n %{libnamedev}
SIM Voleon is a software development system, in the form of an add-on library
to Coin3D. SIM Voleon complements Coin's capabilities for polygon-based
rendering with visualization of volumetric data sets, by providing so-called
"volume rendering" technology.


%prep
%setup -q -n %{tarname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0 -b .simvoleon-2.0.1-mga-fix_here_doc-simvoleon-config.in.patch

chmod +x cfg/doxy4win.pl

%build
./configure \
	--prefix=%{_usr} \
	--libdir=%{_libdir} \
	--includedir=%{_includedir} \
	--disable-dependency-tracking \
	--enable-man \
	--enable-html \
	htmldir=%{_datadir}/Coin/SIMVoleon
%make

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS ChangeLog COPYING README NEWS
%{_libdir}/libSimVoleon*.so.*

%files -n %{libnamedev}
%{_bindir}/*
%{_includedir}/*
%{_libdir}/libSimVoleon*.so
%{_datadir}/aclocal/simvoleon.m4
%{_datadir}/Coin/conf
%{_datadir}/Coin/SIMVoleon/*
#% doc %{_datadir}/Coin/*
