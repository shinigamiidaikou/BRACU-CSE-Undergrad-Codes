.MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here
P1		DB "Enter a String: $"
P2		DB "Reversed String: $"

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
    
    MOV CX, 0
	L1:
    	MOV AH, 1
    	INT 21H
    	CMP AL, 0DH
    	JE	E1
    	PUSH AX
    	INC CX
    	JMP L1
    E1:
    
    ; NEWL + CRET
    MOV AH, 2 
    MOV DL, 0DH
    INT 21H
    MOV DL, 0AH
    INT 21H
    
    ; REVERSE PRINT
    
	L2:
		POP AX
		MOV DL, AL
		MOV AH, 2
		INT 21H
	LOOP L2
    
;exit to DOS
               
MOV AX,4C00H
INT 21H

MAIN ENDP
    END MAIN
