# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-perky
Epoch: 100
Version: 0.9.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Friendly, easy, Pythonic text file format
License: MIT
URL: https://github.com/larryhastings/perky/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Perky is a new, simple "rcfile" text file format for Python programs. It
solves the same problem as "INI" files, "TOML" files, and "JSON" files,
but with its own opinion about how to best solve the problem.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-perky
Summary: Friendly, easy, Pythonic text file format
Requires: python3
Provides: python3-perky = %{epoch}:%{version}-%{release}
Provides: python3dist(perky) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-perky = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(perky) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-perky = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(perky) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-perky
Perky is a new, simple "rcfile" text file format for Python programs. It
solves the same problem as "INI" files, "TOML" files, and "JSON" files,
but with its own opinion about how to best solve the problem.

%files -n python%{python3_version_nodots}-perky
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-perky
Summary: Friendly, easy, Pythonic text file format
Requires: python3
Provides: python3-perky = %{epoch}:%{version}-%{release}
Provides: python3dist(perky) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-perky = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(perky) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-perky = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(perky) = %{epoch}:%{version}-%{release}

%description -n python3-perky
Perky is a new, simple "rcfile" text file format for Python programs. It
solves the same problem as "INI" files, "TOML" files, and "JSON" files,
but with its own opinion about how to best solve the problem.

%files -n python3-perky
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
