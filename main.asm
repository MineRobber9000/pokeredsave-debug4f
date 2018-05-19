INCLUDE "hwc.asm"
INCLUDE "tc.asm"
INCLUDE "charmap.asm"

Predef EQU $3e6d
predef: MACRO
	ld a,\1
	call Predef
ENDM

SECTION "Blah",ROM0[$D6B8]
CallBase:
	ld a,SRAM_ENABLE
	ld [MBC1SRamEnable],a
	ld a,$01
	ld [MBC1SRamBankingMode],a
	ld [MBC1SRamBank],a
	ld de,.return
	push de
	jp hl
.return	xor a
	ld [MBC1SRamEnable],a
	ret

SECTION "Entrypoint4F",ROM0[$da65]
	ld hl, Akas
	call CallBase
	ret

PrintText EQU $3C49
SECTION "SRAM",ROM0[$a000]
Akas:
	ld hl, WhatText
	jp PrintText
	ret

WhatText:
	text "Hello! My name"
	next "is Robert!"
	prompt
	done
