Name: firefox
Version: 24.0	
Release:	2%{?dist}
Summary: Mozilla Firefox Web Browser	
Group: Applications/Internet
License: MPLv1.1 or GPLv2+ or LGPLv2+
URL: http://www.mozilla.org/projects/firefox/
Source0: http://download.cdn.mozilla.net/pub/mozilla.org/firefox/releases/latest/linux-x86_64/en-GB/firefox-%{version}.tar.bz2

%description
Mozilla Firefox is an open-source web browser, designed for standards compliance, performance and portability

%prep
%setup -q -n firefox


%build


%install
install -m 755 -d %{buildroot}/opt/firefox
cp -r * %{buildroot}/opt/firefox/
install -m 755 -d %{buildroot}/%{_bindir}
ln -s /opt/firefox/firefox %{buildroot}/%{_bindir}/firefox
mkdir -p %{buildroot}/usr/share/applications
cat << EOF > %{buildroot}/usr/share/applications/mozilla-firefox.desktop
[Desktop Entry]
Version=%{version}
Encoding=UTF-8
Name=Firefox Web Browser
Name[ca]=Navegador web Firefox
Name[cs]=Firefox Webový prohlížeč
Name[es]=Navegador web Firefox
Name[fa]=مرورگر اینترنتی Firefox
Name[fi]=Firefox-selain
Name[fr]=Navigateur Web Firefox
Name[hu]=Firefox webböngésző
Name[it]=Firefox Browser Web
Name[ja]=Firefox ウェブ・ブラウザ
Name[ko]=Firefox 웹 브라우저
Name[nb]=Firefox Nettleser
Name[nl]=Firefox webbrowser
Name[nn]=Firefox Nettlesar
Name[no]=Firefox Nettleser
Name[pl]=Przeglądarka WWW Firefox
Name[pt]=Firefox Navegador Web
Name[pt_BR]=Navegador Web Firefox
Name[sk]=Internetový prehliadač Firefox
Name[sv]=Webbläsaren Firefox
GenericName=Web Browser
GenericName[ca]=Navegador web
GenericName[cs]=Webový prohlížeč
GenericName[es]=Navegador web
GenericName[fa]=مرورگر اینترنتی
GenericName[fi]=WWW-selain
GenericName[fr]=Navigateur Web
GenericName[hu]=Webböngésző
GenericName[it]=Browser Web
GenericName[ja]=ウェブ・ブラウザ
GenericName[ko]=웹 브라우저
GenericName[nb]=Nettleser
GenericName[nl]=Webbrowser
GenericName[nn]=Nettlesar
GenericName[no]=Nettleser
GenericName[pl]=Przeglądarka WWW
GenericName[pt]=Navegador Web
GenericName[pt_BR]=Navegador Web
GenericName[sk]=Internetový prehliadač
GenericName[sv]=Webbläsare
Comment=Browse the Web
Comment[ca]=Navegueu per el web
Comment[cs]=Prohlížení stránek World Wide Webu
Comment[de]=Im Internet surfen
Comment[es]=Navegue por la web
Comment[fa]=صفحات شبکه جهانی اینترنت را مرور نمایید
Comment[fi]=Selaa Internetin WWW-sivuja
Comment[fr]=Navigue sur Internet
Comment[hu]=A világháló böngészése
Comment[it]=Esplora il web
Comment[ja]=ウェブを閲覧します
Comment[ko]=웹을 돌아 다닙니다
Comment[nb]=Surf på nettet
Comment[nl]=Verken het internet
Comment[nn]=Surf på nettet
Comment[no]=Surf på nettet
Comment[pl]=Przeglądanie stron WWW 
Comment[pt]=Navegue na Internet
Comment[pt_BR]=Navegue na Internet
Comment[sk]=Prehliadanie internetu
Comment[sv]=Surfa på webben
Exec=firefox %u
Icon=/opt/firefox/browser/chrome/icons/default/default48.png
Terminal=false
Type=Application
StartupWMClass=Firefox-bin
MimeType=text/html;text/xml;application/xhtml+xml;application/vnd.mozilla.xul+xml;text/mml;
StartupNotify=true
X-Desktop-File-Install-Version=0.15
Categories=Network;WebBrowser;
EOF


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{_bindir}/*
/opt/firefox/*
/usr/share/applications/mozilla-firefox.desktop


%changelog

