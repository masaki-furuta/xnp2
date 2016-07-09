Name:           xnp2
Version:        0.86
Release:        3%{dist}
Summary:        Xnp2 is a port for UNIX with X11 of "Neko Project II" PC-9801 emulator.
Group:          System/Emulators/PC
License:        BSD
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/build-root-%{name}
BuildRequires:  gcc-c++ libtool
BuildRequires:  gtk2-devel nasm
BuildRequires:  SDL2-devel SDL2_mixer-devel
BuildRequires:  libXv-devel
BuildRequires:  libusb-devel
Patch0:         gcc6-dirty.patch

%description
Xnp2 is a port for UNIX with X11 of "Neko Project II" PC-9801 emulator. http://www.nonakap.org/np2/

%prep
%setup -q
%patch0 -p1 -b .gcc6

%build
cd x11
#%configure
%configure --enable-build-all
make %{?_smp_mflags}

%install
cd x11
make install DESTDIR=$RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_mandir}/man1/xnp2.*
%{_mandir}/man1/xnp21.*
%{_bindir}/xnp2
%{_bindir}/xnp21
%dir %{_datadir}/xnp2
%{_datadir}/xnp2/*

%doc x11/README.ja

%changelog
* Sun Jul 10 2016 Masaki Furuta - 0.86
- Rebuild for Fedora 24 with gcc6
