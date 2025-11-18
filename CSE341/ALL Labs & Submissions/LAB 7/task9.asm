; Write a program that checks whether
; value exists in the array or not using
; procedure.

.MODEL SMALL

PRINT_STRING MACRO X
	LEA DX, X
	MOV AH, 9
	INT 21H
ENDM

.STACK 100H
.DATA

NUM_ARR DW -234,212,1234,-245,32456,23 ; SIGNED DECIMAL NUM ARRAY
LEN_ARR	DW 6

NUM1	DW 453  ; Searching value

P1		DB "Value Exists!$"
P2		DB "Value Does NOT Exist!$"

.CODE

SEARCH PROC
	
	MOV SI, 0
	MOV CX, LEN_ARR
	MOV BX, NUM1
	L1:
		MOV AX, NUM_ARR[SI]
		CMP AX, BX
		JE	FOUND
		ADD SI, 2
	LOOP L1
	
	PRINT_STRING P2
	JMP EX
	
	FOUND:
	PRINT_STRING P1

	EX:
	   	
SEARCH ENDP
JMP EX_PROC

MAIN PROC

; initialize DS
MOV AX,@DATA
MOV DS,AX
 
; code here

CALL SEARCH
EX_PROC:

;exit to DOS              
MOV AX, 4C00H
INT 21H

MAIN ENDP
    END MAIN
