#define snapshot 20220107

Name:		nota
Version:	3.0.2
Release:	%{?snapshot:0.%{snapshot}.}1
URL:		https://invent.kde.org/maui/nota/
Source0:	https://invent.kde.org/maui/nota/-/archive/%{?snapshot:master/nota-master.tar.bz2#/nota-%{snapshot}}%{!?snapshot:v%{version}/nota-v%{version}}.tar.bz2
Group:		Applications/Productivity
Summary:	Text editor for Plasma Mobile
License:	GPLv3
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(MauiKit3)
BuildRequires:  cmake(MauiKitFileBrowsing3)
BuildRequires:  cmake(MauiKitTextEditor3)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(Qt5WebView)
BuildRequires:	cmake(Qt5WebEngine)
BuildRequires:	cmake(Qt5Widgets)

Requires: qml(org.mauikit.texteditor)

%description
Text editor for Plasma Mobile

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang nota

%files -f nota.lang
%{_bindir}/nota
%{_datadir}/applications/org.kde.nota.desktop
%{_datadir}/icons/hicolor/scalable/apps/nota.svg
%{_datadir}/metainfo/org.kde.nota.metainfo.xml
