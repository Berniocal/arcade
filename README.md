# Arcade

Český rozcestník šesti her pro telefon i počítač – čtyři retro klasiky, vlastní fantasy adventura a původní freeware Lure of the Temptress (1992).

| Hra | Soubor | Hráči |
| --- | --- | --- |
| Vlak | `vlak.html` | Jeden hráč, 50 původních scén |
| Pac-Man | `pacman.html` | Jeden hráč |
| Arcade Volleyball | `volejbal.html` | Dva na jednom telefonu nebo proti PC, 3 obtížnosti |
| Supaplex | `supaplex.html` | Jeden hráč, 111 původních úrovní |
| Legenda o Jantarovém lese | `jantarovy-les.html` | Jeden hráč, česká point-and-click adventura se 7 lokacemi |
| Lure of the Temptress (1992) | `lure.html`, `lure.jsdos` | Jeden hráč, původní kompletní anglická fantasy adventura, freeware |

Otevřete `index.html`. Hry se spouštějí ve stejné stránce a tlačítko „Všechny hry“ vrací rozcestník. Klepnutím na hodiny lze u čtyř akčních her napsat vlastní rychlost (čárka i tečka): Vlak 0,03–5 s na políčko, Pac-Man, Supaplex a míč ve volejbalu 0,1–3×. Hodnota se pamatuje v prohlížeči. Čtyři původní arkády a Jantarový les lze otevřít samostatně a stáhnout jako soběstačné HTML soubory. Původní Lure vyžaduje vedle HTML také herní archiv `lure.jsdos` a webové jádro emulátoru js-dos. Čtyři akční hry používají dotyková tlačítka, joystick i klávesnici. Jantarový les používá ťukání na místa ve scéně nebo velká tlačítka s dostupnými akcemi pod obrazem; pro výběr předmětu slouží inventář. Ukládá se automaticky do prohlížeče a je hratelný offline bez cizích knihoven. Volejbal: v ikoně soupeřů vyberte Kamarád / Počítač a lehkou, střední nebo těžkou obtížnost.

## GitHub Pages

Statický web bez sestavení. Pro publikaci zvolte v Settings → Pages → Deploy from a branch → `main` / `(root)`. Používají se relativní cesty, takže web funguje v podadresáři `/arcade/`. Žádná instalace balíčků není potřeba.

## Zdroje a licence

Vlak: původní autor Miroslav Němeček, grafika a mapy ze zveřejněných zdrojů Vlak / PicoPad. Autor dovoluje použití svých softwarových výtvorů pod Unlicense: https://www.breatharian.eu/sw/vlak/index.html a https://www.breatharian.eu/Panda38/index.html . Upravitelný kód, mapy a prostředky webové verze jsou obsažené přímo v HTML.

Pac-Man: samostatná předělávka Shauna Williamse, Masona Bordy a přispěvatelů, https://github.com/masonicGIT/pacman, GNU GPL v3. Hra není bitově přesná emulace ROM. Původní značka a hra patří Namco / Bandai Namco.

Volejbal: původní hra Rhett Anderson, Randy Thompson a COMPUTE! Publications; JavaScript port Iakov Davydov a albertonellifun, https://github.com/albertonellifun/arcade-volleyball, GNU GPL v3. CGA prostředky přes https://github.com/SzJoakim93/ArcadeVolleyBallJS . Těžká obtížnost vychází z původního CPU, lehčí obtížnosti přidávají prodlevu a nepřesnost, fyzika zůstává pro oba hráče stejná.

Supaplex: engine OpenSupaplex Sergia Padrina a přispěvatelů, https://github.com/sergiou87/open-supaplex, GNU GPL v3 (commit 2ae9e5815c508c15e405892db486495d28f74f6d). Původní herní logika, grafika, zvuky a 111 úrovní; mobilní ovládání, menu a časování přes webový adaptér. Původní autoři Supaplexu: Philip Jespersen, Michael Stopp, Robin Heydon, Matt Smith a David Whittaker. Původní prostředky z freeware distribuce přiložené k OpenSupaplexu patří původním autorům. Šipky / WASD, mezerník nebo dotykové akční tlačítko; joystick mění směr už po krátkém posunu prstu. Po puštění ovládání se Murphy zastaví. Původní tempo 35 simulačních kroků za sekundu.

Pac-Man, volejbal i Supaplex mají v informacích úplnou licenci a ZIP kompletních preferovaných zdrojů včetně sestavení a testů. ZIP je vložený do HTML a dostupný i offline. Kopie GNU GPL v3 je v `LICENSE-GPL-3.0.txt`. Písmo uvnitř her Press Start 2P: Cody Boisclair, SIL OFL 1.1; licence je přímo ve hrách a zdrojových archivech.

Rozcestník a mobilní úpravy 2026. Jednotlivé hry si ponechávají vlastní licence a autorské údaje.

## Legenda o Jantarovém lese

Originální krátká česká fantasy point-and-click adventura vytvořená přímo pro tento web; je inspirovaná atmosférou her typu *The Legend of Kyrandia*, ale nepoužívá její původní grafiku, zvuky, dialogy, příběh ani herní data. Je to **pocta žánru, nikoliv port původní hry Kyrandia**. Sedm propojených scén: nádvoří, háj, potok, ruiny, jeskyně, zahrada a svatyně. Hráč sbírá předměty, řeší hádanky, používá inventář, může zvýraznit aktivní místa, zapnout zvuky a využít celoobrazovkový režim. Funguje na dotykovém telefonu v orientaci na výšku i na šířku, na počítači také myší. Celá hra je obsažená v jediném souboru `jantarovy-les.html` a nepotřebuje síťové spojení. Autorská textová a kreslená podoba, bez externích herních assetů.

## Lure of the Temptress (původní hra z roku 1992)

- **Hra je původní**, ne grafická napodobenina. Vývojář Revolution Software ji uvolnil pod vlastní freeware licencí; © Revolution Software Ltd. [Oficiální ScummVM archiv](https://www.scummvm.org/games/) je zdroj verze 1.1 (English). Původní soubory se nepozměňují, pouze se zabalí do js-dos ZIP bundlu. Licence a informace o původu jsou uvnitř `lure.jsdos` (LURE-LICENSE.txt, ORIGINAL-SOURCE.txt).
- **Webové přehrávání:** `lure.html` spouští originální DOS verzi přes [js-dos](https://js-dos.com/) v8 (emulace DOSBox); JavaScript a WebAssembly engine se stahují z oficiálního CDN js-dos, proto tato hra na rozdíl od jiných není plně offline ani jednoborový HTML.
- **Telefon:** dotykové zaměření kurzoru a klik, pravý klik dlouhým podržením nebo tlačítkem režimu, mezerník, Enter, Escape, fullscreen. Na desktopu funguje běžná myš. Původní menu ve hře umožňuje Save/Restore; tlačítko „Uložit stav“ zajišťuje perzistenci herních souborů ve stejném prohlížeči, není to náhrada uložení v menu hry.
- **Vytvoření herního balíčku:** `tools/build-lure.py` stáhne originál z oficiálního archivu a ověří SHA-256 `f3178245a1483da1168c3a11e70b65d33c389f1f5df63d4f3a356886c1890108`. Workflow `.github/workflows/build-lure.yml` ho sestaví a publikuje. Nezasahuje do pravidel a herního obsahu. Nevytváří český překlad; hra zůstává v angličtině.
- Pokud originální hra po prvním startu požádá o ochranný kód, z horního herního menu vyber **Restart**, jak doporučují průvodci freeware verzí. Odlišnou verzi či nastavení ověř samostatně.

**Licence:** Lure je freeware s povolením bezplatné distribuce za zachování licence a oznámení; samotný js-dos/DOSBox software má odlišné otevřené licence. Tento projekt není přidružen k Revolution Software, ScummVM ani js-dos.
