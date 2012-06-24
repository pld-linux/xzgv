Summary:	Picture viewer for X, with thumbnail-based file selector
Summary(pl):	Przegl�darka plik�w graficznych pod X'y z obs�ug� miniatur
Name:		xzgv
Version:	0.7
Release:	3
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://xzgv.browser.org/%{name}-%{version}.tar.gz
# Source0-md5:	37b5bd8286de9f1047f603879460b364
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-patch
URL:		http://xzgv.browser.org/
BuildRequires:	gawk
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xzgv is a picture viewer for X, with a thumbnail-based file selector.
It uses GTK+ and Imlib. Most file formats are supported, and the
thumbnails used are compatible with xv, zgv, and the Gimp. It can also
be used with `xzgv file(s)', to effectively bypass the file selector.
For more on how xzgv works and how to use it, do `info xzgv' or `man
xzgv' once it's installed.

%description -l pl
xzgv jest przegl�dark� plik�w graficznych pod X'y z obs�ug� miniatur.
U�ywa GTK+ i Imliba. Obs�uguje wi�kszo�� format�w, a miniatury s�
zgodne z xv, zgv oraz Gimp. Mo�e by� tak�e u�ywany jako `xzgv plik(i)'
w celu efektywnego pomin�� wbudowany selektor plik�w. Wi�cej
informacji jak dzia�a ten program i jak go u�ywa� mo�na znale�� na
stronach podr�cznika: `info xzgv' oraz `man xzgv'. Oczywi�cie po
instalacji.

%prep
%setup -q
%patch0 -p1

%build
LDFLAGS="%{rpmldflags}" ; export LDFLAGS
%{__make} OPT="%{rpmcflags}" PREFIX=%{_prefix}

cd doc
rm -f *.gz
makeinfo xzgv.texi
gzip -9nf xzgv.info*
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Graphics/Viewers,%{_pixmapsdir}}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	INFODIR=$RPM_BUILD_ROOT%{_infodir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/xzgv
%{_infodir}/xzgv*
%{_mandir}/man1/*
%{_applnkdir}/Graphics/Viewers/*
%{_pixmapsdir}/*
