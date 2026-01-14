%bcond clang 1
%bcond gamin 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg tdesvn
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.0.4
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Subversion client with tight TDE integration
Group:		Applications/Utilities
URL:		http://www.elliptique.net/~ken/kima/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/development/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include
BuildOption:    -DMAN_INSTALL_DIR=%{tde_prefix}/share/man
BuildOption:    -DPKGCONFIG_INSTALL_DIR=%{tde_prefix}/%{_lib}/pkgconfig
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DBUILD_DOC=ON -DBUILD_TRANSLATIONS=ON

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires: libtool

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

# SVN support
BuildRequires:	subversion-devel

# SQLITE3 support
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  libtqt3-mt-sqlite3

# ACL support
BuildRequires:  pkgconfig(libacl)

# IDN support
BuildRequires:  pkgconfig(libidn)

# GAMIN support
%{?with_gamin:BuildRequires:	pkgconfig(gamin)}

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

BuildRequires:  pkgconfig(ldap)


Requires:		%{name}-tdeio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-libsvnqt = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-kdesvn < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdesvn = %{?epoch:%{epoch}:}%{version}-%{release}


%description
TDESvn is a graphical client for the subversion revision control
system (svn).

Besides offering common and advanced svn operations, it features
a tight integration into TDE and can be embedded into other TDE 
applications like konqueror via the TDE component technology KParts.

%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING
%{tde_prefix}/bin/tdesvn
%{tde_prefix}/bin/tdesvnaskpass
%{tde_prefix}/%{_lib}/trinity/tdesvnpart.la
%{tde_prefix}/%{_lib}/trinity/tdesvnpart.so
%{tde_prefix}/share/applications/tde/tdesvn.desktop
%{tde_prefix}/share/apps/tdeconf_update/tdesvn-use-external-update.sh
%{tde_prefix}/share/apps/tdeconf_update/tdesvnpartrc-use-external.upd
%{tde_prefix}/share/apps/tdesvn/
%{tde_prefix}/share/apps/tdesvnpart/
%{tde_prefix}/share/apps/konqueror/servicemenus/tdesvn_subversion.desktop
%{tde_prefix}/share/config.kcfg/tdesvn_part.kcfg
%{tde_prefix}/share/icons/hicolor/*/*/*.png
%{tde_prefix}/share/icons/hicolor/*/*/*.svgz
%{tde_prefix}/share/man/man1/tdesvn.1*
%{tde_prefix}/share/man/man1/tdesvnaskpass.1*
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/tdesvn/
%lang(nl) %{tde_prefix}/share/doc/tde/HTML/nl/tdesvn/
%{tde_prefix}/%{_lib}/libksvnwidgets.la
%{tde_prefix}/%{_lib}/libksvnwidgets.so
%{tde_prefix}/%{_lib}/libsvnfrontend.la
%{tde_prefix}/%{_lib}/libsvnfrontend.so
%{tde_prefix}/%{_lib}/libtdesvncfgreader.la
%{tde_prefix}/%{_lib}/libtdesvncfgreader.so
%{tde_prefix}/%{_lib}/libtdesvnevents.la
%{tde_prefix}/%{_lib}/libtdesvnevents.so
%{tde_prefix}/%{_lib}/libtdesvnhelpers.la
%{tde_prefix}/%{_lib}/libtdesvnhelpers.so

##########

%package -n trinity-libsvnqt
Group:			Development/Libraries
Summary:		Qt wrapper library for subversion [Trinity]

%description -n trinity-libsvnqt
This package provides svnqt, a Qt wrapper library around the 
subversion library.

It is based on the RapidSvn SvnCpp library, a subversion client API 
written in C++.

%files -n trinity-libsvnqt
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libsvnqt.so.4
%{tde_prefix}/%{_lib}/libsvnqt.so.4.2.2

##########

%package -n trinity-libsvnqt-devel
Group:			Development/Libraries
Requires:		trinity-libsvnqt = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		lib64tqt4-devel
Requires:		subversion-devel
Summary:		Qt wrapper library for subversion (development files) [Trinity]

%description -n trinity-libsvnqt-devel
This package contains the header files and symbolic links that developers
using svnqt will need.

%files -n trinity-libsvnqt-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/svnqt
%{tde_prefix}/%{_lib}/libsvnqt.so

##########

%package tdeio-plugins
Group:			Development/Libraries
Conflicts:	trinity-kdesdk-tdeio-plugins
Summary:		subversion I/O slaves for Trinity

Obsoletes:	trinity-kdesvn-kio-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdesvn-kio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-tdesvn-kio-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-tdesvn-kio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}

%description tdeio-plugins
This packages includes TDEIO slaves for svn, svn+file, svn+http, 
svn+https, svn+ssh. This allows you to access subversion repositories 
inside any TDEIO enabled TDE application.

This package is part of tdesvn-trinity.

%post tdeio-plugins
for proto in svn+file svn+http svn+https svn+ssh svn; do
  update-alternatives --install \
    %{tde_prefix}/share/services/${proto}.protocol \
    ${proto}.protocol \
    %{tde_prefix}/share/services/${proto}.protocol_tdesvn \
    20
done

%preun tdeio-plugins
if [ $1 -eq 0 ]; then
  for proto in svn+file svn+http svn+https svn+ssh svn; do
    update-alternatives --remove \
      ${proto}.protocol \
      %{tde_prefix}/share/services/${proto}.protocol_tdesvn || :
  done
fi

%files tdeio-plugins
%defattr(-,root,root,-)
%{tde_prefix}/share/services/kded/tdesvnd.desktop
%{tde_prefix}/share/services/ksvn+file.protocol
%{tde_prefix}/share/services/ksvn+http.protocol
%{tde_prefix}/share/services/ksvn+https.protocol
%{tde_prefix}/share/services/ksvn+ssh.protocol
%{tde_prefix}/share/services/ksvn.protocol
%{tde_prefix}/share/services/svn+file.protocol_tdesvn
%{tde_prefix}/share/services/svn+http.protocol_tdesvn
%{tde_prefix}/share/services/svn+https.protocol_tdesvn
%{tde_prefix}/share/services/svn+ssh.protocol_tdesvn
%{tde_prefix}/share/services/svn.protocol_tdesvn
%{tde_prefix}/%{_lib}/trinity/tdeio_ksvn.la
%{tde_prefix}/%{_lib}/trinity/tdeio_ksvn.so
%{tde_prefix}/%{_lib}/trinity/kded_tdesvnd.la
%{tde_prefix}/%{_lib}/trinity/kded_tdesvnd.so

%prep -a
rm -f src/svnqt/CMakeLists.txt.orig
#rm -fr src/svnqt/cache/sqlite3/


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export CMAKE_INCLUDE_PATH="%{tde_prefix}/include/tde"


%install -a
# Installs SVN protocols as alternatives
%__mv -f %{?buildroot}%{tde_prefix}/share/services/svn+file.protocol %{?buildroot}%{tde_prefix}/share/services/svn+file.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_prefix}/share/services/svn+http.protocol %{?buildroot}%{tde_prefix}/share/services/svn+http.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_prefix}/share/services/svn+https.protocol %{?buildroot}%{tde_prefix}/share/services/svn+https.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_prefix}/share/services/svn+ssh.protocol %{?buildroot}%{tde_prefix}/share/services/svn+ssh.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_prefix}/share/services/svn.protocol %{?buildroot}%{tde_prefix}/share/services/svn.protocol_tdesvn

# Locales
%find_lang %{tde_pkg}

