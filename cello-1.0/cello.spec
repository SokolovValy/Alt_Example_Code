Name: cello
Version: 1.0
Release: alt1
Summary: Hello World example implemented in C
Group: Other

License: GPLv3+
URL: https://www.example.com/%{name}

Source0: https://www.example.com/%{name}/releases/%{name}-%{version}.tar

BuildRequires: gcc
BuildRequires: make

%description
The long-tail description for our Hello World Example implemented in C.

%prep
%setup -q

%build
%make

%install
%makeinstall_std

%files
%doc LICENSE
%_bindir/%name

%changelog
* Mon Sep 05 2022 Evgeny Sinelnikov <sin@altlinux.org> 1.0-alt1
- First cello package
