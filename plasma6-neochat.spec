%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define oname neochat
#define git 20211107
#define gitcommit 71d01593b141f12bcf6556f8fb3e4e41d8a2c1d3

Name: plasma6-neochat
Version: 24.01.75
Release: %{?git:0.%{git}.}1
License: GPLv2 and GPLv2+ and GPLv3 and GPLv3+ and BSD
Summary: Client for matrix, the decentralized communication protocol
URL: https://invent.kde.org/network/neochat

Source0: https://invent.kde.org/network/neochat/-/archive/v%{version}/neochat-v%{version}.tar.bz2

#Source0: https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: cmake(Qt6)
BuildRequires: cmake(QCoro6)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Keychain)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WebView)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(Olm)
BuildRequires: cmake(QtOlm)
BuildRequires: cmake(QuotientQt6)
BuildRequires: cmake(Quotient)
BuildRequires: cmake(KQuickImageEditor)
BuildRequires: cmake(KF6QQC2DesktopStyle)
BuildRequires: pkgconfig(libcmark)
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(icu-uc)
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(appstream-glib)
BuildRequires: cmake(KF6SyntaxHighlighting)
Requires: hicolor-icon-theme
Requires: kf6-kirigami
Requires: %{_lib}KF6ItemModels
#Requires: qml(org.kde.kquickimageeditor)
#Requires: qt6-qtquickcontrols2
Requires: %{_lib}KF6SyntaxHighlighting
Requires: kirigami-addons-kde6
#Requires: qt6-qtlocation
Requires: %{_lib}Qt6Multimedia
Requires: kf6-kquickcharts

%description
Neochat is a client for Matrix, the decentralized communication protocol for
instant messaging. It is a fork of Spectral, using KDE frameworks, most
notably Kirigami, KConfig and KI18n.

%prep
%autosetup -n %{oname}-v%{version} -p1
export CC=gcc
export CXX=g++
%cmake  \
        -G Ninja \
        -DBUILD_WITH_QT6:BOOL=ON

%build
# Switch to GCC because Clang 16 crashing at compiling time. Same with libquotient.
export CC=gcc
export CXX=g++
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{oname} --with-man

%files -f %{oname}.lang
%license LICENSES/*
%doc README.md
%{_bindir}/%{oname}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/*.appdata.xml
%{_datadir}/knotifications6/neochat.notifyrc
%{_datadir}/qlogging-categories6/neochat.categories
%{_datadir}/krunner/dbusplugins/plasma-runner-neochat.desktop
%{_mandir}/man1/neochat.1*
