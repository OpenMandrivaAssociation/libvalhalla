%define major 2
%define libname %mklibname valhalla %{major}
%define develname %mklibname valhalla -d

Name: libvalhalla
Version: 2.0.0
Release: %mkrel 1
URL: http://libvalhalla.geexbox.org/
Source:	http://libvalhalla.geexbox.org/releases/%{name}-%{version}.tar.bz2
License: LGPLv2+
Summary: A media scanner
Group: System/Libraries
BuildRequires: sqlite3-devel
BuildRequires: ffmpeg-devel
BuildRequires: curl-devel
BuildRequires: libxml2-devel
BuildRequires: libexif-devel
BuildRequires: libgcrypt-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
libvalhalla is a library written in C. It is a media scanner, that stores
various information in an SQLite database and relies on FFmpeg (libavformat
and libavutil) and libcurl. It features many Internet grabbers that allows
automatic download of covers, lyrics, informations on media files, tags
retrival in video and music files and so on.

%package test
Summary: A media scanner
Group: System/Libraries

%description test
libvalhalla is a library written in C. It is a media scanner, that stores
various information in an SQLite database and relies on FFmpeg (libavformat
and libavutil) and libcurl. It features many Internet grabbers that allows
automatic download of covers, lyrics, informations on media files, tags
retrival in video and music files and so on.

%package -n %{libname}
Summary: A media scanner
Group: System/Libraries

%description -n %{libname}
libvalhalla is a library written in C. It is a media scanner, that stores
various information in an SQLite database and relies on FFmpeg (libavformat
and libavutil) and libcurl. It features many Internet grabbers that allows
automatic download of covers, lyrics, informations on media files, tags
retrival in video and music files and so on.

%package -n %{develname}
Summary: A media scanner
Group: System/Libraries
Provides: %{name}-devel = %{version}-%{release}
Requires: %libname = %version

%description -n %{develname}
libvalhalla is a library written in C. It is a media scanner, that stores
various information in an SQLite database and relies on FFmpeg (libavformat
and libavutil) and libcurl. It features many Internet grabbers that allows
automatic download of covers, lyrics, informations on media files, tags
retrival in video and music files and so on.

This package contains the headers required for compiling software that uses
the libvalhalla library.

%prep
%setup -q -n %{name}-%{version}

%build
%setup_compile_flags
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--includedir=%{_includedir} \
	--disable-static \
	--enable-shared
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files test
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
