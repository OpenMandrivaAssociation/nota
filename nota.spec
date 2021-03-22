Name:		nota
Version:	1.2.1
Release:	1
Source0:	https://invent.kde.org/maui/nota/-/archive/v%{version}/nota-v%{version}.tar.bz2
Group:		Applications/Productivity
Summary:	Text editor for Plasma Mobile
License:	GPLv3
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(MauiKit)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(Qt5WebView)
BuildRequires:	cmake(Qt5WebEngine)

%description
Text editor for Plasma Mobile

%prep
%autosetup -p1 -n %{name}-v%{version}
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/nota
%{_datadir}/applications/org.kde.nota.desktop
%{_datadir}/icons/hicolor/scalable/apps/nota.svg
