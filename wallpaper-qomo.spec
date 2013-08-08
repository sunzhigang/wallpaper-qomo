Name: wallpaper-qomo
Version: 4.8
Release: 3
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
rm -rf ${RPM_BUILD_ROOT}

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

# loverf
git clone git://github.com/sunzhigang/wallpaper-loverf.git  loverf
rm -rf loverf/{.git,LICENSE,README.md}
install -d -m755 ${_ROOT}/usr/share/wallpapers/
mv loverf ${_ROOT}/usr/share/wallpapers/
# loverf

%post
pushd /usr/share/wallpapers/ &>/dev/null
    rm -rf wallpaper-default
    ln -sf loverf wallpaper-default
popd &>/dev/null
[[ -x /usr/share/wallpapers/update-gnome-wallpaper.sh ]] && /usr/share/wallpapers/update-gnome-wallpaper.sh
pushd /usr/share/apps/ksplash/Themes/ &>/dev/null
    ! test -e Default || test -e default || ln -sf Default default
popd &>/dev/null


%postun
pushd /usr/share/wallpapers/ &>/dev/null
    test -L wallpaper-default && unlink wallpaper-default
popd &>/dev/null

pushd /usr/share/apps/ksplash/Themes/ &>/dev/null
    test -L default && test ! -e default && unlink default
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
/usr/share/wallpapers/loverf/contents/images/1024x768.jpg
/usr/share/wallpapers/loverf/contents/images/1280x1024.jpg
/usr/share/wallpapers/loverf/contents/images/1280x720.jpg
/usr/share/wallpapers/loverf/contents/images/1280x800.jpg
/usr/share/wallpapers/loverf/contents/images/1366x768.jpg
/usr/share/wallpapers/loverf/contents/images/1440x1050.jpg
/usr/share/wallpapers/loverf/contents/images/1440x900.jpg
/usr/share/wallpapers/loverf/contents/images/1600x1200.jpg
/usr/share/wallpapers/loverf/contents/images/1680x1050.jpg
/usr/share/wallpapers/loverf/contents/images/1920x1080.jpg
/usr/share/wallpapers/loverf/contents/images/1920x1200.jpg
/usr/share/wallpapers/loverf/contents/images/2048x1536.jpg
/usr/share/wallpapers/loverf/contents/images/2560x1600.jpg
/usr/share/wallpapers/loverf/contents/images/640x480.jpg
/usr/share/wallpapers/loverf/contents/images/800x600.jpg
/usr/share/wallpapers/loverf/contents/screenshot.png
/usr/share/wallpapers/loverf/metadata.desktop

%changelog
* Thu Aug 8 2013 sunzhigang <sunzhigang@redflag-linux.com> 4.8-3
- configure the default ksplash

* Thu Aug 8 2013 sunzhigang <sunzhigang@redflag-linux.com> 4.8-2
- add wallpaper by loverf

* Mon Aug 5 2013 sunzhigang <sunzhigang@redflag-linux.com> 4.8-1
- wallpaper-qomo init
