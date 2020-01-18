%if 0%{?fedora}
%global _with_python3 1
# Documentation generation disabled on EPEL because
# fontawesome-fonts-web package, required by python-sphinx_rtd_theme,
# is dead
%global _with_doc 1
# Tests disabled:
# - on EPEL because of missing dependencies
# - on Fedora < 25 because python-vcrpy >= 1.8.0 is required
%if 0%{?fedora} >= 25
%global _with_tests 1
%endif
%endif

%if 0%{?rhel}
%global py2_prefix python
%else
%global py2_prefix python2
%endif

%global srcname azure-sdk
# global prerelease rc6

%global common_summary Microsoft Azure SDK for Python
%global common_description This project provides a set of Python packages that make it easy to access the\
Microsoft Azure components such as ServiceManagement, Storage*, and ServiceBus.

Name:           python-%{srcname}
Version:        2.0.0
Release:        %{?prerelease:0.}3%{?prerelease:.%{prerelease}}%{?dist}
Summary:        %{common_summary}

Group:          System Environment/Libraries
# All packages are licensed under the MIT license, except:
# - azure-servicebus
# - azure-servicemanagement-legacy
License:        MIT and ASL 2.0
URL:            https://github.com/Azure/azure-sdk-for-python/
# Remember to delete examples-directory from Source file for new releases
# due to possible licensing issues
Source0:        %{srcname}-%{version}%{?prerelease}.tar.gz
# Fix install_requires option, for EPEL especially
Patch0:         %{name}-2.0.0-build.patch

BuildRequires:  %{py2_prefix}-setuptools
BuildRequires:  python2-devel

Requires:       pyOpenSSL
Requires:       %{py2_prefix}-msrest
Requires:       %{py2_prefix}-msrestazure
Requires:       %{py2_prefix}-requests

# Needed to build documentation
%if 0%{?_with_doc}
BuildRequires:  python-pip
BuildRequires:  %{py2_prefix}-sphinx
BuildRequires:  %{py2_prefix}-sphinx_rtd_theme
%endif
%if 0%{?_with_python3}
BuildRequires:  python3-devel
%endif
# Needed for tests
%if 0%{?_with_tests}
BuildRequires:  %{py2_prefix}-certifi
BuildRequires:  python-chardet
BuildRequires:  %{py2_prefix}-coverage
BuildRequires:  python-enum34
BuildRequires:  python-isodate
BuildRequires:  %{py2_prefix}-keyring
BuildRequires:  %{py2_prefix}-msrest
BuildRequires:  %{py2_prefix}-msrestazure
BuildRequires:  %{py2_prefix}-nose
BuildRequires:  %{py2_prefix}-oauthlib
BuildRequires:  %{py2_prefix}-requests
BuildRequires:  %{py2_prefix}-requests-oauthlib
BuildRequires:  python-vcrpy >= 1.8.0
%if 0%{?_with_python3}
BuildRequires:  python3-certifi
BuildRequires:  python3-chardet
BuildRequires:  python3-coverage
BuildRequires:  python3-enum34
BuildRequires:  python3-isodate
BuildRequires:  python3-keyring
BuildRequires:  python3-msrest
BuildRequires:  python3-msrestazure
BuildRequires:  python3-nose
BuildRequires:  python3-oauthlib
BuildRequires:  python3-requests
BuildRequires:  python3-requests-oauthlib
BuildRequires:  python3-vcrpy >= 1.8.0
%endif
%endif
BuildArch:      noarch

%description
%{common_description}


%if 0%{?_with_python3}
%package -n python3-%{srcname}
Summary:        %{common_summary}
Requires:       python3-msrest
Requires:       python3-msrestazure
Requires:       python3-pyOpenSSL
Requires:       python3-requests
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_description}
%endif


%if 0%{?_with_doc}
%package doc
Summary:        Documentation for %{name}
Group:          Documentation

%description doc
%{common_description}

This package provides documentation for %{name}.
%endif


%prep
%autosetup -n %{srcname}-for-python-azure_%{version}%{?prerelease} -p0

# Disable online tests requiring a valid Azure subscription
pushd azure-mgmt/tests/
rm test_batch.py \
   test_key_vault_data.py \
   test_mgmt_cdn.py \
   test_mgmt_compute.py \
   test_mgmt_datalake_analytics.py \
   test_mgmt_datalake_store.py \
   test_mgmt_dns.py \
   test_mgmt_network.py \
   test_mgmt_notificationhubs.py \
   test_mgmt_redis.py \
   test_mgmt_resource.py \
   test_mgmt_resource_links.py \
   test_mgmt_resource_locks.py \
   test_mgmt_resource_policy.py \
   test_mgmt_storage.py
popd
rm azure-servicebus/tests/test_servicebus_servicebus.py

# Disable online tests requiring python-azure-storage
# TODO: once the python-azure-storage package available, re-enable it
rm azure-servicemanagement-legacy/tests/test_legacy_mgmt_misc.py

# append bundled-directory to search path
sed -i "/^import keyring/iimport sys\nsys.path.insert(0, '%{_libdir}/fence-agents/bundled')" azure-batch/azure/batch/batch_auth.py


%build
%py2_build
%{?_with_python3:%py3_build}

# Build documentation
%if 0%{?_with_doc}
%make_build -C doc/ html
rm doc/_build/html/.buildinfo
%endif


%install
%py2_install
%if 0%{?_with_python3}
%py3_install
%endif


%check
%if 0%{?_with_tests}
%{__python2} azure_nosetests.py
%{?_with_python3:%{__python3} azure_nosetests.py}
%endif


%files -n python-%{srcname}
%doc ChangeLog.rst HOWTO.txt README.rst
%license LICENSE.txt
%{python2_sitelib}/*


%if 0%{?_with_python3}
%files -n python3-%{srcname}
%doc ChangeLog.rst HOWTO.txt README.rst
%license LICENSE.txt
%{python3_sitelib}/*
%endif


%if 0%{?_with_doc}
%files doc
%doc doc/_build/html/
%license LICENSE.txt
%endif


%changelog
* Thu Jan 25 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 2.0.0-3
- Remove examples-directory from Source tarball due to possible
  licensing issues
- Append python-keyring bundled directory to search path where needed

  Resolves: rhbz#1511222

* Sun Sep 03 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0.0-2
- Use python2- prefix for Fedora dependencies if possible
- Use parallel make to build documentation

* Thu Jun 15 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0
- Move documentation to a subpackage

* Tue Sep 27 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0.0-0.8.rc6
- Update to 2.0.0rc6

* Thu Jul 21 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0.0-0.7.rc5
- Update to 2.0.0rc5
- Build documentation
- Run tests at build

* Thu May 26 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0.0-0.6.rc4
- Update to 2.0.0rc4

* Sun May 01 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0.0-0.5.rc3
- Update to 2.0.0rc3

* Mon Apr 11 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0.0-0.4.rc2
- Update to 2.0.0rc2

* Fri Mar 25 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0.0-0.3.rc1
- Add missing dependency to enum34 Python module

* Sat Mar 05 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0.0-0.2.rc1
- Update to 2.0.0rc1

* Mon Feb 29 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0.0-0.1.a1
- Update to 2.0.0a1
- Improve macros for Python 3 subpackage

* Mon Feb 08 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Sun Jan 10 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.2-1
- Initial RPM release
