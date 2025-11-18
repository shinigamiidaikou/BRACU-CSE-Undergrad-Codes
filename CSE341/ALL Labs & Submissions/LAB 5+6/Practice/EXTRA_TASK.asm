.MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here
P1      DB "ENTER NAME: $?"
P2      DB "YOUR NAME IS: $"
NAME1   DB 6 DUP(?)

.CODE
MAIN PROC

; initialize DS

MOV AX,@DATA
MOV DS,AX
 
; enter your code here

    ; INPUT
    
    LEA DX, P1
    MOV AH, 9
    INT 21H
    
    LEA SI, NAME1
    MOV CX, 6
    
    INPUT_BLCK:        
        MOV AH, 1
        INT 21H
        MOV [SI], AL
        INC SI
    LOOP INPUT_BLCK
    
    ; ARRAY ITERATION
    ; (Pointer method)
    MOV AH, 2 
    MOV DL, 0DH
    INT 21H
    MOV DL, 0AH
    INT 21H
    
    LEA DX, P2
    MOV AH, 9
    INT 21H
    
    LEA SI, NAME1
    MOV CX, 6
    
    PRINT_BLCK:
        MOV DL, [SI]
        
        MOV AH, 2
        INT 21H
        INC SI
    LOOP PRINT_BLCK
    

;exit to DOS
               
MOV AX,4C00H
INT 21H

MAIN ENDP
    END MAIN

