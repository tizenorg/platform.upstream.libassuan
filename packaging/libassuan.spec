Name:           libassuan
Version:        2.0.2
Release:        0
License:        GPL-2.0+ ; LGPL-2.1+
Summary:        IPC library used by GnuPG version 2
Url:            http://www.gnupg.org/aegypten2/index.html
Group:          Development/Libraries/C and C++
Source:         %{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRequires:  libgpg-error-devel >= 1.4
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libassuan is the IPC library used by gpg2 (GnuPG version 2)

%package devel
Summary:        IPC library used by GnuPG version 2
Requires:       libassuan = %{version}
Requires:       libgpg-error-devel

%description devel
Libassuan is the IPC library used by gpg2 (GnuPG version 2)

gpgme also uses libassuan to communicate with a libassuan-enabled GnuPG
v2 server, but it uses it's own copy of libassuan.

%prep
%setup -q

%build
# Compile with PIC, library is linked into shared libraries:
export CFLAGS="%{optflags}"
export LDFLAGS="-fPIC"
%configure
make %{?_smp_mflags}

%install
%make_install

%post  -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/assuan.info.gz

%postun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/assuan.info.gz


%files
%defattr(-,root,root)
%{_libdir}/libassuan.so.*

%files devel
%defattr(-,root,root)
%doc %{_infodir}/assuan*
%{_includedir}/*.h
%{_bindir}/*-config
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/*.m4
%{_libdir}/libassuan.so

%changelog
