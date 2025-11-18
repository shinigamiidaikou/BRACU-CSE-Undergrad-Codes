MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here

base_rate DW 1101110010b
usage_HIGH DW 000Ah
usage_LOW DW 40CDh
per_unit_cost DW 0050H
C DW ?

.CODE
MAIN PROC

; initialize DS

MOV AX,@DATA
MOV DS,AX
 
; enter your code here
MOV BX, per_unit_cost
SUB BX, 76

MOV CX, 100
MOV DX, usage_HIGH
MOV AX, usage_LOW 
DIV CX

MUL BX

MOV BX, base_rate
ADD AX, BX
 
MOV C, AX

;exit to DOS
               
MOV AX,4C00H
INT 21H

MAIN ENDP
END MAIN