# revision 30255
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/bahasa
# catalog-date 2013-05-06 22:45:34 +0200
# catalog-license lppl1.3
# catalog-version 1.0l
Name:		texlive-babel-bahasa
Version:	1.0l
Release:	9
Summary:	Support for Bahasa within babel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/bahasa
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-bahasa.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-bahasa.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-bahasa.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides two sets of language typesetting support,
for Bahasa Indonesia and Bahasa Malaysia.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-bahasa/bahasai.ldf
%{_texmfdistdir}/tex/generic/babel-bahasa/bahasam.ldf
%doc %{_texmfdistdir}/doc/generic/babel-bahasa/bahasa.pdf
%doc %{_texmfdistdir}/doc/generic/babel-bahasa/bahasam.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-bahasa/bahasa.dtx
%doc %{_texmfdistdir}/source/generic/babel-bahasa/bahasa.ins
%doc %{_texmfdistdir}/source/generic/babel-bahasa/bahasam.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
