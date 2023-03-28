Name:           eww
Version:        0.4.0
Release:        1%{?dist}
Summary:        ElKowars wacky widgets

License:        MIT
URL:            https://github.com/elkowar/eww
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cairo-devel gtk3-devel gtk-layer-shell-devel pango-devel
BuildRequires:  glib2-devel glibc-devel gcc gdk-pixbuf2-devel glib2-devel
Requires:       cairo glibc libgcc gtk3 gtk-layer-shell pango gdk-pixbuf2 glib2

%description
Elkowars Wacky Widgets is a standalone widget system made in Rust that allows
you to implement your own, custom widgets in any window manager.

%global debug_package %{nil}
%prep
%autosetup -n eww-%{version}
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- --default-toolchain none -y

%build
source "$HOME/.cargo/env"
cargo build --release --no-default-features --features=wayland


%install
%{__mkdir} -p %{buildroot}%{_bindir}
%{__install} -m 755 %{_builddir}/%{name}-%{version}/target/release/eww %{buildroot}%{_bindir}/eww
# License
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}
mkdir -p %{buildroot}%{_docdir}/%{name}
mv LICENSE %{buildroot}%{_datadir}/licenses/%{name}/
mv README.md %{buildroot}%{_docdir}/%{name}/


%files
%license LICENSE
%doc README.md
%{_bindir}/eww


%changelog
* Tue Mar 28 2023 Halvor <flkz@proton.me>
- 
