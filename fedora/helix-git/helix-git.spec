Name:           helix-git
Version:        23.03
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
Release: 2.%{?build_timestamp}%{?dist}
Summary:        A post-modern modal text editor.

License:        MPL-2.0
URL:            https://github.com/helix-editor/helix
Source0:        %{url}/archive/master.tar.gz

BuildRequires:  tar xz cargo git clang



%description
A Kakoune / Neovim inspired editor, written in Rust.



%prep
%autosetup -n helix-master



%install
cargo install --path helix-term --locked --root %{buildroot}%{_datadir}/%{name}
rm -rf runtime/grammars/sources

# Bin / Runtime
mv runtime %{buildroot}%{_datadir}/%{name}/
# mv %{buildroot}%{_datadir}/%{name}/bin/hx %{buildroot}%{_datadir}/%{name}/

# License
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}
mv LICENSE %{buildroot}%{_datadir}/licenses/%{name}/

# Docs
mkdir -p %{buildroot}%{_docdir}/%{name}
mv README.md %{buildroot}%{_docdir}/%{name}/

rm %{buildroot}%{_datadir}/%{name}/.crates.toml
rm %{buildroot}%{_datadir}/%{name}/.crates2.json

# Bin
mkdir -p %{buildroot}%{_bindir}
touch %{buildroot}%{_bindir}/hx
cat >> %{buildroot}%{_bindir}/hx <<EOF
#!/usr/bin/env sh

HELIX_RUNTIME="%{_datadir}/%{name}/runtime" exec %{_datadir}/%{name}/bin/hx "\$@"
EOF
chmod +x %{buildroot}%{_prefix}/bin/hx

%files
%license LICENSE
%doc README.md
%{_bindir}/hx
%{_datadir}/%{name}/



%changelog
* Fri Mar 31 2023 Halvor <flkz@proton.me> - 23.03-2.20230331
- Update version to 23.03

* Thu Nov 10 2022 Halvor <flkz@proton.me>
- 
