# read the spec file documentation before you break things.
# this file generates trinity-lang-templare.in file
# which contains lines to be inserted in the spec file.
language=$(cat <<'EOF'
Afrikaans af
Arabic ar
Azerbaijani az
Belarusian be
Bulgarian bg
Bengali bn
Tibetan bo
Breton br
Bosnian bs
Catalan ca
Czech cs
Kashubian csb
Welsh cy
Danish da
German de
Greek el
British en_GB
Esperanto eo
Spanish es
Spanish-Argentina es_AR
Estonian et
Basque eu
Farsi fa
Finnish fi
Faroese fo
French fr
Frisian fy
Irish ga
Galician gl
Hebrew he
Hindi hi
Croatian hr
Hungarian hu
Indonesian id
Icelandic is
Italian it
Japanese ja
Kazakh kk
Khmer km
Korean ko
Kurdish ku
Lao lo
Lithuanian lt
Latvian lv
Maori mi
Macedonian mk
Mongolian mn
Malay ms
Maltese mt
Norwegian-Bokmål nb
Low-Saxon nds
Dutch nl
Norwegian-Nynorsk nn
Norwegian no
Occitan oc
Punjabi pa
Polish pl
Portuguese pt
Brazil pt_BR
Romanian ro
Russian ru
Kinyarwanda rw
Northern-Sami se
Slovak sk
Slovenian sl
Serbian sr
Serbian-Latin sr@Latn sr-Latn
South-Sudan ss
Swedish sv
Tamil ta
Telugu te
Tajik tg
Thai th
Turkish tr
Ukrainian uk
Uzbek uz
Uzbek-Cyrillic uz@cyrillic uz-Cyrl
Venda ven
Vietnamese vi
Walloon wa
Xhosa xh
Chinese zh_CN
Chinese-Big5 zh_TW
EOF
)

while IFS= read -r line;
do
LANG=$(echo $line | tr -s ' ' | cut -d " " -f1)
ABBR=$(echo $line | tr -s ' ' | cut -d " " -f2)
ALT=$(echo $line | tr -s ' ' | cut -d " " -f3)

if [[ -n $ALT ]]; then
echo %_trinity_lang_template_alt $ABBR $LANG $ALT >> trinity_lang_template.in;
else
echo %_trinity_lang_template $ABBR $LANG >> trinity_lang_template.in;
fi
sed -i '/^$/d' trinity_lang_template.in
done <<< "$language"

