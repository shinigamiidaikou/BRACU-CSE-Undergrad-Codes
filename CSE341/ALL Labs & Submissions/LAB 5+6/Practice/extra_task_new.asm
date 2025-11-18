.MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here
NAME1 DB "DEMHA NIFAHS"


.CODE
MAIN PROC

; initialize DS

MOV AX,@DATA
MOV DS,AX
 
; enter your code here

    ; INPUT
    
    LEA SI, NAME1
    MOV CX, 12
    
    PUSH_BLCK:        
        MOV DX, [SI]
        PUSH DX       
        INC SI
    LOOP PUSH_BLCK
    
    ; REVERSE ITERATION
    

    MOV CX, 12
    PRINT_BLCK:
        POP DX
        
        MOV AH, 2
        INT 21H
        INC SI
    LOOP PRINT_BLCK

;exit to DOS
               
MOV AX,4C00H
INT 21H

MAIN ENDP
    END MAIN

