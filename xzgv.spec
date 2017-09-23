Summary:	Picture viewer for X, with thumbnail-based file selector
Summary(pl.UTF-8):	Przeglądarka plików graficznych pod X Window System z obsługą miniatur
Name:		xzgv
Version:	0.9.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	87d14e59268ace5ba83005a6e20e2be7
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-patch
URL:		http://sourceforge.net/projects/xzgv
BuildRequires:	gawk
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	pkgconfig
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xzgv is a picture viewer for X, with a thumbnail-based file selector.
It uses GTK+ and Imlib. Most file formats are supported, and the
thumbnails used are compatible with xv, zgv, and the Gimp. It can also
be used with `xzgv file(s)', to effectively bypass the file selector.
For more on how xzgv works and how to use it, do `info xzgv' or `man
xzgv' once it's installed.

%description -l pl.UTF-8
xzgv jest przeglądarką plików graficznych pod X Window System z
obsługą miniatur. Używa GTK+ i Imliba. Obsługuje większość formatów, a
miniatury są zgodne z xv, zgv oraz Gimpem. Może być także używany jako
`xzgv plik(i)' w celu efektywnego pominięcia wbudowanego okna wyboru
plików. Więcej informacji jak działa ten program i jak go używać można
znaleźć na stronach podręcznika: `info xzgv' oraz `man xzgv'.
Oczywiście po instalacji.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	PREFIX=%{_prefix} \
	OPT="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

cd doc
rm -f *.gz
makeinfo xzgv.texi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	INFODIR=$RPM_BUILD_ROOT%{_infodir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/xzgv
%{_infodir}/xzgv.info*
%{_mandir}/man1/xzgv.1*
%{_desktopdir}/xzgv.desktop
%{_pixmapsdir}/xzgv.png
