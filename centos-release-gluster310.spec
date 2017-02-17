Summary: Gluster 3.10 (Long Term Stable) packages from the CentOS Storage SIG repository
Name: centos-release-gluster310
Version: 1.0
Release: 1%{?dist}
License: GPLv2
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
Source0: CentOS-Gluster-3.10.repo

BuildArch: noarch

# This provides the public key to verify the RPMs
Requires: centos-release-storage-common

# Provides only, no Obsoletes or Conflicts because it should not automatically
# replace previous centos-release-gluster* packages. Also, tools from older
# repositories should still be able to work with the new version.
Provides: centos-release-gluster = 3.10

%description
yum configuration for Gluster 3.10 packages from the CentOS Storage SIG.
Gluster 3.10 is a Long Term Stable release and will receive updates for 12
months. For more details about the Long Term Stable and Short Term Stable
release schedule, see https://www.gluster.org/community/release-schedule

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Gluster-3.10.repo

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-Gluster-3.10.repo

%changelog
* Fri Feb 17 2017 Niels de Vos <ndevos@redhat.com> - 1.0-1
- Initial version based on centos-release-gluster39
