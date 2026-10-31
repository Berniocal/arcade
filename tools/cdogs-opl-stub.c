/*
 * C-Dogs SDL WebAssembly build: silent replacement for the old MAME FM OPL chip.
 * Copyright (c) 2026 Arcade mobile adaptation authors.
 * SPDX-License-Identifier: GPL-2.0-only
 *
 * C-Dogs SDL's normal audio is handled by its freely licensed OGG assets.
 * The Wolfenstein mod's FM OPL chip is unnecessary for original Ogre/BEM
 * campaigns and its legacy upstream implementation has licensing ambiguity.
 * This stub preserves the interface without bundling its code.
 */
#include "fmopl.h"
#include <string.h>
int YM3812Init(int num, int clock, int rate)
{
    (void)num;
    (void)clock;
    (void)rate;
    return 0;
}
void YM3812Shutdown(void) {}
void YM3812ResetChip(int which) { (void)which; }
int YM3812Write(int which, int a, int v, const int *volume)
{
    (void)which; (void)a; (void)v; (void)volume;
    return 0;
}
unsigned char YM3812Read(int which, int a)
{
    (void)which; (void)a;
    return 0;
}
void YM3812Mute(int which, int channel, BOOL mute)
{
    (void)which; (void)channel; (void)mute;
}
int YM3812TimerOver(int which, int c)
{
    (void)which; (void)c;
    return 0;
}
void YM3812UpdateOne(int which, INT16 *buffer, int length)
{
    (void)which;
    if (buffer && length > 0) memset(buffer, 0, (size_t)length * sizeof(*buffer));
}
void YM3812SetTimerHandler(int which, OPL_TIMERHANDLER fn, int offset)
{
    (void)which; (void)fn; (void)offset;
}
void YM3812SetIRQHandler(int which, OPL_IRQHANDLER fn, int param)
{
    (void)which; (void)fn; (void)param;
}
void YM3812SetUpdateHandler(int which, OPL_UPDATEHANDLER fn, int param)
{
    (void)which; (void)fn; (void)param;
}
