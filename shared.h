/*
 * Course IFJ @ FIT VUT Brno, 2015
 * IFJ15 Interpreter Project
 *
 * Authors:
 * Lukas Osadsky  - xosads00
 * Pavol Plaskon  - xplask00
 * Pavel Pospisil - xpospi88
 * Matej Postolka - xposto02
 *
 * Unless otherwise stated, all code is licensed under a
 * Creative Commons Attribution-ShareAlike 4.0 International License
 *
 */

#ifndef SHARED_H
#define SHARED_H

#include "ial.h"
#include "stack.h"

// Global ConstTab
extern htab_t *g_constTab;

// Global GlobalTab
extern htab_t *g_globalTab;

// Global FrameStack
extern TStack *g_frameStack;

void global_init();

#endif // SHARED_H
