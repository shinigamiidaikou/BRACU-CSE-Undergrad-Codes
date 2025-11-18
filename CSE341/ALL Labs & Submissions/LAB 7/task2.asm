; Write a macro to calculate factorial of a number.

.MODEL SMALL

FACTORIAL MACRO X
	; value considered to be within
	; data word limit.
	MOV AX, 1
	MOV CX, X
	L1:
		MUL CX
	LOOP L1
	MOV NUM1, AX
ENDM

PRINT_CHAR MACRO X
	MOV DX, X
	MOV AH, 2
	INT 21H
ENDM

PRINT_NUM MACRO X
	MOV AX, X
    MOV BX, 10
    MOV CX, 0
    ASCII_CONVERT:
    	MOV DX, 0
    	DIV BX
    	ADD DX, 30H
    	PUSH DX
    	CMP AX, 0
    	JE	PRINT
    	INC CX
    	JMP ASCII_CONVERT
    PRINT:
    	PRINT_LOOP:
    	POP DX
    	PRINT_CHAR DX
    	DEC CX 
    	CMP CX, 0
    	JGE PRINT_LOOP
ENDM

.STACK 100H
.DATA

NUM1	 DW 6
P2		 DB "FACTORIAL ANSWER: $"

.CODE
MAIN PROC

; initialize DS
MOV AX,@DATA
MOV DS,AX
 
; code here

FACTORIAL NUM1

PRINT_NUM NUM1

;exit to DOS              
MOV AX,4C00H
INT 21H

MAIN ENDP
    END MAIN
