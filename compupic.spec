Summary:	A commercial picture browsing tool.
Summary(pl):	Komercyjna aplikacja do przegl±dania obrazków
Name:		compupic
Version:	5.1.1063
Release:	1
##License:	Proprietary (Free for non-business use. Busines use requires registration.)
Copyright:	Photodex Corporation
Group:		X11/Applications/Multimedia
Source0:	http://www.photodex.com/files.system/linux/%{name}-%{version}-i386-Linux.tar.gz 
# NoSource0-md5: 7c4c1f042cfef63055de960933d7a19c
NoSource:	0
URL:		http://www.photodex.com/products/compupic/index.html
BuildRequires:	coreutils
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The fastest, easiest to use software for browsing and viewing pictures. 
CompuPic gives you unmatched performance paired with a full set of 
features for editing, sharing, and using your digital content

%description -l pl
Najszybsze i naj³atwiejsze w u¿yciu narzêdzie do przegl±dania i podgl±du
obrazków. 

%prep
%setup -q -n compupic-5.1.1063-i386-Linux
> install.sh

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/compupic,%{_pixmapsdir},%{_desktopdir}}

tar xf compupic.tar -C $RPM_BUILD_ROOT%{_datadir}/compupic
mv -f $RPM_BUILD_ROOT%{_datadir}/compupic/compupic.1 $RPM_BUILD_ROOT%{_mandir}/man1/
mv $RPM_BUILD_ROOT%{_datadir}/compupic/*.xpm	$RPM_BUILD_ROOT%{_pixmapsdir}/
mv $RPM_BUILD_ROOT%{_datadir}/compupic/LICENSE ./
mv $RPM_BUILD_ROOT%{_datadir}/compupic/README ./
cd $RPM_BUILD_ROOT%{_datadir}/compupic
ln compupic ../../bin/compupic
cd -

cat > $RPM_BUILD_ROOT%{_desktopdir}/compupic.desktop <<_EOF_
[Desktop Entry]
Encoding=UTF-8
Name=Compupic
Name[pl]=
Type=Application
Exec=compupic
GenericName=Picture browser
GenericName[pl]=Przegl±darka obrazów
_EOF_

iconv -f iso8859-2 -t utf8 $RPM_BUILD_ROOT%{_desktopdir}/compupic.desktop >> $RPM_BUILD_ROOT%{_desktopdir}/compupic.desktop.1
mv $RPM_BUILD_ROOT%{_desktopdir}/compupic.desktop{.1,}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE
%attr(755,root,root) %{_bindir}/compupic
%doc %{_datadir}/compupic/english
%doc %{_datadir}/compupic/web
%{_mandir}/man1/compupic*
%{_datadir}/compupic/compupic
%{_datadir}/compupic/cpicoeme.bmp
%{_datadir}/compupic/defscr
%{_datadir}/compupic/docscr
%{_datadir}/compupic/order.txt
%{_pixmapsdir}/cpicicon-*.xpm
%{_desktopdir}/compupic.desktop
