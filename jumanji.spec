%define		gitver	0931613fda448180596e142ba7d92fcc9b2e983b

Summary:	Web browser
Name:		jumanji
Version:	0.0.0
Release:	0.%{gitver}.1
License:	BSD-like
Group:		Libraries
#Source0:	https://pwmt.org/projects/jumanji/download/%{name}-%{version}.tar.gz
#
# git clone git://pwmt.org/jumanji.git
# cd jumanji
# git checkout --track -b develop origin/develop
# git archive --format=tar --prefix=jumanji/ develop | gzip -9 > jumanji-GITVER.tar.gz
#
Source:		%{name}-%{gitver}.tar.gz
BuildRequires:	girara3-devel
BuildRequires:	gtk+3-webkit-devel
BuildRequires:	intltool
BuildRequires:	libsoup-devel
BuildRequires:	pkg-config
Requires:	glib-networking
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jumanji is a highly customizable and functional web browser based on
the libwebkit web content engine and the gtk+ toolkit. The idea behind
jumanji is a web browser that provides a minimalistic and space saving
interface as well as an easy usage that mainly focuses on keyboard
interaction like vimperator does.

%prep
%setup -qn %{name}

%{__sed} -i "s/^DFLAGS.*/DFLAGS =/" config.mk

%build
export CFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README
%attr(755,root,root) %{_bindir}/jumanji
%{_mandir}/man1/jumanji.1*

