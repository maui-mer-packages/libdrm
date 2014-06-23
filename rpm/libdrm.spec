# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       libdrm

# >> macros
# << macros

Summary:    Direct Rendering Manager runtime library
Version:    2.4.54
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://dri.sourceforge.net
Source0:    %{name}-%{version}.tar.xz
Source1:    91-drm-modeset.rules
Source100:  libdrm.yaml
Patch0:     libdrm-make-dri-perms-okay.patch
Patch1:     libdrm-2.4.0-no-bc.patch
Patch2:     libdrm-2.4.25-check-programs.patch
Requires:   udev
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(pciaccess) >= 0.10
BuildRequires:  pkgconfig(pthread-stubs)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  docbook-style-xsl

%description
%{summary}


%package -n drm-utils
Summary:    Direct Rendering Manager utilities
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}

%description -n drm-utils
Utility programs for the kernel DRM interface.  Will void your warranty.


%ifarch %arm
%package exynos
Summary:    Direct Rendering Manager exynos api
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description exynos
%{summary}.


%package freedreno
Summary:    Direct Rendering Manager freedreno api
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description freedreno
%{summary}.


%package omap
Summary:    Direct Rendering Manager omap api
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description omap
%{summary}.
%endif


%ifarch %{ix86} x86_64 ia64
%package radeon
Summary:    Direct Rendering Manager radeon api
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description radeon
%{summary}.


%package nouveau
Summary:    Direct Rendering Manager nouveau api
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description nouveau
%{summary}.


%package intel
Summary:    Direct Rendering Manager intel api
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description intel
%{summary}.
%endif


%package devel
Summary:    Direct Rendering Manager development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
%ifarch %arm
Requires:   %{name}-exynos = %{version}-%{release}
Requires:   %{name}-freedreno = %{version}-%{release}
Requires:   %{name}-omap = %{version}-%{release}
%endif
%ifarch %{ix86} x86_64 ia64
Requires:   %{name}-radeon = %{version}-%{release}
Requires:   %{name}-nouveau = %{version}-%{release}
Requires:   %{name}-intel = %{version}-%{release}
%endif
Requires:   kernel-headers

%description devel
%{summary}.


%prep
%setup -q -n %{name}-%{version}/upstream

# libdrm-make-dri-perms-okay.patch
%patch0 -p1
# libdrm-2.4.0-no-bc.patch
%patch1 -p1
# libdrm-2.4.25-check-programs.patch
%patch2 -p1
# >> setup
# << setup

%build
unset LD_AS_NEEDED
# >> build pre
%autogen \
%ifarch %arm
	--enable-exynos-experimental-api \
	--enable-freedreno-experimental-api \
	--enable-omap-experimental-api \
%endif
	--enable-udev
# << build pre


make %{?_smp_mflags}

# >> build post
pushd tests
make %{?smp_mflags} `make check-programs`
popd
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
pushd tests
mkdir -p $RPM_BUILD_ROOT%{_bindir}
for foo in $(make check-programs) ; do
install -m 0755 .libs/$foo $RPM_BUILD_ROOT%{_bindir}
done
popd

mkdir -p $RPM_BUILD_ROOT/%{_lib}/udev/rules.d/
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT/%{_lib}/udev/rules.d/
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%ifarch %arm
%post exynos -p /sbin/ldconfig

%postun exynos -p /sbin/ldconfig

%post freedreno -p /sbin/ldconfig

%postun freedreno -p /sbin/ldconfig

%post omap -p /sbin/ldconfig

%postun omap -p /sbin/ldconfig
%endif

%ifarch %{ix86} x86_64 ia64
%post radeon -p /sbin/ldconfig

%postun radeon -p /sbin/ldconfig

%post nouveau -p /sbin/ldconfig

%postun nouveau -p /sbin/ldconfig

%post intel -p /sbin/ldconfig

%postun intel -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%doc README
%{_libdir}/libdrm.so.*
%{_libdir}/libkms.so.*
%{_mandir}/man3/drm*.3*
%{_mandir}/man7/drm*.7*
/%{_lib}/udev/rules.d/91-drm-modeset.rules
# >> files
# << files

%files -n drm-utils
%defattr(-,root,root,-)
%{_bindir}/dristat
%{_bindir}/drmstat
%ifarch %{ix86} x86_64 ia64
%{_bindir}/gem_basic
%{_bindir}/gem_flink
%{_bindir}/gem_mmap
%{_bindir}/gem_readwrite
%endif
%{_bindir}/getclient
%{_bindir}/getstats
%{_bindir}/getversion
%{_bindir}/name_from_fd
%{_bindir}/openclose
%{_bindir}/setversion
%{_bindir}/updatedraw
# >> files drm-utils
# << files drm-utils

%ifarch %arm
%files exynos
%defattr(-,root,root,-)
%{_libdir}/libdrm_exynos.so.*
# >> files exynos
# << files exynos

%files freedreno
%defattr(-,root,root,-)
%{_libdir}/libdrm_freedreno.so.*
# >> files freedreno
# << files freedreno

%files omap
%defattr(-,root,root,-)
%{_libdir}/libdrm_omap.so.*
# >> files omap
# << files omap
%endif

%ifarch %{ix86} x86_64 ia64
%files radeon
%defattr(-,root,root,-)
%{_libdir}/libdrm_radeon.so.*
# >> files radeon
# << files radeon

%files nouveau
%defattr(-,root,root,-)
%{_libdir}/libdrm_nouveau.so.*
# >> files nouveau
# << files nouveau

%files intel
%defattr(-,root,root,-)
%{_libdir}/libdrm_intel.so.*
# >> files intel
# << files intel
%endif

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/libdrm
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
# >> files devel
# << files devel