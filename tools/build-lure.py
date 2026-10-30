#!/usr/bin/env python3
"""Build a js-dos bundle from the official Lure freeware package (preserve all files)."""
import hashlib,io,pathlib,urllib.request,zipfile
URL="https://downloads.scummvm.org/frs/extras/Lure%20of%20the%20Temptress/lure-1.1.zip"
SHA256="f3178245a1483da1168c3a11e70b65d33c389f1f5df63d4f3a356886c1890108"
req=urllib.request.Request(URL,headers={"User-Agent":"Berniocal Arcade (ScummVM freeware download)"})
with urllib.request.urlopen(req,timeout=90) as r: data=r.read()
assert hashlib.sha256(data).hexdigest()==SHA256,"Official game archive failed SHA256 verification"
source=zipfile.ZipFile(io.BytesIO(data))
files=[m for m in source.infolist() if not m.is_dir()]
names=[m.filename.replace("\\","/") for m in files]
print("Official files:",names)
exe=next((n for n in names if n.lower().endswith("/lure.exe") or n.lower()=="lure.exe"),None)
assert exe,"Official archive contains no original DOS LURE.EXE; cannot run via DOSBox"
common=[n.split("/") for n in names if "/" in n]
prefix=common[0][0]+"/" if len(common)==len(names) and all(c[0]==common[0][0] for c in common) else ""
if exe.startswith(prefix): exe=exe[len(prefix):]
directory=str(pathlib.PurePosixPath(exe).parent)
cd="" if directory=="." else "cd "+directory.replace("/","\\")+"\n"
conf=f"""[sdl]
fullscreen=false
[dosbox]
machine=svga_s3
memsize=16
[cpu]
core=auto
cycles=6000
[midi]
mpu401=none
[sblaster]
sbtype=sb16
[autoexec]
@echo off
mount c .
c:
{cd}LURE.EXE
"""
NOTICE="""Lure of the Temptress Copyright (C) Revolution Software Ltd.
Lure of the Temptress freeware licence
1) You may distribute this game for free on any medium, provided this license and all associated copyright notices and disclaimers are left intact.
2) You may charge a reasonable copying fee for this archive, and may distribute it in aggregate as part of a larger & possibly commercial software distribution (such as a Linux distribution or magazine coverdisk). You must provide proper attribution and ensure this license and all associated copyright notices, and disclaimers are left intact.
3) You may not charge a fee for the game itself. This includes reselling the game as an individual item.
4) You may modify the game as you wish. You may also distribute modified versions under the terms set forth in this license, but with the additional requirement that the work is marked with a prominent notice which states that it is a modified version.
5) All game content is (C) Revolution Software Ltd.
6) THE GAMEDATA IN THIS ARCHIVE IS PROVIDED "AS IS" AND WITHOUT ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING AND NOT LIMITED TO ANY IMPLIED WARRANTIES OF MERCHANTIBILITY AND FITNESS FOR A PARTICULAR PURPOSE.
"""
with zipfile.ZipFile("lure.jsdos","w",zipfile.ZIP_DEFLATED,compresslevel=6) as target:
 for m in files:
  path=m.filename.replace("\\","/")
  if path.startswith(prefix):path=path[len(prefix):]
  if not path or pathlib.PurePosixPath(path).is_absolute() or ".." in pathlib.PurePosixPath(path).parts:continue
  target.writestr(path,source.read(m))
 target.writestr(".jsdos/dosbox.conf",conf)
 target.writestr("LURE-LICENSE.txt",NOTICE)
 target.writestr("ORIGINAL-SOURCE.txt",f"Original freeware download: {URL}\nVerified SHA256: {SHA256}\nRepacked without changes to the original game files for js-dos browser DOSBox.\n")
print("Created lure.jsdos:",pathlib.Path("lure.jsdos").stat().st_size,"bytes; entrypoint:",exe)
