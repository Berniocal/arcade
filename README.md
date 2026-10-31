# Arcade

Český rozcestník šesti klasických her pro telefon i počítač.

| Hra | Soubor | Hráči |
| --- | --- | --- |
| Vlak | `vlak.html` | Jeden hráč, 50 původních scén |
| Pac-Man | `pacman.html` | Jeden hráč |
| Arcade Volleyball | `volejbal.html` | Dva na jednom telefonu nebo proti PC, 3 obtížnosti |
| Supaplex | `supaplex.html` | Jeden hráč, 111 původních úrovní |
| Epic Pinball | `pinball.html` | Jeden hráč, původní DOSový sharewarový stůl Super Android |
| C-Dogs SDL | `cdogs.html`, `cdogs-runtime/` | Jeden hráč, originální akční hra v prohlížeči s kampaněmi Ogre a BEM |

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

## C-Dogs SDL (originální open-source hra)

C-Dogs SDL 2.5.0 od Cong Xu a přispěvatelů, navazuje na původní DOSovou hru od Ronnyho Westera. Hratelnost, původní dvě kampaně Ogre a BEM, grafika a engine pochází z originálu, **nejde o napodobeninu**. Webový port používá oficiální upstream zdrojový kód tagu [2.5.0](https://github.com/cxong/cdogs-sdl/tree/2.5.0) sestavený pomocí Emscripten 3.1.72. Nástrojové kompatibilitní opravy se zdrojovým kódem jsou přesně uvedeny v [sestavovacím workflow](.github/workflows/cdogs-mobile-build.yml) (chybějící `emscripten.h`, oprava deklarace `waderrno` a export souborového systému). Originální program ani herní mechaniky se nemění.

Omezení herních dat: z balíku byly záměrně vynechány komunitní kampaně s nejasným původem a modové podklady pro další hry (např. Wolfenstein / Noah’s Ark). Zůstaly dvě původní kampaně původního autora, **Ogre** a **BEM**. Většina herních grafických a zvukových souborů obsahuje vlastní licenční či zdrojové poznámky přibalené ve výsledném `index.data`.

**Licence a uvedení autorů:** Engine GPL-2.0 s částmi BSD / LGPL; původní grafika a kampaně byly autorem Ronny Westerem zveřejněny pod CC BY (2016); další data CC0 / CC BY / CC BY-SA podle souborů. Dokumenty [COPYING](https://github.com/cxong/cdogs-sdl/blob/2.5.0/COPYING) a [README_DATA](https://github.com/cxong/cdogs-sdl/blob/2.5.0/doc/README_DATA.md) jsou součástí sestavení, stejně jako úplný veřejný zdroj odpovídající binárnímu souboru (upstream + výše uvedené kroky). Mobilní obal v `cdogs.html` je publikován pod GPL-2.0.

**Mobil:** ve vodorovném režimu jsou směrové šipky vlevo, střelba X, zbraň Z, granát S a mapa A vpravo. Podržení více tlačítek najednou funguje. Enter potvrzuje, Esc přeruší hru, fullscreen maximalizuje obraz. Hra používá WebAssembly engine, nikoli pomalý DOS emulátor. Uložení konfigurace, rekordů a postupu kampaně se provádí ve webovém úložišti IndexedDB a tlačítkem 💾, ale neumožňuje uložení uprostřed mise. Načtení originálních dat potřebuje síť; následné obnovení postupu vyžaduje stejný prohlížeč.

**Ověření:** build je povolen k nasazení pouze po úspěšném kontrolním sestavení původního C-Dogs SDL, kontrole typu Wasm, testu skutečného vykreslení v Chromiu, simulovaném dotyku a ověření uložení/obnovy. Viz `tests/cdogs_smoke.py` a workflow.
