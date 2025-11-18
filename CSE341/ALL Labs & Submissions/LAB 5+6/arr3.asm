.MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here
NUM1		DW 3 DUP(0)
BUFF_NUM	DW ?
BUFF_ARR	DB 5 DUP(?)
P1			DB "Enter Three numbers (Sep: ','): $"
P2			DB "Max Number: $"

.CODE
MAIN PROC

; initialize DS

MOV AX,@DATA
MOV DS,AX
 
; code start

	; NUMBERS INPUT
    
    LEA DX, P1
    MOV AH, 9
    INT 21H
    
    MOV SI, 0
    MOV CX, 3
    OUTER1:
    	MOV BX, 10
    	MOV BUFF_NUM, 0
    	INNER:
    		MOV AH, 1
    		INT 21H
    		CMP AL, 2CH
    		JE	D1
    		CMP AL, 0DH
    		JE	D1
    		SUB AL, 30H
    		MOV AH, 0
    		MOV DX, BUFF_NUM
    		MOV BUFF_NUM, AX
    		MOV AX, DX
    		MUL BX
    		ADD BUFF_NUM, AX
    		JMP INNER
    	D1:
    	MOV BX, BUFF_NUM
    	MOV NUM1[SI], BX
    	ADD SI, 2
    LOOP OUTER1
    
    ; NEWL + CRET
    MOV AH, 2 
    MOV DL, 0DH
    INT 21H
    MOV DL, 0AH
    INT 21H
    
    ; ARRAY SORT
    
    MOV SI, 0
    MOV CX, 2
    I_LOOP:
    	MOV DI, SI
    	ADD DI, 2
    	J_LOOP:
    		MOV AX, NUM1[SI]
    		MOV BX, NUM1[DI]
    	    CMP AX, BX
    	    JLE CONTINUE
    	    MOV NUM1[SI], BX
    	    MOV NUM1[DI], AX
    	    CONTINUE:
    	    ADD DI, 2
    	    CMP DI, 10
    	    JL J_LOOP
    	ADD SI, 2
    LOOP I_LOOP

    ; MAX NUMBER PRINT
    
    LEA DX, P2
    MOV AH, 9
    INT 21H
    
    MOV AX, NUM1[4]
    MOV BUFF_NUM, AX
    MOV DI, 0
    MOV BX, 10
    ASCII_CONVERT:
    	MOV AX, BUFF_NUM
    	MOV DX, 0
    	DIV BX
    	ADD DX, 30H
    	MOV BUFF_ARR[DI], DL
    	MOV BUFF_NUM, AX
    	CMP AX, 0
    	JE	PRINT
    	INC DI
    	JMP ASCII_CONVERT
    PRINT:
    	MOV AH, 2
    	PRINT_LOOP:
    	MOV DL, BUFF_ARR[DI]
    	INT 21H
    	DEC DI 
    	CMP DI, 0
    	JGE PRINT_LOOP

;exit to DOS
               
MOV AX,4C00H
INT 21H

MAIN ENDP
    END MAIN
