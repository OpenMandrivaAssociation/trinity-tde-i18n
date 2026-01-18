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
%{load %{S:1}}

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
%_trinity_lang_template af Afrikaans
%_trinity_lang_template ar Arabic
%_trinity_lang_template az Azerbaijani
%_trinity_lang_template be Belarusian
%_trinity_lang_template bg Bulgarian
%_trinity_lang_template bn Bengali
%_trinity_lang_template bo Tibetan
%_trinity_lang_template br Breton
%_trinity_lang_template bs Bosnian
%_trinity_lang_template ca Catalan
%_trinity_lang_template cs Czech
%_trinity_lang_template csb Kashubian
%_trinity_lang_template cy Welsh
%_trinity_lang_template da Danish
%_trinity_lang_template de German
%_trinity_lang_template el Greek
%_trinity_lang_template en_GB British
%_trinity_lang_template eo Esperanto
%_trinity_lang_template es Spanish
%_trinity_lang_template es_AR Spanish-Argentina
%_trinity_lang_template et Estonian
%_trinity_lang_template eu Basque
%_trinity_lang_template fa Farsi
%_trinity_lang_template fi Finnish
%_trinity_lang_template fo Faroese
%_trinity_lang_template fr French
%_trinity_lang_template fy Frisian
%_trinity_lang_template ga Irish
%_trinity_lang_template gl Galician
%_trinity_lang_template he Hebrew
%_trinity_lang_template hi Hindi
%_trinity_lang_template hr Croatian
%_trinity_lang_template hu Hungarian
%_trinity_lang_template id Indonesian
%_trinity_lang_template is Icelandic
%_trinity_lang_template it Italian
%_trinity_lang_template ja Japanese
%_trinity_lang_template kk Kazakh
%_trinity_lang_template km Khmer
%_trinity_lang_template ko Korean
%_trinity_lang_template ku Kurdish
%_trinity_lang_template lo Lao
%_trinity_lang_template lt Lithuanian
%_trinity_lang_template lv Latvian
%_trinity_lang_template mi Maori
%_trinity_lang_template mk Macedonian
%_trinity_lang_template mn Mongolian
%_trinity_lang_template ms Malay
%_trinity_lang_template mt Maltese
%_trinity_lang_template nb Norwegian-Bokmål
%_trinity_lang_template nds Low-Saxon
%_trinity_lang_template nl Dutch
%_trinity_lang_template nn Norwegian-Nynorsk
%_trinity_lang_template no Norwegian
%_trinity_lang_template oc Occitan
%_trinity_lang_template pa Punjabi
%_trinity_lang_template pl Polish
%_trinity_lang_template pt Portuguese
%_trinity_lang_template pt_BR Brazil
%_trinity_lang_template ro Romanian
%_trinity_lang_template ru Russian
%_trinity_lang_template rw Kinyarwanda
%_trinity_lang_template se Northern-Sami
%_trinity_lang_template sk Slovak
%_trinity_lang_template sl Slovenian
%_trinity_lang_template sr Serbian
%_trinity_lang_template_alt sr@Latn Serbian-Latin sr-Latn
%_trinity_lang_template ss South-Sudan
%_trinity_lang_template sv Swedish
%_trinity_lang_template ta Tamil
%_trinity_lang_template te Telugu
%_trinity_lang_template tg Tajik
%_trinity_lang_template th Thai
%_trinity_lang_template tr Turkish
%_trinity_lang_template uk Ukrainian
%_trinity_lang_template uz Uzbek
%_trinity_lang_template_alt uz@cyrillic Uzbek-Cyrillic uz-Cyrl
%_trinity_lang_template ven Venda
%_trinity_lang_template vi Vietnamese
%_trinity_lang_template wa Walloon
%_trinity_lang_template xh Xhosa
%_trinity_lang_template zh_CN Chinese
%_trinity_lang_template zh_TW Chinese-Big5

##########

%prep
%autosetup -n %{tde_pkg}-trinity-%{version} -p1
%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"

%install -a
# remove zero-length file
find "%{buildroot}%{tde_prefix}/share/doc/tde/HTML" -size 0 -exec rm -f {} \;

# remove obsolete KDE 3 application data translations
%__rm -rf "%{buildroot}%{tde_prefix}/share/apps"
