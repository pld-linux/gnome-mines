Summary:	GNOME Mines
Summary(pl.UTF-8):	Miny dla GNOME
Name:		gnome-mines
Version:	3.12.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-mines/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	341423c9075fd75f9466b7ba8f0e4b89
URL:		https://wiki.gnome.org/Apps/Mines
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	pkgconfig
BuildRequires:	vala >= 2:0.22.0
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	glib2 >= 1:2.36.0
Requires:	gtk+3 >= 3.4.0
Requires:	hicolor-icon-theme
Requires:	librsvg >= 2.32.0
Provides:	gnome-games-gnomine = 1:%{version}-%{release}
Obsoletes:	gnome-games-gnomine < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Clear mines from a minefield.

%description -l pl.UTF-8
Gra, której celem jest rozminowanie pola minowego.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-mines
%{_datadir}/appdata/gnome-mines.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.mines.gschema.xml
%{_datadir}/gnome-mines
%{_desktopdir}/gnome-mines.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_mandir}/man6/gnome-mines.6*
