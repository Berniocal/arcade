# Arcade

Český rozcestník tří klasických her pro telefon i počítač.

| Hra | Soubor | Hráči |
| --- | --- | --- |
| Vlak | `vlak.html` | Jeden hráč, 50 původních scén |
| Pac-Man | `pacman.html` | Jeden hráč |
| Arcade Volleyball | `volejbal.html` | Dva na jednom telefonu nebo proti PC, 3 obtížnosti |

Otevřete `index.html`. Hry se spouštějí ve stejné stránce a tlačítko „Všechny hry“ vrací rozcestník. Klepnutím na hodiny lze u každé hry napsat vlastní rychlost (čárka i tečka): Vlak 0,03–5 s na políčko, Pac-Man a míč ve volejbalu 0,1–3×. Hodnota se pamatuje v prohlížeči. Lze je otevřít také samostatně a stáhnout jako soběstačné HTML soubory. Fungují dotyková tlačítka, joystick i klávesnice. Volejbal: v ikoně soupeřů vyberte Kamarád / Počítač a lehkou, střední nebo těžkou obtížnost.

## GitHub Pages

Statický web bez sestavení. Pro publikaci zvolte v Settings → Pages → Deploy from a branch → `main` / `(root)`. Používají se relativní cesty, takže web funguje v podadresáři `/arcade/`. Žádná instalace balíčků není potřeba.

## Zdroje a licence

Vlak: původní autor Miroslav Němeček, grafika a mapy ze zveřejněných zdrojů Vlak / PicoPad. Autor dovoluje použití svých softwarových výtvorů pod Unlicense: https://www.breatharian.eu/sw/vlak/index.html a https://www.breatharian.eu/Panda38/index.html . Upravitelný kód, mapy a prostředky webové verze jsou obsažené přímo v HTML.

Pac-Man: samostatná předělávka Shauna Williamse, Masona Bordy a přispěvatelů, https://github.com/masonicGIT/pacman, GNU GPL v3. Hra není bitově přesná emulace ROM. Původní značka a hra patří Namco / Bandai Namco.

Volejbal: původní hra Rhett Anderson, Randy Thompson a COMPUTE! Publications; JavaScript port Iakov Davydov a albertonellifun, https://github.com/albertonellifun/arcade-volleyball, GNU GPL v3. CGA prostředky přes https://github.com/SzJoakim93/ArcadeVolleyBallJS . Těžká obtížnost vychází z původního CPU, lehčí obtížnosti přidávají prodlevu a nepřesnost, fyzika zůstává pro oba hráče stejná.

Pac-Man i volejbal mají v informacích úplnou licenci a ZIP kompletních preferovaných zdrojů včetně sestavení a testů. ZIP je vložený do HTML a dostupný i offline. Kopie GNU GPL v3 je v `LICENSE-GPL-3.0.txt`. Písmo uvnitř her Press Start 2P: Cody Boisclair, SIL OFL 1.1; licence je přímo ve hrách a zdrojových archivech.

Rozcestník a mobilní úpravy 2026. Jednotlivé hry si ponechávají vlastní licence a autorské údaje.
