.MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here
NAME0	DB 50 dup(?)
LEN0	DB 0
P0		DB "LENGTH: $"
P1		DB "ENTER NAME: $?"
P2      DB "YOUR NAME IS: $"

.CODE
MAIN PROC

; initialize DS

MOV AX,@DATA
MOV DS,AX
 
; enter your code here

	; LENGTH INPUT
    
    LEA DX, P0
    MOV AH, 9
    INT 21H
    
    MOV BL, 10
    LEN_INPUT:
    	MOV AH, 1
    	INT 21H
    	CMP AL, 0DH
    	JE DONE
    	MOV DL, AL
    	SUB DL, 30H
    	MOV AL, LEN0
    	MUL BL
    	ADD AL, DL
    	MOV LEN0, AL
    	JMP LEN_INPUT
    DONE:
    
    ; NEWL + CRET
    MOV AH, 2 
    MOV DL, 0DH
    INT 21H
    MOV DL, 0AH
    INT 21H
    
    ; NAME INPUT
    
    LEA DX, P1
    MOV AH, 9
    INT 21H
    
    LEA SI, NAME0
    MOV CH, 0
    MOV CL, LEN0
    
    NAME_INPUT:        
        MOV AH, 1
        INT 21H
        MOV [SI], AL
        INC SI
    LOOP NAME_INPUT
    
    ; NEWL + CRET
    MOV AH, 2 
    MOV DL, 0DH
    INT 21H
    MOV DL, 0AH
    INT 21H

    ; NAME OUTPUT
    
    LEA DX, P2
    MOV AH, 9
    INT 21H
    
    LEA SI, NAME0
    MOV CH, 0
    MOV CL, LEN0
    
    NAME_OUTPUT:        
        MOV DL, [SI]
        MOV AH, 2
        INT 21H
        INC SI
    LOOP NAME_OUTPUT

;exit to DOS
               
MOV AX,4C00H
INT 21H

MAIN ENDP
    END MAIN
