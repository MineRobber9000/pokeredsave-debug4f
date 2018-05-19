# pokeredsave-base

A base for Pokemon Red save edits with RGBDS ASM.

Requires [my fork of RGBBIN](//github.com/MineRobber9000/rgbbin/tree/update-to-rgb-6) and [my .sav file library](//github.com/MineRobber9000/savfiles).

## `map` file
Tab-seperated. States where each sections belongs in the loaded game's RAM. Can only place from `$D2F7` to `$DA7F`.

Example:

```
Payload4F	$da65
Items		$d31f
```
