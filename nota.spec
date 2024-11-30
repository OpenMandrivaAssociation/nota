#define snapshot 20220107

Name:		nota
Version:	4.0.0
Release:	%{?snapshot:0.%{snapshot}.}1
URL:		https://invent.kde.org/maui/nota/
Source0:	https://invent.kde.org/maui/nota/-/archive/%{?snapshot:master/nota-master.tar.bz2#/nota-%{snapshot}}%{!?snapshot:v%{version}/nota-v%{version}}.tar.bz2
Group:		Applications/Productivity
Summary:	Text editor for Plasma Mobile
License:	GPLv3
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(MauiKit4)
BuildRequires:  cmake(MauiKitFileBrowsing4)
BuildRequires:  cmake(MauiKitTextEditor4)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Attica)
BuildRequires:	cmake(KF6SyntaxHighlighting)
BuildRequires:	cmake(Qt6WebView)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(Qt6Widgets)

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
