Summary: NethServer MariaDB 10.5 configuration
Name: nethserver-rh-mariadb105
Version: 0.0.1
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: rh-mariadb105
Requires: nethserver-base

BuildRequires: nethserver-devtools 

%description
NethServer MariaDB 10.5 configuration

%prep
%setup

%build
%{__mkdir} -p root/var/log/rh-mariadb105
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} \
    --dir   /var/log/rh-mariadb105 'attr(0755,mysql,mysql)' \
%{buildroot} > %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
