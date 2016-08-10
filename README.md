# daCwa_project

Data for exploring the Ismāʿīlī daʿwaŧ 

## Structure:

1. Profiles: biographical reports on people
	1. Files should have URIs as their names.
	2. Run betaCode script to transliterate and convert into Arabic


## Bio record structure

```

URI: 0597IbnJawzi

SHUHRA: Ibn al-Ǧawzī [[ابن الجوزي]]
ISM: ʿAbd al-Raḥmãn [[عبد الرحمن]]
NASAB1: ibn Fulān [[ابن فلان]]
NASAB2:
LAQAB: Abū al-Faraǧ [[ابو الفرج]], Ǧamāl al-Dīn [[جمال الدين]]
NISBA: al-Baġdādī [[البغدادي]], al-Wāʿiẓ [[الواعظ]], al-Ḥanbalī [[الحنبلي]]
KUNYA: Abū Ḳāsim [[ابو قاسم]] 

BORN: 510AH
DIED: 597AH

BIO: Free running narrative... 

```

## BetaCode Note

Explanations and scheme (http://maximromanov.github.io/2015/02-07.html)[http://maximromanov.github.io/2015/02-07.html]

Things that should be transliterated and converted into Arabic must be types between `@@ and @@`, for example @@Ibn al-Jawz_i@@, which after conversion will become `Ibn al-Ǧawzī [[ابن الجوزي]]`.
