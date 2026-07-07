Name:           libnvme
Version:        1.16.2
Release:        1%{?dist}
Summary:        The libnvme library provides an API for working with NVMe devices
Summary(ru):    Библиотека libnvme предоставляет API для работы с NVMe-устройствами

License:        LGPL-2.1-or-later
URL:            https://github.com/linux-nvme/libnvme
Source0:        https://github.com/linux-nvme/libnvme/archive/v%{version}/%{name}-%{version}.tar.gz

Packager:       NICE SOFT GROUP LLC (ООО "НАЙС СОФТ ГРУПП") 5024245440 <niceos@ncsgp.ru>
Vendor:         NiceSOFT
Distribution:   NiceOS.Core
BugURL:         https://bugs.niceos.ru/
VCS:            https://specs.niceos.ru/rmps/%{name}

BuildRequires:  dbus-devel
BuildRequires:  gcc
BuildRequires:  json-c-devel
BuildRequires:  meson
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:	python3-xml
BuildRequires:  swig
BuildRequires:  keyutils-devel

Requires:       dbus
Requires:       json-c
Requires:       openssl

%description
libnvme provides a set of tools and a C API for interacting with NVMe devices.
It enables applications to manage and monitor NVMe drives, including operations
such as querying controller and namespace information, and performing various
management and diagnostic tasks.

%description -l ru
libnvme предоставляет набор инструментов и API для работы с NVMe-устройствами.
Она позволяет разрабатывать приложения для управления и мониторинга NVMe-накопителей
и выполнения различных операций (получение информации о контроллерах/пространствах
имён, диагностика и т.п.).

%package devel
Summary:        Development files for the libnvme library
Summary(ru):    Файлы разработки для библиотеки libnvme
Requires:       %{name} = %{version}-%{release}

%description -n %{name}-devel
This subpackage contains headers, linkable library symlinks, and pkg-config files
required to build applications using libnvme.

%description -l ru -n %{name}-devel
Подпакет devel содержит заголовочные файлы, библиотеки для линковки и файлы
pkg-config, необходимые для компиляции и разработки приложений, использующих libnvme.

%package -n python3-libnvme
Summary:        Python bindings for the libnvme library
Summary(ru):    Python-биндинги для библиотеки libnvme
Requires:       %{name} = %{version}-%{release}
Requires:       python3
Provides:       python3-nvme = %{version}-%{release}

%description -n python3-libnvme
Python bindings for libnvme, enabling NVMe management and monitoring from Python
applications.

%description -l ru -n python3-libnvme
Подпакет python3-libnvme содержит Python-привязки для работы с NVMe-устройствами и
предоставляет удобный интерфейс для управления и мониторинга NVMe-накопителей на Python.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%if 0%{?with_check}
%check
%meson_test
%endif

%files
%attr(0755,root,root) %{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h
%{_includedir}/nvme/*.h

%files -n python3-libnvme
%{python3_sitearch}/%{name}/

%changelog
* Tue Jul 07 2026 NiceOS Team <support@niceos.ru> - 1.16.2-1
- EN: Update to upstream version 1.16.2.
- RU: Обновление до upstream-версии 1.16.2.


* Fri Jan 09 2026 NiceOS Team <niceos@ncsgp.ru> - 1.16.1-1
- Initial build for NiceOS (Первая сборка для НАЙС.ОС)
