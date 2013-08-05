Name: wallpaper-qomo
Version: 4.8
Release: 1
Summary: wallpapers for Qomo Linux
Group: Themes
License: GPL
URL: http://www.linux-ren.org/
BuildRequires: git
Requires: qomo-release

%description
wallpapers for Qomo Linux

%prep
%setup -T -c -n wallpaper-qomo

%build

%install
_ROOT=${RPM_BUILD_ROOT}/wallpaper-qomo
install -d -m755 $_ROOT
cd ${RPM_BUILD_DIR}/wallpaper-qomo

# Qomo1
git clone git://github.com/sunzhigang/wallpaper-qomo1.git  Qomo1
rm -rf Qomo1/.git
install -d -m755 ${_ROOT}/usr/share/wallpapers/
mv Qomo1 ${_ROOT}/usr/share/wallpapers/
# Qomo1 end

%post
pushd /usr/share/wallpapers/ &>/dev/null
    test -e wallpaper-default || ln -sf Qomo1 wallpaper-default
popd &>/dev/null

%postun
pushd /usr/share/wallpapers/ &>/dev/null
    test -L wallpaper-default && unlink wallpaper-default
popd &>/dev/null

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,-)
/usr/share/wallpapers/Qomo1/contents/images/1024x768.jpg
/usr/share/wallpapers/Qomo1/contents/images/1280x1024.jpg
/usr/share/wallpapers/Qomo1/contents/images/1280x800.jpg
/usr/share/wallpapers/Qomo1/contents/images/1366x768.jpg
/usr/share/wallpapers/Qomo1/contents/images/1440x900.jpg
/usr/share/wallpapers/Qomo1/contents/images/1600x1200.jpg
/usr/share/wallpapers/Qomo1/contents/images/1920x1080.jpg
/usr/share/wallpapers/Qomo1/contents/images/1920x1200.jpg
/usr/share/wallpapers/Qomo1/contents/screenshot.png
/usr/share/wallpapers/Qomo1/metadata.desktop

%changelog
* Mon Aug 5 2013 sunzhigang <sunzhigang@redflag-linux.com> 4.8-1
- wallpaper-qomo init
