# Arcade

Český rozcestník pěti her pro telefon i počítač – čtyři retro klasiky a vlastní fantasy adventura.

| Hra | Soubor | Hráči |
| --- | --- | --- |
| Vlak | `vlak.html` | Jeden hráč, 50 původních scén |
| Pac-Man | `pacman.html` | Jeden hráč |
| Arcade Volleyball | `volejbal.html` | Dva na jednom telefonu nebo proti PC, 3 obtížnosti |
| Supaplex | `supaplex.html` | Jeden hráč, 111 původních úrovní |
| Legenda o Jantarovém lese | `jantarovy-les.html` | Jeden hráč, česká point-and-click adventura se 7 lokacemi |

Otevřete `index.html`. Hry se spouštějí ve stejné stránce a tlačítko „Všechny hry“ vrací rozcestník. Klepnutím na hodiny lze u čtyř akčních her napsat vlastní rychlost (čárka i tečka): Vlak 0,03–5 s na políčko, Pac-Man, Supaplex a míč ve volejbalu 0,1–3×. Hodnota se pamatuje v prohlížeči. Lze je otevřít také samostatně a stáhnout jako soběstačné HTML soubory. Čtyři akční hry používají dotyková tlačítka, joystick i klávesnici. Jantarový les používá ťukání na místa ve scéně nebo velká tlačítka s dostupnými akcemi pod obrazem; pro výběr předmětu slouží inventář. Ukládá se automaticky do prohlížeče a je hratelný offline bez cizích knihoven. Volejbal: v ikoně soupeřů vyberte Kamarád / Počítač a lehkou, střední nebo těžkou obtížnost.

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
