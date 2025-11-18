.MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here
NUM1	DW ?
P1		DB "Enter a number: $"
P2		DB "Factors Stored in Stack!$"

.CODE
MAIN PROC

; initialize DS

MOV AX,@DATA
MOV DS,AX
 
; code start

	; NUMBER INPUT
    
    LEA DX, P1
    MOV AH, 9
    INT 21H
    
    MOV BX, 10
	L1:
    	MOV AH, 1
    	INT 21H
    	CMP AL, 0DH
    	JE	E1
    	SUB AL, 30H
    	MOV AH, 0
    	MOV DX, NUM1
    	MOV NUM1, AX
    	MOV AX, DX
    	MUL BX
    	ADD NUM1, AX
    	JMP L1
    E1:
    
    ; NEWL + CRET
    MOV AH, 2 
    MOV DL, 0DH
    INT 21H
    MOV DL, 0AH
    INT 21H
    
    ; FINDING FACTORS
    
    PUSH 1
    MOV CX, 2
    L2:
    	MOV AX, NUM1
    	MOV DX, 0
    	DIV CX
    	CMP DX, 0
    	JNE CONTINUE
    	PUSH CX
    	CONTINUE:
    	INC CX
    	MOV AX, NUM1
    	CMP CX, AX
    	JG	EXIT 
    	JMP L2
    
    EXIT:
    LEA DX, P2
    MOV AH, 9
    INT 21H
    
;exit to DOS
               
MOV AX,4C00H
INT 21H

MAIN ENDP
    END MAIN
