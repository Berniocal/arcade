# Arcade

Český rozcestník pěti klasických her pro telefon i počítač.

| Hra | Soubor | Hráči |
| --- | --- | --- |
| Vlak | `vlak.html` | Jeden hráč, 50 původních scén |
| Pac-Man | `pacman.html` | Jeden hráč |
| Arcade Volleyball | `volejbal.html` | Dva na jednom telefonu nebo proti PC, 3 obtížnosti |
| Supaplex | `supaplex.html` | Jeden hráč, 111 původních úrovní |
| Epic Pinball | `pinball.html` | Jeden hráč, původní DOSový sharewarový stůl Super Android |

Otevřete `index.html`. Hry se spouštějí ve stejné stránce a tlačítko „Všechny hry“ vrací rozcestník. Klepnutím na hodiny lze u každé hry napsat vlastní rychlost (čárka i tečka): Vlak 0,03–5 s na políčko, Pac-Man, Supaplex, pinball a míč ve volejbalu 0,1–3×. Hodnota se pamatuje v prohlížeči. Lze je otevřít také samostatně a stáhnout jako soběstačné HTML soubory. Fungují dotyková tlačítka, joystick i klávesnice. Volejbal: v ikoně soupeřů vyberte Kamarád / Počítač a lehkou, střední nebo těžkou obtížnost.

Pinball: levý / pravý Shift nebo šipky vlevo / vpravo ovládají pálky, mezerník pružinu, P pauzu. Dotykové pálky fungují současně; pružinu podržte a pusťte. Ikona ruky přepíná tlačítka a dotyk levé / pravé poloviny hrací plochy. Spuštění připraví původní zvukovou konfiguraci a automaticky projde menu (obvykle kolem 15 sekund). Původní menu je dál dostupné přes ikonu ☰ včetně šipek, Enter, Esc, Y/N a zadání iniciál. Celá obrazovka zvětší herní plochu, ostatní ikony zůstávají stranou.

## GitHub Pages

Statický web bez sestavení. Pro publikaci zvolte v Settings → Pages → Deploy from a branch → `main` / `(root)`. Používají se relativní cesty, takže web funguje v podadresáři `/arcade/`. Žádná instalace balíčků není potřeba.

## Zdroje a licence

Vlak: původní autor Miroslav Němeček, grafika a mapy ze zveřejněných zdrojů Vlak / PicoPad. Autor dovoluje použití svých softwarových výtvorů pod Unlicense: https://www.breatharian.eu/sw/vlak/index.html a https://www.breatharian.eu/Panda38/index.html . Upravitelný kód, mapy a prostředky webové verze jsou obsažené přímo v HTML.

Pac-Man: samostatná předělávka Shauna Williamse, Masona Bordy a přispěvatelů, https://github.com/masonicGIT/pacman, GNU GPL v3. Hra není bitově přesná emulace ROM. Původní značka a hra patří Namco / Bandai Namco.

Volejbal: původní hra Rhett Anderson, Randy Thompson a COMPUTE! Publications; JavaScript port Iakov Davydov a albertonellifun, https://github.com/albertonellifun/arcade-volleyball, GNU GPL v3. CGA prostředky přes https://github.com/SzJoakim93/ArcadeVolleyBallJS . Těžká obtížnost vychází z původního CPU, lehčí obtížnosti přidávají prodlevu a nepřesnost, fyzika zůstává pro oba hráče stejná.

Supaplex: engine OpenSupaplex Sergia Padrina a přispěvatelů, https://github.com/sergiou87/open-supaplex, GNU GPL v3 (commit 2ae9e5815c508c15e405892db486495d28f74f6d). Původní herní logika, grafika, zvuky a 111 úrovní; mobilní ovládání, menu a časování přes webový adaptér. Původní autoři Supaplexu: Philip Jespersen, Michael Stopp, Robin Heydon, Matt Smith a David Whittaker. Původní prostředky z freeware distribuce přiložené k OpenSupaplexu patří původním autorům. Šipky / WASD, mezerník nebo dotykové akční tlačítko; joystick mění směr už po krátkém posunu prstu. Po puštění ovládání se Murphy zastaví. Původní tempo 35 simulačních kroků za sekundu.

Pac-Man, volejbal i Supaplex mají v informacích úplnou licenci a ZIP kompletních preferovaných zdrojů včetně sestavení a testů. ZIP je vložený do HTML a dostupný i offline. Kopie GNU GPL v3 je v `LICENSE-GPL-3.0.txt`. Písmo uvnitř her Press Start 2P: Cody Boisclair, SIL OFL 1.1; licence je přímo ve hrách a zdrojových archivech.

Epic Pinball: původní Epic MegaGames, Inc., sharewarová verze 2.1, jeden hratelný stůl Super Android. Jde o původní DOSový program v emulátoru, s původní grafikou a fyzikou. Shareware znamená „vyzkoušej před koupí“, nikoli freeware. Kompletní nezměněný 56souborový sharewarový balíček `epicpn21.zip` z https://www.classicdosgames.com/files/games/epic/epicpn21.zip je vložený do HTML a lze jej stáhnout z informací spolu s původní licencí. Původní program ani prostředky se nemění; zvuk nastavuje původní SETUP.EXE při spuštění.

Emulátor pinballu: DOSBox / js-dos 6.22.31, GNU GPL v2, distribuce npm `js-dos@6.22.31`. Úplné odpovídající zdroje z https://github.com/Emupedia/emupedia-library-js-dos (commit 8a05150d685aba42a8520c1134fafd276009fc97), původní licence, upravitelný mobilní adaptér, sestavení a testy jsou v offline ZIPu uvnitř HTML, dostupném v informacích. Zdrojový archiv umožňuje znovu sestavit totožný HTML soubor pomocí Pythonu 3.

Rozcestník a mobilní úpravy 2026. Jednotlivé hry si ponechávají vlastní licence a autorské údaje.
