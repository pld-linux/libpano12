#
# Conditional build:
%bcond_with	java	# build with Java Native Interface
#
Summary:	Panorama Tools library
Summary(pl.UTF-8):	Panorama Tools - biblioteka do obróbki panoram
Name:		libpano12
Version:	2.8.6
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/panotools/%{name}-%{version}.tar.gz
# Source0-md5:	d4eae64c292bff3001ef3eef0fc9cb94
URL:		http://panotools.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
%{?with_java:BuildRequires:	jdk}
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Panorama Tools library.
%{!?with_java:Note: this version does not provide Java interface!}

%description -l pl.UTF-8
Panorama Tools - biblioteka do obróbki panoram.
%{!?with_java:Uwaga: ta wersja nie dostarcza interfesju dla Javy!}

%package devel
Summary:	Header files for Panorama Tools library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Panorama Tools
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libjpeg-devel >= 6b
Requires:	libpng-devel
Requires:	libtiff-devel

%description devel
Header files for Panorama Tools library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Panorama Tools.

%package static
Summary:	Static Panorama Tools library
Summary(pl.UTF-8):	Statyczna biblioteka Panorama Tools
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Panorama Tools library.

%description static -l pl.UTF-8
Statyczna biblioteka Panorama Tools.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	%{?with_java:--with-java=/usr/%{_lib}/java}%{!?with_java:--without-java}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README README.linux doc/*.txt
%attr(755,root,root) %{_bindir}/PTOptimizer
%attr(755,root,root) %{_bindir}/pano12info
%attr(755,root,root) %{_libdir}/libpano12.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpano12.so
%{_libdir}/libpano12.la
%{_includedir}/pano12

%files static
%defattr(644,root,root,755)
%{_libdir}/libpano12.a
