; Write a macro to display a character string. The string is the macro parameter.

.MODEL SMALL

PRINT_STRING MACRO STR
	LEA DX, STR
	MOV AH, 9
	INT 21h
ENDM

.STACK 100H
.DATA
              
STR1 DB "TEST STRING!$"

.CODE
MAIN PROC

; initialize DS
MOV AX,@DATA
MOV DS,AX
 
; code here

PRINT_STRING STR1			

;exit to DOS              
MOV AX,4C00H
INT 21H

MAIN ENDP
    END MAIN
