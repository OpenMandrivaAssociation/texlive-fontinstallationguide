%global tl_name fontinstallationguide
%global tl_revision 59755

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.14
Release:	%{tl_revision}.1
Summary:	Font installation guide
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/Type1fonts/fontinstallationguide
License:	fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontinstallationguide.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontinstallationguide.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This guide discusses the most common scenarios you are likely to
encounter when installing Type 1 PostScript fonts. While the individual
tools employed in the installation process are documented well, the
actual difficulty most users are facing when trying to install new fonts
is understanding how to put all the pieces together. This is what this
guide is about.

