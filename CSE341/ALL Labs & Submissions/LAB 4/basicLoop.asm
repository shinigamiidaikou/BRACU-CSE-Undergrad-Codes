.MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here

.CODE
MAIN PROC

; initialize DS

MOV AX,@DATA
MOV DS,AX
 
; enter your code here

mov cx,8

mov dl,2Ah
mov ah,2

start:
int 21h
loop start

;exit to DOS
               
MOV AX,4C00H
INT 21H

MAIN ENDP
    END MAIN
