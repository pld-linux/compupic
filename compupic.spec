Summary:	A commercial picture browsing tool.
Summary(pl):	Komercyjna aplikacja do przegl±dania obrazków
Name:		compupic
Version:	5.1.1063
Release:	2
License:	Proprietary (Free for non-business use. Busines use requires registration.)
Vendor:		Photodex Corporation
Group:		X11/Applications/Multimedia
Source0:	http://www.photodex.com/files.system/linux/%{name}-%{version}-i386-Linux.tar.gz 
# Source0-md5:	7c4c1f042cfef63055de960933d7a19c
Source1:	%{name}.desktop
URL:		http://www.photodex.com/products/compupic/index.html
BuildRequires:	perl-base
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The fastest, easiest to use software for browsing and viewing
pictures. CompuPic gives you unmatched performance paired with a full
set of features for editing, sharing, and using your digital content.

%description -l pl
Najszybsze i naj³atwiejsze w u¿yciu narzêdzie do przegl±dania i
podgl±du obrazków. CompuPic daje nieporównywaln± wydajno¶æ po³±czon± z
pe³n± gam± mo¿liwo¶ci edycji, udostêpniania oraz u¿ywania cyfrowych
zasobów.

%prep
%setup -q -n compupic-5.1.1063-i386-Linux
> install.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/compupic,%{_pixmapsdir},%{_desktopdir}}

tar xf compupic.tar -C $RPM_BUILD_ROOT%{_datadir}/compupic
mv -f $RPM_BUILD_ROOT%{_datadir}/compupic/compupic.1 $RPM_BUILD_ROOT%{_mandir}/man1
mv $RPM_BUILD_ROOT%{_datadir}/compupic/*.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
mv $RPM_BUILD_ROOT%{_datadir}/compupic/LICENSE .
mv $RPM_BUILD_ROOT%{_datadir}/compupic/README .
cd $RPM_BUILD_ROOT%{_datadir}/compupic
%{__perl} -pi -e 's/libn/FOOB/g' compupic
%{__perl} -pi -e 's/nss/FOO/g' compupic
ln compupic ../../bin/compupic
cd -

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE
%attr(755,root,root) %{_bindir}/compupic
%dir %{_datadir}/compupic
# XXX: it can't be in %{_datadir}
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
