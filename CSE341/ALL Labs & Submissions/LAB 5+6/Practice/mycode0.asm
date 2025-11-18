.MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here
arr1    db  1,2,3,4,5   ; Number array (8 bit)
arr2    dw  2,3,4,5,6   ; Number array (16 bit)
chr_arr db  "Hello"     ; Char array (8 bit)
arr     db  5 dup(?)    ; duplicated null array (8 bit)

.CODE
MAIN PROC

; initialize DS

MOV AX,@DATA
MOV DS,AX
 
; enter your code here

    ; ARRAY ITERATION
    ; (Pointer method)
    LEA SI, arr1
    MOV CX, 5
    
    PRINT_BLCK:
        MOV DL, [SI]
        ADD DL, 30H
        
        MOV AH, 2
        INT 21H
        INC SI
    LOOP PRINT_BLCK
    
    
    ; (indexing method)
    MOV SI, 0
    MOV CX, 5
    
    PRINT_BLCK0:
        MOV DL, [SI]
        ADD DL, 30H
        
        MOV AH, 2
        INT 21H
        INC SI
    LOOP PRINT_BLCK0
    
    ; STACK
    
    
    ; PUSH 16-BIT REG/CONST
    ; POP 16-BIT REG
    
    PUSH 24H
    MOV AX, 1234H
    PUSH AX
    POP CX
    
    PUSH F
    POP F 
           

;exit to DOS
               
MOV AX,4C00H
INT 21H

MAIN ENDP
    END MAIN

