.MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here
NUM1		DW ?
BUFF_NUM	DW ?
P1			DB "Enter a number: $"
P2			DB "Prime numbers: $"

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
    
    ; FINDING PRIMES
    
    LEA DX, P2
    MOV AH, 9
    INT 21H
    
    MOV CX, 2
    L2: 
    	MOV BX, 2
    	L3:
    		CMP BX, CX
    		JE	PRIME
    		MOV AX, CX
    		MOV DX, 0
    		DIV BX
    		CMP DX, 0
    		JE E3
    		INC BX
    		JMP L3
    		
    		PRIME:
    		MOV BUFF_NUM, CX
    		MOV BX, 10
    		PUSH CX
    		MOV CX, 0
    		ASCII_CONVERT:
    			MOV AX, BUFF_NUM
    			MOV DX, 0
    			DIV BX
    			ADD DX, 30H
    			PUSH DX
    			MOV BUFF_NUM, AX
    			CMP AX, 0
    			JE	PRINT
    			INC CX
    			JMP ASCII_CONVERT
    		PRINT:
    			MOV AH, 2
    			PRINT_LOOP:
    			POP DX
    			INT 21H
    			DEC CX 
    			CMP CX, 0
    			JGE PRINT_LOOP
    			POP CX
    			MOV AH, 2
    			MOV DL, 2CH
    			INT 21H
    	E3:
    	MOV AX, NUM1
    	CMP CX, AX
    	JG	EXIT
    	INC CX
    	JMP L2
    	
    EXIT:

;exit to DOS
               
MOV AX,4C00H
INT 21H

MAIN ENDP
    END MAIN
