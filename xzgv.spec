Summary:	Picture viewer for X, with thumbnail-based file selector
Summary(pl):	Przegl±darka plików graficznych pod X Window System z obs³ug± miniatur
Name:		xzgv
Version:	0.8
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://xzgv.browser.org/%{name}-%{version}.tar.gz
# Source0-md5:	e392277f1447076402df2e3d9e782cb2
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
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xzgv is a picture viewer for X, with a thumbnail-based file selector.
It uses GTK+ and Imlib. Most file formats are supported, and the
thumbnails used are compatible with xv, zgv, and the Gimp. It can also
be used with `xzgv file(s)', to effectively bypass the file selector.
For more on how xzgv works and how to use it, do `info xzgv' or `man
xzgv' once it's installed.

%description -l pl
xzgv jest przegl±dark± plików graficznych pod X Window System z
obs³ug± miniatur. U¿ywa GTK+ i Imliba. Obs³uguje wiêkszo¶æ formatów,
a miniatury s± zgodne z xv, zgv oraz Gimpem. Mo¿e byæ tak¿e u¿ywany
jako `xzgv plik(i)' w celu efektywnego pominiêcia wbudowanego okna
wyboru plików. Wiêcej informacji jak dzia³a ten program i jak go
u¿ywaæ mo¿na znale¼æ na stronach podrêcznika: `info xzgv' oraz `man
xzgv'. Oczywi¶cie po instalacji.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	PREFIX=%{_prefix} \
	OPT="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

cd doc
rm -f *.gz
makeinfo xzgv.texi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Graphics/Viewers,%{_pixmapsdir}}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	INFODIR=$RPM_BUILD_ROOT%{_infodir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/xzgv
%{_infodir}/xzgv*
%{_mandir}/man1/*
%{_applnkdir}/Graphics/Viewers/*
%{_pixmapsdir}/*
