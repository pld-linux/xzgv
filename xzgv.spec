Summary:	picture viewer for X, with thumbnail-based file selector
Summary(pl):	Przegl±darka plików graficznych pod X'y z obs³ug± thumbnail'i
Name:		xzgv
Version:	0.7
Release:	2
License:	GPL
Vendor:		Russell Marks <russell.marks@dtn.ntl.com>
Group:		X11/Applications/Graphics
URL:		ftp://metalab.unc.edu/pub/Linux/apps/graphics/viewers/X/
Source0:	ftp://metalab.unc.edu/pub/Linux/apps/graphics/viewers/X/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-patch
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xzgv is a picture viewer for X, with a thumbnail-based file selector.
It uses GTK+ and Imlib. Most file formats are supported, and the
thumbnails used are compatible with xv, zgv, and the Gimp. It can also
be used with `xzgv file(s)', to effectively bypass the file selector.
For more on how xzgv works and how to use it, do `info xzgv' or `man
xzgv' once it's installed.

%description -l pl
xzgv jest przegl±dark± plików graficznych pod X'y z obs³ug±
thumbnail'i. U¿ywa GTK+ i Imlib'a. Obs³uguje wiêkszo¶æ formatów, a
thumbnail'e s± kompatybilne z xv, zgv, oraz Gimp. Mo¿e byæ tak¿e
u¿ywane z `xzgv file(s)', aby efektywnie pomin±æ wbudowany selektor
plików. Wiêcej informacji jak dzia³aj± te programy i jak ich u¿ywaæ
uzyskasz ze stron manuali: `info xzgv' oraz `man xzgv'. Oczywi¶cie po
instalacji.

%prep
%setup -q
%patch0 -p1

%build
LDFLAGS="%{rpmldflags}" ; export LDFLAGS
%{__make} OPT="%{rpmcflags}" PREFIX=%{_prefix}

(cd doc; rm -f *.gz; makeinfo xzgv.texi; gzip -9nf xzgv.info*)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	INFODIR=$RPM_BUILD_ROOT%{_infodir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/xzgv
%{_infodir}/xzgv*.gz
%{_mandir}/man1/*
%{_applnkdir}/Graphics/Viewers/*
