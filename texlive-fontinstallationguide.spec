Name:		texlive-fontinstallationguide
Version:	59755
Release:	1
Summary:	Font installation guide
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fontinstallationguide
License:	fdl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontinstallationguide.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontinstallationguide.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This guide discusses the most common scenarios you are likely
to encounter when installing Type 1 PostScript fonts. While the
individual tools employed in the installation process are
documented well, the actual difficulty most users are facing
when trying to install new fonts is understanding how to put
all the pieces together. This is what this guide is about.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/fonts/fontinstallationguide

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
