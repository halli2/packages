Name:           eww
Version:        0.4.0
Release:        1%{?dist}
Summary:        ElKowars wacky widgets

License:        MIT
URL:            https://github.com/elkowar/eww
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cairo-devel gtk3-devel gtk-layer-shell-devel pango-devel
BuildRequires:  glib2-devel glibc-dvel
Requires:       cairo glibc libgcc

%description


%prep
%autosetup -n eww-%{version}
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- --default-toolchain none -y

%build
cargo build --release --no-default-features --features=wayland


%install
%{__mkdir} -p %{buildroot}%{_bindir}
%{__install} -m 755 %{_builddir}/%{name}/target/release/eww %{buildroot}%{_bindir}/eww


%files
%{_bindir}/eww


%changelog
* Tue Mar 28 2023 Halvor <flkz@proton.me>
- 
