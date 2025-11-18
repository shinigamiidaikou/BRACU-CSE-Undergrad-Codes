.MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here
NUM1		DB 50 DUP(?)
P1			DB "Enter a number: $"
P2			DB "Digits are unique.$"
P3			DB "Digits are NOT unique.$"

.CODE
MAIN PROC

; initialize DS

MOV AX,@DATA
MOV DS,AX
 
; enter your code here

	; NUMBERS INPUT
    
    LEA DX, P1
    MOV AH, 9
    INT 21H
    
    MOV SI, 0
    MOV AH, 1
    INPUT:
    	INT 21H
    	CMP AL, 0DH
    	JE	EX1
    	MOV NUM1[SI], AL
    	INC SI
    	JMP INPUT
    EX1:
    MOV CX, SI
       
    ; NEWL + CRET
    MOV AH, 2 
    MOV DL, 0DH
    INT 21H
    MOV DL, 0AH
    INT 21H
    
    ; UNIQUE CHECKER
    
    MOV SI, 0
    MOV DI, 0 
    L1:
    	MOV AL, NUM1[SI]
    	CHECK_UNIQUE:
    		CMP DI, 0
    		JE	PUSH_UPTO_CURRENT
    		POP BX
    		CMP AL, BL
    		JE	NOT_UNIQUE
    		DEC DI
    		JMP CHECK_UNIQUE
    	PUSH_UPTO_CURRENT:
    		MOV AL, NUM1[DI]
    		PUSH AX
    		CMP DI, SI
    		JE	BREAK
    		INC DI
    		JMP PUSH_UPTO_CURRENT
    	BREAK:
    	INC SI
    LOOP L1
    
    UNIQUE:
    LEA DX, P2
    MOV AH, 9
    INT 21H
    JMP EXIT
    
    NOT_UNIQUE:
    LEA DX, P3
    MOV AH, 9
    INT 21H
    JMP EXIT
    
    EXIT:

;exit to DOS
               
MOV AX,4C00H
INT 21H

MAIN ENDP
    END MAIN
