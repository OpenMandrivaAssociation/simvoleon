%define name		simvoleon
%define tarname		SIMVoleon
%define major		40
%define libname		%mklibname %{name} %{major}
%define libnamedev	%mklibname %{name} %{major} -d

Name:			%{name}
Version:		2.0.3
Release:		1
Summary:		Volume rendering library for Coin
License:		GPLv2
Group:			System/Libraries
URL:			http://www.coin3d.org
Source0:		https://bitbucket.org/Coin3D/simvoleon/downloads/%{name}-%{version}-src.zip
# bash-4 compatibility bugfix
Patch0: SIMVoleon-2.0.1-bash4.0.diff

BuildRequires:		pkgconfig(Coin4)
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
%autosetup -p1 -n simvoleon

chmod +x cfg/doxy4win.pl

%build
%cmake -DSIMVOLEON_BUILD_DOCUMENTATION=TRUE \
       -DSIMVOLEON_BUILD_TESTS=FALSE \
       -DSIMVOLEON_BUILD_DOC_MAN=TRUE

%make_build

%install
%make_install -C build

%files -n %{libname}
%doc AUTHORS ChangeLog COPYING README NEWS
%{_libdir}/libSIMVoleon*.so.*

%files -n %{libnamedev}
%{_includedir}/*
%{_libdir}/libSIMVoleon*.so
%{_mandir}/man3/*
%{_datadir}/doc/SIMVoleon/*
%{_libdir}/cmake/SIMVoleon-%{version}/*.cmake
%{_libdir}/pkgconfig/SIMVoleon.pc
%{_datadir}/info/SIMVoleon2/build-options.*
