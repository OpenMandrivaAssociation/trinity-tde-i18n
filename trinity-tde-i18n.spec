%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2
%define tde_pkg tde-i18n
%define tde_prefix /opt/trinity
%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1
%define tarball_name %{tde_pkg}-trinity

Name:           trinity-%{tde_pkg}
Version:        %{tde_version}
Release:        %{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:        Internationalization support for Trinity
Group:          User Interface/Desktops
URL:            http://www.trinitydesktop.org/
License:        GPLv2+
BuildArch:      noarch

# Speed build options
%define debug_package %{nil}
%define __spec_install_post %{nil}
AutoReq: no
Source0:        https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz
Source1:	trinity_lang.macro
# NOTE This load's the template macro definitions
# NOTE which includes the _trinity_lang_template* macros use in this spec file
# NOTE do not delete this line, else everything using these defines will break.
%{load:%{S:1}}

BuildSystem:    cmake
BuildOption:    -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DPKGCONFIG_INSTALL_DIR=%{tde_prefix}/%{_lib}/pkgconfig
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DBUILD_DOC=ON
BuildOption:    -DBUILD_DATA=ON
BuildOption:    -DBUILD_MESSAGES=ON

BuildRequires:  trinity-tdelibs-devel >= %{tde_version}
BuildRequires:  findutils
BuildRequires:  gettext
BuildRequires:  trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:    gcc-c++}

%description
This package contains %{summary}.
# NOTE In order to generate these, check and run the create_language_templates.sh
# NOTE script which generates the trinity_lang_template.in file.
# NOTE If any entries have @ symbols, check its ISO 639 language code and
# NOTE insert the ISO-639 languiage code as a third entry in-
# NOTE create_language_templates.sh, replacing those @ symbils with hyphens -
# NOTE then change the remplate type to %%_trinity_lang_template_alt which
# NOTE handles 3 parameter values, then copy and paste the contents of-
# NOTE trinity_lang_template.in and paste here to overwrite the below.
# NOTE This creates %%package entries for all languages provided.
%_trinity_lang_template Afrikaans af
%_trinity_lang_template Arabic ar
%_trinity_lang_template Azerbaijani az
%_trinity_lang_template Belarusian be
%_trinity_lang_template Bulgarian bg
%_trinity_lang_template Bengali bn
%_trinity_lang_template Tibetan bo
%_trinity_lang_template Breton br
%_trinity_lang_template Bosnian bs
%_trinity_lang_template Catalan ca
%_trinity_lang_template Czech cs
%_trinity_lang_template Kashubian csb
%_trinity_lang_template Welsh cy
%_trinity_lang_template Danish da
%_trinity_lang_template German de
%_trinity_lang_template Greek el
%_trinity_lang_template British en_GB
%_trinity_lang_template Esperanto eo
%_trinity_lang_template Spanish es
%_trinity_lang_template Spanish-Argentina es_AR
%_trinity_lang_template Estonian et
%_trinity_lang_template Basque eu
%_trinity_lang_template Farsi fa
%_trinity_lang_template Finnish fi
%_trinity_lang_template Faroese fo
%_trinity_lang_template French fr
%_trinity_lang_template Frisian fy
%_trinity_lang_template Irish ga
%_trinity_lang_template Galician gl
%_trinity_lang_template Hebrew he
%_trinity_lang_template Hindi hi
%_trinity_lang_template Croatian hr
%_trinity_lang_template Hungarian hu
%_trinity_lang_template Indonesian id
%_trinity_lang_template Icelandic is
%_trinity_lang_template Italian it
%_trinity_lang_template Japanese ja
%_trinity_lang_template Kazakh kk
%_trinity_lang_template Khmer km
%_trinity_lang_template Korean ko
%_trinity_lang_template Kurdish ku
%_trinity_lang_template Lao lo
%_trinity_lang_template Lithuanian lt
%_trinity_lang_template Latvian lv
%_trinity_lang_template Maori mi
%_trinity_lang_template Macedonian mk
%_trinity_lang_template Mongolian mn
%_trinity_lang_template Malay ms
%_trinity_lang_template Maltese mt
%_trinity_lang_template Norwegian-Bokmal nb
%_trinity_lang_template Low-Saxon nds
%_trinity_lang_template Dutch nl
%_trinity_lang_template Norwegian-Nynorsk nn
%_trinity_lang_template Norwegian no
%_trinity_lang_template Occitan oc
%_trinity_lang_template Punjabi pa
%_trinity_lang_template Polish pl
%_trinity_lang_template Portuguese pt
%_trinity_lang_template Brazil pt_BR
%_trinity_lang_template Romanian ro
%_trinity_lang_template Russian ru
%_trinity_lang_template Kinyarwanda rw
%_trinity_lang_template Northern-Sami se
%_trinity_lang_template Slovak sk
%_trinity_lang_template Slovenian sl
%_trinity_lang_template Serbian sr
%_trinity_lang_template_alt Serbian-Latin sr@Latn sr-Latn
%_trinity_lang_template South-Sudan ss
%_trinity_lang_template Swedish sv
%_trinity_lang_template Tamil ta
%_trinity_lang_template Telugu te
%_trinity_lang_template Tajik tg
%_trinity_lang_template Thai th
%_trinity_lang_template Turkish tr
%_trinity_lang_template Ukrainian uk
%_trinity_lang_template Uzbek uz
%_trinity_lang_template_alt Uzbek-Cyrillic uz@cyrillic uz-Cyrl
%_trinity_lang_template Venda ven
%_trinity_lang_template Vietnamese vi
%_trinity_lang_template Walloon wa
%_trinity_lang_template Xhosa xh
%_trinity_lang_template Chinese zh_CN
%_trinity_lang_template Chinese-Big5 zh_TW

##########
%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"

%install -a
# remove zero-length file
find "%{buildroot}%{tde_prefix}/share/doc/tde/HTML" -size 0 -exec rm -f {} \;

# remove obsolete KDE 3 application data translations
%__rm -rf "%{buildroot}%{tde_prefix}/share/apps"
