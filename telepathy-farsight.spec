Summary:	Telepathy client to handle media streaming channels
Name:		telepathy-farsight
Version:	0.0.19
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-farsight/%{name}-%{version}.tar.gz
# Source0-md5:	6bacc22aaec00823f3bbce8517600ec3
URL:		http://telepathy.freedesktop.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	farsight2-devel >= 0.0.14
BuildRequires:	gtk-doc >= 1.10
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-gstreamer-devel
BuildRequires:	python-pygtk-devel >= 2:2.12.0
BuildRequires:	telepathy-glib-devel >= 0.7.26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
telepathy-farsight is a Telepathy client that uses Farsight and
GStreamer to handle media streaming channels. It's used as a
background process by other Telepathy clients, rather than presenting
any user interface of its own.

%package devel
Summary:	Header files for telepathy-farsight library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki telepathy-farsight
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.74
Requires:	farsight2-devel >= 0.0.3
Requires:	glib2-devel >= 1:2.10.0
Requires:	gstreamer-devel
Requires:	telepathy-glib-devel >= 0.7.23

%description devel
Header files for telepathy-farsight library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki telepathy-farsight.

%package static
Summary:	Static telepathy-farsight library
Summary(pl.UTF-8):	Statyczna biblioteka telepathy-farsight
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static telepathy-farsight library.

%description static -l pl.UTF-8
Statyczna biblioteka telepathy-farsight.

%package apidocs
Summary:	telepathy-farsight library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki telepathy-farsight
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
telepathy-farsight library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki telepathy-farsight.

%package -n python-telepathy-farsight
Summary:	telepathy-farsight Python bindings
Summary(pl.UTF-8):	Wiązania Pythona do telepathy-farsight
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-telepathy-farsight
telepathy-farsight Python bindings.

%description -n python-telepathy-farsight -l pl.UTF-8
Wiązania Pythona do telepathy-farsight.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libtelepathy-farsight.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-farsight.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtelepathy-farsight.so
%{_libdir}/libtelepathy-farsight.la
%{_includedir}/telepathy-1.0/telepathy-farsight
%{_pkgconfigdir}/telepathy-farsight.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libtelepathy-farsight.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/telepathy-farsight

%files -n python-telepathy-farsight
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/tpfarsight.so
