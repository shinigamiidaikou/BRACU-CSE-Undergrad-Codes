; Write a procedure that prints all the
; prime numbers upto a given number. 

.MODEL SMALL

PRINT_STRING MACRO STR
	LEA DX, STR
	MOV AH, 9
	INT 21h
ENDM

PRINT_CHAR MACRO X
	MOV DX, X
	MOV AH, 2
	INT 21H
ENDM

.STACK 100H
.DATA

NUM1	DW 34
P2		DB "Prime numbers: $"

.CODE

PRIME_FINDING_N PROC
	    
    PRINT_STRING P2
    
    ;selected number CX
    MOV CX, 2
    L1:
    	;finding divisors upto CX
    	MOV BX, 2
    	L2:
    		CMP BX, CX
    		JE	PRIME
    		
    		MOV AX, CX
    		MOV DX, 0
    		DIV BX
    		CMP DX, 0
    		JE	BREAK
    		
    		INC BX
    		JMP L2
    		
    	PRIME:
    	MOV AX, CX
    	MOV BX, 10
    	PUSH CX
		MOV CX, 0
		ASCII_CONVERT:
			MOV DX, 0
			DIV BX
			ADD DX, 30H
			PUSH DX
			INC CX
			CMP AX, 0
			JE	PRINT
			JMP ASCII_CONVERT
		PRINT:
			POP DX
			PRINT_CHAR DX
			LOOP PRINT
		POP CX
		PRINT_CHAR 2CH
    		
    	BREAK:
    	MOV AX, NUM1
    	CMP CX, AX
    	JG	E1
    	INC CX
    	JMP L1
    E1:

PRIME_FINDING_N ENDP
JMP EX_CODE

MAIN PROC

; initialize DS
MOV AX,@DATA
MOV DS,AX
 
; code here

CALL PRIME_FINDING_N
EX_CODE:

;exit to DOS              
MOV AX, 4C00H
INT 21H

MAIN ENDP
    END MAIN
