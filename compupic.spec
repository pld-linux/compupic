Summary:	A commercial picture browsing tool
Summary(pl.UTF-8):	Komercyjna aplikacja do przeglądania obrazków
Name:		compupic
Version:	5.1.1063
Release:	3
License:	Proprietary (Free for non-business use. Busines use requires registration.)
Group:		X11/Applications/Multimedia
Source0:	http://www.photodex.com/files.system/linux/%{name}-%{version}-i386-Linux.tar.gz
# Source0-md5:	7c4c1f042cfef63055de960933d7a19c
Source1:	%{name}.desktop
URL:		http://www.photodex.com/products/compupic/index.html
BuildRequires:	sed >= 4.0
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The fastest, easiest to use software for browsing and viewing
pictures. CompuPic gives you unmatched performance paired with a full
set of features for editing, sharing, and using your digital content.

%description -l pl.UTF-8
Najszybsze i najłatwiejsze w użyciu narzędzie do przeglądania i
podglądu obrazków. CompuPic daje nieporównywalną wydajność połączoną z
pełną gamą możliwości edycji, udostępniania oraz używania cyfrowych
zasobów.

%prep
%setup -q -n %{name}-%{version}-i386-Linux
> install.sh
mkdir -p compupic
tar xf compupic.tar -C compupic
mv compupic/compupic.1 .
mv compupic/LICENSE .
mv compupic/README .
mv compupic/*.xpm .
%{__sed} -i -e 's/libn/FOOB/g;s/nss/FOO/g' compupic/compupic

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/compupic,%{_pixmapsdir},%{_desktopdir}}

cp -a compupic/* $RPM_BUILD_ROOT%{_datadir}/compupic
cp -a compupic.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -a *.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
ln -s %{_datadir}/compupic/compupic $RPM_BUILD_ROOT%{_bindir}/compupic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE
%attr(755,root,root) %{_bindir}/compupic
%dir %{_datadir}/compupic
# XXX: x86 binary can't be in %{_datadir}
%attr(755,root,root) %{_datadir}/compupic/compupic
%doc %{_datadir}/compupic/english
%doc %{_datadir}/compupic/web
%{_datadir}/compupic/cpicoeme.bmp
%{_datadir}/compupic/defscr
%{_datadir}/compupic/docscr
%{_datadir}/compupic/order.txt
%{_pixmapsdir}/cpicicon-*.xpm
%{_desktopdir}/compupic.desktop
%{_mandir}/man1/compupic.1*
