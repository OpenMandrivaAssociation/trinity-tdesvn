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
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

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

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/development/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_SKIP_RPATH=OFF
BuildOption:    -DCMAKE_SKIP_INSTALL_RPATH=OFF
BuildOption:    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON
BuildOption:    -DCMAKE_INSTALL_RPATH="%{tde_libdir}"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DBIN_INSTALL_DIR=%{tde_bindir}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_includedir}
BuildOption:    -DLIB_INSTALL_DIR=%{tde_libdir}
BuildOption:    -DMAN_INSTALL_DIR=%{tde_mandir}
BuildOption:    -DPKGCONFIG_INSTALL_DIR=%{tde_tdelibdir}/pkgconfig
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_datadir}
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
%{tde_bindir}/tdesvn
%{tde_bindir}/tdesvnaskpass
%{tde_tdelibdir}/tdesvnpart.la
%{tde_tdelibdir}/tdesvnpart.so
%{tde_datadir}/applications/tde/tdesvn.desktop
%{tde_datadir}/apps/tdeconf_update/tdesvn-use-external-update.sh
%{tde_datadir}/apps/tdeconf_update/tdesvnpartrc-use-external.upd
%{tde_datadir}/apps/tdesvn/
%{tde_datadir}/apps/tdesvnpart/
%{tde_datadir}/apps/konqueror/servicemenus/tdesvn_subversion.desktop
%{tde_datadir}/config.kcfg/tdesvn_part.kcfg
%{tde_datadir}/icons/hicolor/*/*/*.png
%{tde_datadir}/icons/hicolor/*/*/*.svgz
%{tde_mandir}/man1/tdesvn.1*
%{tde_mandir}/man1/tdesvnaskpass.1*
%lang(en) %{tde_tdedocdir}/HTML/en/tdesvn/
%lang(nl) %{tde_tdedocdir}/HTML/nl/tdesvn/
%{tde_libdir}/libksvnwidgets.la
%{tde_libdir}/libksvnwidgets.so
%{tde_libdir}/libsvnfrontend.la
%{tde_libdir}/libsvnfrontend.so
%{tde_libdir}/libtdesvncfgreader.la
%{tde_libdir}/libtdesvncfgreader.so
%{tde_libdir}/libtdesvnevents.la
%{tde_libdir}/libtdesvnevents.so
%{tde_libdir}/libtdesvnhelpers.la
%{tde_libdir}/libtdesvnhelpers.so

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
%{tde_libdir}/libsvnqt.so.4
%{tde_libdir}/libsvnqt.so.4.2.2

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
%{tde_includedir}/svnqt
%{tde_libdir}/libsvnqt.so

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
    %{tde_datadir}/services/${proto}.protocol \
    ${proto}.protocol \
    %{tde_datadir}/services/${proto}.protocol_tdesvn \
    20
done

%preun tdeio-plugins
if [ $1 -eq 0 ]; then
  for proto in svn+file svn+http svn+https svn+ssh svn; do
    update-alternatives --remove \
      ${proto}.protocol \
      %{tde_datadir}/services/${proto}.protocol_tdesvn || :
  done
fi

%files tdeio-plugins
%defattr(-,root,root,-)
%{tde_datadir}/services/kded/tdesvnd.desktop
%{tde_datadir}/services/ksvn+file.protocol
%{tde_datadir}/services/ksvn+http.protocol
%{tde_datadir}/services/ksvn+https.protocol
%{tde_datadir}/services/ksvn+ssh.protocol
%{tde_datadir}/services/ksvn.protocol
%{tde_datadir}/services/svn+file.protocol_tdesvn
%{tde_datadir}/services/svn+http.protocol_tdesvn
%{tde_datadir}/services/svn+https.protocol_tdesvn
%{tde_datadir}/services/svn+ssh.protocol_tdesvn
%{tde_datadir}/services/svn.protocol_tdesvn
%{tde_tdelibdir}/tdeio_ksvn.la
%{tde_tdelibdir}/tdeio_ksvn.so
%{tde_tdelibdir}/kded_tdesvnd.la
%{tde_tdelibdir}/kded_tdesvnd.so

%prep -a
rm -f src/svnqt/CMakeLists.txt.orig
#rm -fr src/svnqt/cache/sqlite3/


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export CMAKE_INCLUDE_PATH="%{tde_tdeincludedir}"


%install -a
# Installs SVN protocols as alternatives
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+file.protocol %{?buildroot}%{tde_datadir}/services/svn+file.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+http.protocol %{?buildroot}%{tde_datadir}/services/svn+http.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+https.protocol %{?buildroot}%{tde_datadir}/services/svn+https.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+ssh.protocol %{?buildroot}%{tde_datadir}/services/svn+ssh.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_datadir}/services/svn.protocol %{?buildroot}%{tde_datadir}/services/svn.protocol_tdesvn

# Locales
%find_lang %{tde_pkg}

