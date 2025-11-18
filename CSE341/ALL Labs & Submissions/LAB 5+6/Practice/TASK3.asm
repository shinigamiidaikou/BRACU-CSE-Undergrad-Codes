.MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here
NAME0 DB 20 DUP(?)
NAME1 DB "SHAFIN AHMED"

.CODE
MAIN PROC

; initialize DS

MOV AX,@DATA
MOV DS,AX
 
; enter your code here

    ; ARRAY ITERATION
    ; (Pointer method)
    LEA SI, NAME1
    MOV CX, 12
    
    PRINT_BLCK:
        MOV DL, [SI]
                
        MOV AH, 2
        INT 21H
        INC SI
    LOOP PRINT_BLCK
    
    ; CURSOR BREAK
    MOV AH, 2 
    MOV DL, 0DH
    INT 21H
    MOV DL, 0AH
    INT 21H
    
    
    ; (indexing method)
    MOV SI, 0
    MOV CX, 12
    
    PRINT_BLCK0:
        MOV DL, NAME1[SI]
        
        MOV AH, 2
        INT 21H
        INC SI
    LOOP PRINT_BLCK0

;exit to DOS
               
MOV AX,4C00H
INT 21H

MAIN ENDP
    END MAIN

