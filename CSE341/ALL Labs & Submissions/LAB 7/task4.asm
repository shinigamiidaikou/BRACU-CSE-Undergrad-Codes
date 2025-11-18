; Write a macro to whether parenthesis in an equation are balanced or not.

.MODEL SMALL

Parentheses MACRO
	MOV SI, 0
	MOV CX, -1
	
	L1:
		MOV AL, equation[SI]
		CMP AL, '$'
		JE E1
		
		CMP AL, '('
		JE	OPEN
		CMP AL, ')'
		JE	CLOSE
		JMP C1
		
		OPEN:
			INC CX
			JMP C1
		
		CLOSE:
			CMP CX, -1
			JE	UNBALANCED
			DEC CX
			JMP C1
		
		C1:
			INC SI
			JMP L1
	E1:
	CMP	CX, -1
	JNE	UNBALANCED
	
	PRINT_STRING bMsg
	JMP Done
	
	UNBALANCED:
	PRINT_STRING ubMsg
	Done:

ENDM

PRINT_STRING MACRO STR
	LEA DX, STR
	MOV AH, 9
	INT 21h
ENDM

.STACK 100H
.DATA

equation DB '(67 + (3 * (10 - 5)))$'
bMsg 	 DB 'Parentheses are balanced.$'
ubMsg 	 DB 'Parentheses are NOT balanced.$'

.CODE
MAIN PROC

; initialize DS
MOV AX,@DATA
MOV DS,AX
 
; code here

Parentheses

;exit to DOS              
MOV AX, 4C00H
INT 21H

MAIN ENDP
    END MAIN
