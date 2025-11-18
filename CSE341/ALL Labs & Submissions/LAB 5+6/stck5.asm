.MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here
STR_ARR DB 500 DUP(?)
P1		DB "Enter a text: $"
P2		DB "Reverse Encoded text: $"

.CODE
MAIN PROC

; initialize DS

MOV AX,@DATA
MOV DS,AX
 
; code start

	; STRING INPUT
    
    LEA DX, P1
    MOV AH, 9
    INT 21H
    
    MOV SI, 0
	L1:
    	MOV AH, 1
    	INT 21H
    	CMP AL, 0DH
    	JE	E1
    	MOV STR_ARR[SI], AL
    	INC SI
    	JMP L1
    E1:
    
    ; NEWL + CRET
    MOV AH, 2 
    MOV DL, 0DH
    INT 21H
    MOV DL, 0AH
    INT 21H
    
    ; FINDING FACTORS
    
    MOV CX, SI
    MOV SI, 0
    MOV BX, 0
	L2:
		MOV DL, STR_ARR[SI]
		MOV DH, ' '
		CMP DL, DH
		JNE	CONTINUE
		MOV AH, 2
		REVERSE_PRINT:
			POP DX
			INT 21H
			DEC BX
			CMP BX, 0
			JNE REVERSE_PRINT
			CMP CX, 1
			JE	END_LOOP
			MOV DL, ' '
			INT 21H
			INC SI
			JMP END_LOOP
		CONTINUE:
		PUSH DX
		INC SI
		INC BX
		CMP CX, 1
		JE REVERSE_PRINT
		END_LOOP:
	LOOP L2
    
;exit to DOS
               
MOV AX,4C00H
INT 21H

MAIN ENDP
    END MAIN
