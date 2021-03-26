Summary:	GNOME Mines
Summary(pl.UTF-8):	Miny dla GNOME
Name:		gnome-mines
Version:	40.0
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	https://download.gnome.org/sources/gnome-mines/40/%{name}-%{version}.tar.xz
# Source0-md5:	569b2b3c4d41fb122ec2f1958d9ded01
URL:		https://wiki.gnome.org/Apps/Mines
BuildRequires:	appstream-glib
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gtk+3-devel >= 3.24
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	libgnome-games-support-devel >= 1.7.1
BuildRequires:	librsvg-devel >= 1:2.32.0
BuildRequires:	meson >= 0.37.1
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	vala >= 2:0.24.0
BuildRequires:	vala-libgee >= 0.8
BuildRequires:	vala-librsvg >= 1:2.32.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.40.0
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.24
Requires:	hicolor-icon-theme
Requires:	libgnome-games-support >= 1.7.1
Requires:	librsvg >= 1:2.32.0
Provides:	gnome-games-gnomine = 1:%{version}-%{release}
Obsoletes:	gnome-games-gnomine < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mines (previously gnomine) is a puzzle game where you locate mines
floating in an ocean using only your brain and a little bit of luck.

%description -l pl.UTF-8
Mines (dawniej gnomine) to układanka, w której należy zlokalizować
przywające w oceanie miny, korzystając z własnego mózgu oraz odrobiny
szczęścia.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-mines
%{_datadir}/glib-2.0/schemas/org.gnome.Mines.gschema.xml
%{_datadir}/gnome-mines
%{_datadir}/metainfo/org.gnome.Mines.appdata.xml
%{_desktopdir}/org.gnome.Mines.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Mines.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Mines-symbolic.svg
%{_mandir}/man6/gnome-mines.6*
