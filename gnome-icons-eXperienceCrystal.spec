#
%define realname eXperienceCrystal
#
Summary:	eXperience Crystal icon theme
Summary(pl.UTF-8):	Motyw ikon eXperience Crystal
Name:		gnome-icons-eXperienceCrystal
Version:	1.1.1
Release:	0.1
License:	other
Group:		X11/Amusements
Source0:	http://art.gnome.org/download/themes/icon/768/ICON-eXperienceCrystal.tar.gz
# Source0-md5:	01b1a46d6969f0716f0f5c1bcf6f1138
URL:		http://art.gnome.org/themes/icon/768/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An icon theme to go with the eXperience Gtk-theme. It's based on
Everaldos Crystal theme. Actually only some icons are changed.

%description -l pl.UTF-8
Zestaw ikonek do wykorzystanie razem z tematem eXperience. Ikonki są
oparte na zestawie Everaldos Crystal. W tej chwili tylko niektóre
ikonki są zmienione.

%prep
%setup -q -n %{realname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/%{realname}
cp -af . $RPM_BUILD_ROOT%{_iconsdir}/%{realname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_iconsdir}/%{realname}
%dir %{_iconsdir}/%{realname}/scalable
%dir %{_iconsdir}/%{realname}/scalable/apps
%dir %{_iconsdir}/%{realname}/scalable/devices
%dir %{_iconsdir}/%{realname}/scalable/emblems
%dir %{_iconsdir}/%{realname}/scalable/filesystems
%dir %{_iconsdir}/%{realname}/scalable/mimetypes
%dir %{_iconsdir}/%{realname}/scalable/stock
%dir %{_iconsdir}/%{realname}/scalable/stock/generic
%dir %{_iconsdir}/%{realname}/scalable/stock/media
%dir %{_iconsdir}/%{realname}/scalable/stock/navigation
%dir %{_iconsdir}/%{realname}/scalable/stock/text
%{_iconsdir}/%{realname}/index.theme
%{_iconsdir}/%{realname}/scalable/apps/*.svg
%{_iconsdir}/%{realname}/scalable/devices/*.svg
%{_iconsdir}/%{realname}/scalable/emblems/*.svg
%{_iconsdir}/%{realname}/scalable/filesystems/*.svg
%{_iconsdir}/%{realname}/scalable/mimetypes/*.svg
%{_iconsdir}/%{realname}/scalable/stock/generic/*.svg
%{_iconsdir}/%{realname}/scalable/stock/media/*.svg
%{_iconsdir}/%{realname}/scalable/stock/navigation/*.svg
%{_iconsdir}/%{realname}/scalable/stock/text/*.svg

%dir %{_iconsdir}/%{realname}/128x128
%dir %{_iconsdir}/%{realname}/128x128/mimetypes
%{_iconsdir}/%{realname}/128x128/mimetypes/*.png
%dir %{_iconsdir}/%{realname}/128x128/filesystems
%{_iconsdir}/%{realname}/128x128/filesystems/*.png
%dir %{_iconsdir}/%{realname}/128x128/actions
%{_iconsdir}/%{realname}/128x128/actions/*.png
%dir %{_iconsdir}/%{realname}/128x128/apps
%{_iconsdir}/%{realname}/128x128/apps/*.png
%dir %{_iconsdir}/%{realname}/128x128/devices
%{_iconsdir}/%{realname}/128x128/devices/*.png
%dir %{_iconsdir}/%{realname}/128x128/devices/apps
%{_iconsdir}/%{realname}/128x128/devices/apps/*.png

%dir %{_iconsdir}/%{realname}/16x16
%dir %{_iconsdir}/%{realname}/16x16/mimetypes
%{_iconsdir}/%{realname}/16x16/mimetypes/*.png
%dir %{_iconsdir}/%{realname}/16x16/filesystems
%{_iconsdir}/%{realname}/16x16/filesystems/*.png
%dir %{_iconsdir}/%{realname}/16x16/actions
%{_iconsdir}/%{realname}/16x16/actions/*.png
%dir %{_iconsdir}/%{realname}/16x16/apps
%{_iconsdir}/%{realname}/16x16/apps/*.png
%dir %{_iconsdir}/%{realname}/16x16/devices
%{_iconsdir}/%{realname}/16x16/devices/*.png
%dir %{_iconsdir}/%{realname}/16x16/devices/apps
%{_iconsdir}/%{realname}/16x16/devices/apps/*.png

%dir %{_iconsdir}/%{realname}/32x32
%dir %{_iconsdir}/%{realname}/32x32/mimetypes
%{_iconsdir}/%{realname}/32x32/mimetypes/*.png
%dir %{_iconsdir}/%{realname}/32x32/filesystems
%{_iconsdir}/%{realname}/32x32/filesystems/*.png
%dir %{_iconsdir}/%{realname}/32x32/actions
%{_iconsdir}/%{realname}/32x32/actions/*.png
%dir %{_iconsdir}/%{realname}/32x32/apps
%{_iconsdir}/%{realname}/32x32/apps/*.png
%dir %{_iconsdir}/%{realname}/32x32/devices
%{_iconsdir}/%{realname}/32x32/devices/*.png
%dir %{_iconsdir}/%{realname}/32x32/devices/apps
%{_iconsdir}/%{realname}/32x32/devices/apps/*.png

%dir %{_iconsdir}/%{realname}/48x48
%dir %{_iconsdir}/%{realname}/48x48/mimetypes
%{_iconsdir}/%{realname}/48x48/mimetypes/*.png
%dir %{_iconsdir}/%{realname}/48x48/filesystems
%{_iconsdir}/%{realname}/48x48/filesystems/*.png
%{_iconsdir}/%{realname}/48x48/filesystems/*.icon
%dir %{_iconsdir}/%{realname}/48x48/actions
%{_iconsdir}/%{realname}/48x48/actions/*.png
%dir %{_iconsdir}/%{realname}/48x48/apps
%{_iconsdir}/%{realname}/48x48/apps/*.png
%dir %{_iconsdir}/%{realname}/48x48/devices
%{_iconsdir}/%{realname}/48x48/devices/*.png
%dir %{_iconsdir}/%{realname}/48x48/devices/apps
%{_iconsdir}/%{realname}/48x48/devices/apps/*.png
%dir %{_iconsdir}/%{realname}/48x48/emblems
%{_iconsdir}/%{realname}/48x48/emblems/*.png

%dir %{_iconsdir}/%{realname}/22x22
%dir %{_iconsdir}/%{realname}/22x22/mimetypes
%{_iconsdir}/%{realname}/22x22/mimetypes/*.png
%dir %{_iconsdir}/%{realname}/22x22/filesystems
%{_iconsdir}/%{realname}/22x22/filesystems/*.png
%dir %{_iconsdir}/%{realname}/22x22/actions
%{_iconsdir}/%{realname}/22x22/actions/*.png
%dir %{_iconsdir}/%{realname}/22x22/apps
%{_iconsdir}/%{realname}/22x22/apps/*.png
%dir %{_iconsdir}/%{realname}/22x22/devices
%{_iconsdir}/%{realname}/22x22/devices/*.png
%dir %{_iconsdir}/%{realname}/22x22/devices/apps
%{_iconsdir}/%{realname}/22x22/devices/apps/*.png

%dir %{_iconsdir}/%{realname}/64x64
%dir %{_iconsdir}/%{realname}/64x64/mimetypes
%{_iconsdir}/%{realname}/64x64/mimetypes/*.png
%dir %{_iconsdir}/%{realname}/64x64/filesystems
%{_iconsdir}/%{realname}/64x64/filesystems/*.png
%dir %{_iconsdir}/%{realname}/64x64/actions
%{_iconsdir}/%{realname}/64x64/actions/*.png
%dir %{_iconsdir}/%{realname}/64x64/apps
%{_iconsdir}/%{realname}/64x64/apps/*.png
%dir %{_iconsdir}/%{realname}/64x64/devices
%{_iconsdir}/%{realname}/64x64/devices/*.png
