Summary:	Tamil TTF fonts (Unicode encoded)
Name:		fonts-ttf-tamil
Version:	1.1
Release:	14
License:	Free
Group:		System/Fonts/True type
Url:		http://www.tamil.net/tscii/tools.html#fonts
# from http://groups.yahoo.com/group/tamilinix/files/
# the suitability for free distribution has been checked by
# Thuraiappah Vaseeharan <t_vasee@yahoo.com>
Source0:	tsc-avarangal.tar.bz2
Source1:	tscii-bitmap.tar.bz2
Source2:	tamil_opentype_fonts.tar.bz2
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	freetype-tools

%description
Tamil TTF fonts usable to display Unicode encoded text; through text
engines like pango etc.

%package -n fonts-ttf-tscii
Url:		http://www.geocities.com/avarangal/
Summary:	Tamil TTF fonts (TSCII encoded)
Group:		System/Fonts/True type	

%description -n fonts-ttf-tscii
Tamil TTF fonts in TSCII encoding.
Those fonts present themselves as covering western (cp1252) character set,
which is wrong, but currently the only way to make Tamil TSCII work.

%package -n fonts-bitmap-tscii
Summary:	Tamil Bitmap fonts
Group:		System/Fonts/X11 bitmap
License:	GPLv2

%description -n fonts-bitmap-tscii
Tamil bitmap fonts for X11 in TSCII encoding 


%prep

%setup -q -T -c -a0 -a1 -a2
 
%build

cp tsc-avarangal/README README.avarangal
cp tamil_opentype_fonts/README README.TSCu

%install
install -d %{buildroot}/%{_datadir}/fonts/TTF/tamil/
install -m 0644 tamil_opentype_fonts/*.ttf %{buildroot}/%{_datadir}/fonts/TTF/tamil
install -d %{buildroot}/%{_datadir}/fonts/TTF/tscii/
install -m 0644 tsc-avarangal/*.ttf %{buildroot}/%{_datadir}/fonts/TTF/tscii
install -d %{buildroot}/%{_datadir}/fonts/bitmap/tscii/
install -m 0644 tscii-bitmap/*.gz %{buildroot}/%{_datadir}/fonts/bitmap/tscii
install -m 0644 tscii-bitmap/fonts.dir %{buildroot}/%{_datadir}/fonts/bitmap/tscii

(
cd %{buildroot}/%{_datadir}/fonts/TTF/tscii
# ttmkfdir can't be used as we need special names
cat << EOF > fonts.scale
15
tscavai.TTF -misc-TSC_Avarangal-medium-i-normal--0-0-0-0-p-0-tscii-0
tscavai.TTF -misc-TSC_Avarangal-medium-i-normal--0-0-0-0-p-0-iso8859-1
tscavai.TTF -misc-TSC_Avarangal-medium-i-normal--0-0-0-0-p-0-iso10646-1
tscavaf.TTF -misc-TSC_AvarangalFxd-medium-r-normal--0-0-0-0-m-0-tscii-0
tscavaf.TTF -misc-TSC_AvarangalFxd-medium-r-normal--0-0-0-0-m-0-iso8859-1
tscavaf.TTF -misc-TSC_AvarangalFxd-medium-r-normal--0-0-0-0-m-0-iso10646-1
tscavabi.TTF -misc-TSC_Avarangal-bold-i-normal--0-0-0-0-p-0-tscii-0
tscavabi.TTF -misc-TSC_Avarangal-bold-i-normal--0-0-0-0-p-0-iso8859-1
tscavabi.TTF -misc-TSC_Avarangal-bold-i-normal--0-0-0-0-p-0-iso10646-1
tscavab.TTF -misc-TSC_Avarangal-bold-r-normal--0-0-0-0-p-0-tscii-0
tscavab.TTF -misc-TSC_Avarangal-bold-r-normal--0-0-0-0-p-0-iso8859-1
tscavab.TTF -misc-TSC_Avarangal-bold-r-normal--0-0-0-0-p-0-iso10646-1
tscava.TTF -misc-TSC_Avarangal-medium-r-normal--0-0-0-0-p-0-tscii-0
tscava.TTF -misc-TSC_Avarangal-medium-r-normal--0-0-0-0-p-0-iso8859-1
tscava.TTF -misc-TSC_Avarangal-medium-r-normal--0-0-0-0-p-0-iso10646-1
EOF
cp fonts.scale fonts.dir
) 

(
cd %{buildroot}/%{_datadir}/fonts/bitmap/tscii
# just to be sure that an mkfontdir won't rewrite it
cp fonts.dir fonts.scale
)

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
for dir in tamil tscii; do
	ln -s ../../..%{_datadir}/fonts/TTF/$dir \
		%{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-$dir:pri=50
done
ln -s ../../..%{_datadir}/fonts/bitmap/tscii \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/bitmap-tscii:pri=50


%files
%doc tamil_opentype_fonts/README
%dir %{_datadir}/fonts/TTF/tamil/
%{_datadir}/fonts/TTF/tamil/*.ttf
%{_sysconfdir}/X11/fontpath.d/ttf-tamil:pri=50

%files -n fonts-ttf-tscii 
%doc README.avarangal
%dir %{_datadir}/fonts/TTF/tscii/
%{_datadir}/fonts/TTF/tscii/*.ttf
%config(noreplace) %{_datadir}/fonts/TTF/tscii/fonts.dir
%config(noreplace) %{_datadir}/fonts/TTF/tscii/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-tscii:pri=50

%files -n fonts-bitmap-tscii
%doc tscii-bitmap/README
%dir %{_datadir}/fonts/bitmap/
%dir %{_datadir}/fonts/bitmap/tscii/
%{_datadir}/fonts/bitmap/tscii/*.gz
%config(noreplace) %{_datadir}/fonts/bitmap/tscii/fonts.dir
%config(noreplace) %{_datadir}/fonts/bitmap/tscii/fonts.scale
%{_sysconfdir}/X11/fontpath.d/bitmap-tscii:pri=50

