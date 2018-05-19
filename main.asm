Predef EQU $3e6d
predef: MACRO
	ld a,\1
	call Predef
ENDM

Bankswitch EQU $35d6
SECTION "Entrypoint",ROM0[$da65]
	ld hl, $d36e
	ld a,$21
	ld [hli],a
	ld a,$d3
	ld [hl],a
	predef 43
	predef 83
	predef 80
	ret


Init EQU $1f49
SECTION "Reset",ROM0[$d321]
Reset:
	jp Init
